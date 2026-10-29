# ☁️ NebulaVault — Cloud Storage Management Dashboard

A modern, space-inspired file management dashboard built using Python and Flask. NebulaVault demonstrates the core workflow of a cloud-storage application, including file uploads, downloads, deletion, metadata management, search, and storage analytics.

> **Project Type:** Cloud Computing Mini Project  
> **Status:** Functional Local Prototype  
> **Domain:** Cloud Computing · Web Development · File Management

---

## ✨ Overview

Managing digital files becomes easier when users can organize, search, and access them through a centralized interface.

**NebulaVault** is a web-based file management application designed with a futuristic dark UI and an interactive storage dashboard. It allows users to upload files, explore stored files, filter by file type, monitor storage usage, and perform file operations through a browser.

The project demonstrates how a frontend, application server, metadata database, and storage layer work together in a file-storage system.

**Note:** The current version runs locally. File contents are stored on the local machine, and SQLite stores file metadata. Integration with cloud object storage and cloud deployment are planned future enhancements.

## 🚀 Features

- **Interactive Dashboard:** View file count, total storage used, and largest-file statistics.
- **File Upload:** Upload files through a browser-based interface.
- **Download & Delete:** Download stored files or remove them from the system.
- **Search:** Find files by filename.
- **File-Type Filtering:** Filter files by category.
- **Drag-and-Drop Interface:** Select files using the dashboard's drag-and-drop workflow.
- **Metadata Management:** Store file names, sizes, and upload timestamps in SQLite.
- **Filename Sanitization:** Use Werkzeug's `secure_filename` utility when handling uploaded filenames.
- **Upload Size Limit:** Restrict individual uploads to 25 MB.
- **Modern UI:** Responsive, space-inspired styling with a dark theme and neon accents.

## 🖥️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| Flask | Web framework and HTTP routing |
| SQLite | Persistent file metadata |
| HTML | Dashboard structure |
| CSS | Styling and responsive layout |
| JavaScript | Client-side search, filtering, and interactions |
| Werkzeug | Secure filename handling |
| Waitress | WSGI server dependency for deployment preparation |

## 🏗️ System Architecture

```text
              User / Browser
                    |
                    v
          NebulaVault Dashboard
             HTML / CSS / JS
                    |
                    v
             Flask Backend
                    |
          +---------+---------+
          |                   |
          v                   v
   Local File Storage    SQLite Database
       uploads/              vault.db
          |                   |
          +---------+---------+
                    |
                    v
       File Operations & Metrics
```

### How it works

1. The user accesses the dashboard through a browser.
2. Flask receives file-operation requests.
3. Uploaded files are saved in the local `uploads/` directory.
4. SQLite stores metadata such as filenames, file sizes, and upload timestamps.
5. The dashboard retrieves metadata and calculates storage statistics.
6. Users can search, filter, download, or delete files through the interface.

## 📂 Project Structure

```text
NebulaVault/
├── app.py                 # Flask application and backend routes
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── PROJECT_REPORT.md      # Academic project report
├── Procfile               # WSGI deployment starter
├── render.yaml            # Hosting configuration starter
├── templates/
│   └── index.html         # Dashboard interface
├── static/
│   └── style.css          # UI styling
└── uploads/               # Local uploaded-file storage
```

The SQLite database, `vault.db`, is initialized by the application when it runs.

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or later
- Git (optional, for cloning the repository)
- Visual Studio Code or another code editor

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username after publishing the repository.

```bash
git clone https://github.com/YOUR-USERNAME/NebulaVault.git
cd NebulaVault
```

Alternatively, download the repository as a ZIP and extract it.

### 2. Create a virtual environment

**Windows:**

```powershell
py -m venv .venv
```

### 3. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
.\.venv\Scripts\python.exe app.py
```

### 5. Open the dashboard

Visit:

**http://127.0.0.1:5000**

Upload a sample file to explore the dashboard and test its file-management features.

## 🧪 Testing Checklist

- [ ] Launch the application successfully.
- [ ] Upload a supported sample file.
- [ ] Confirm the file appears in the dashboard.
- [ ] Search for a file by name.
- [ ] Filter files by type.
- [ ] Download a stored file.
- [ ] Delete a file and confirm it disappears.
- [ ] Verify that the dashboard statistics update after file operations.
- [ ] Confirm that files larger than the 25 MB limit are rejected.

## ☁️ Cloud Computing Concepts

This project provides a practical starting point for understanding the architecture of a storage service.

- **Application Layer:** Flask processes user requests and performs file operations.
- **Storage Layer:** The current implementation uses local file storage.
- **Metadata Layer:** SQLite maintains an index of stored files.
- **Usage Monitoring:** The dashboard calculates file count and storage usage.
- **Cloud Migration:** The local storage layer could be replaced with an object-storage service such as Amazon S3 or Azure Blob Storage.
- **Cloud Deployment:** The application could be deployed to a cloud hosting platform with appropriate configuration.

The current implementation is a local prototype, not a production cloud-storage service.

## 🔐 Security Considerations

Security measures and limitations include:

- Uploaded filenames are sanitized using Werkzeug.
- Database operations use parameterized SQL queries.
- Individual file uploads are limited to 25 MB.
- Authentication, authorization, malware scanning, and production-grade access controls have not been implemented.

**Use this project for educational and demonstration purposes only. Do not upload sensitive or confidential files.**

## 🔮 Future Enhancements

- Integrate Amazon S3 or Azure Blob Storage for cloud-based file storage.
- Deploy the application to a cloud hosting platform.
- Implement user authentication and role-based access control.
- Add file-sharing links with controlled access.
- Introduce storage quotas and audit logs.
- Add cloud monitoring, logging, and a managed database.
- Implement file validation and malware scanning.

## 📚 Learning Outcomes

Through this project, I explored:

- Building a web application with Python and Flask.
- Implementing file upload, download, and deletion workflows.
- Connecting a backend application to an SQLite database.
- Managing file metadata and calculating storage metrics.
- Designing a dashboard with search and filtering functionality.
- Understanding the separation between application logic, metadata, and file storage.
- Identifying the architectural changes required to move a local prototype to cloud infrastructure.

## 👩‍💻 Author

**Shrutika Patil**

- GitHub: https://github.com/patilyshrutika
- LinkedIn: https://www.linkedin.com/in/shrutika-patil-0a340832a/

---

*Built as a learning project to explore file management, backend development, and cloud-storage architecture.*
