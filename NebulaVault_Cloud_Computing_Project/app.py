from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import sqlite3

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DATABASE = os.path.join(BASE_DIR, "vault.db")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "nebula-vault-demo-key")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_name TEXT NOT NULL,
                stored_name TEXT NOT NULL,
                size INTEGER NOT NULL,
                uploaded_at TEXT NOT NULL
            )
        """)

def readable_size(size):
    if size < 1024:
        return f"{size} B"
    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 * 1024):.2f} MB"

@app.template_filter("filesize")
def filesize(size):
    return readable_size(size)

@app.template_filter("filekind")
def filekind(name):
    ext = os.path.splitext(name.lower())[1]
    if ext in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
        return ("IMG", "image")
    if ext in {".pdf"}:
        return ("PDF", "pdf")
    if ext in {".zip", ".rar", ".7z"}:
        return ("ZIP", "archive")
    if ext in {".py", ".js", ".html", ".css", ".c", ".cpp", ".java"}:
        return ("DEV", "code")
    if ext in {".mp4", ".mov", ".mp3", ".wav"}:
        return ("MED", "media")
    return ("FILE", "generic")

@app.route("/")
def index():
    with get_db() as conn:
        files = conn.execute("SELECT * FROM files ORDER BY id DESC").fetchall()
    total_bytes = sum(row["size"] for row in files)
    largest = max((row["size"] for row in files), default=0)
    return render_template("index.html", files=files, total=len(files),
                           total_size=readable_size(total_bytes), raw_bytes=total_bytes,
                           largest=readable_size(largest))

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file or not file.filename:
        flash("Choose a file before uploading.", "error")
        return redirect(url_for("index"))
    original_name = secure_filename(file.filename)
    if not original_name:
        flash("Please rename the file and try again.", "error")
        return redirect(url_for("index"))
    stored_name = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}_{original_name}"
    path = os.path.join(app.config["UPLOAD_FOLDER"], stored_name)
    file.save(path)
    size = os.path.getsize(path)
    with get_db() as conn:
        conn.execute(
            "INSERT INTO files (original_name, stored_name, size, uploaded_at) VALUES (?, ?, ?, ?)",
            (original_name, stored_name, size, datetime.now().strftime("%d %b %Y · %I:%M %p"))
        )
    flash(f"{original_name} is now in your vault.", "success")
    return redirect(url_for("index"))

@app.route("/download/<int:file_id>")
def download(file_id):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM files WHERE id = ?", (file_id,)).fetchone()
    if not row:
        flash("That file could not be found.", "error")
        return redirect(url_for("index"))
    return send_from_directory(app.config["UPLOAD_FOLDER"], row["stored_name"],
                               as_attachment=True, download_name=row["original_name"])

@app.route("/delete/<int:file_id>", methods=["POST"])
def delete(file_id):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM files WHERE id = ?", (file_id,)).fetchone()
        if row:
            path = os.path.join(app.config["UPLOAD_FOLDER"], row["stored_name"])
            if os.path.exists(path):
                os.remove(path)
            conn.execute("DELETE FROM files WHERE id = ?", (file_id,))
            flash("File removed from your vault.", "success")
        else:
            flash("That file could not be found.", "error")
    return redirect(url_for("index"))

@app.errorhandler(413)
def too_large(_error):
    flash("File exceeds the 25 MB demo limit.", "error")
    return redirect(url_for("index"))

init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=False)
