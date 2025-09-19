# Student Management System - Installation Guide

## Prerequisites

Before installing the Student Management System, ensure you have the following software installed on your system:

### Required Software
- **Python 3.8 or higher** - [Download from python.org](https://www.python.org/downloads/)
- **Git** (optional, for version control) - [Download from git-scm.com](https://git-scm.com/)
- **Web Browser** - Chrome, Firefox, Edge, or Safari

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux Ubuntu 18.04+
- **RAM**: Minimum 4GB, Recommended 8GB
- **Storage**: At least 1GB free space
- **Network**: Internet connection for downloading dependencies

## Installation Steps

### Step 1: Download the Project

#### Option A: Download ZIP File
1. Download the project ZIP file
2. Extract to your desired location (e.g., `C:\Projects\StudentManagementSystem`)

#### Option B: Clone with Git (if available)
```bash
git clone <repository-url>
cd StudentManagementSystem
```

### Step 2: Set Up Python Environment

#### Windows
1. Open Command Prompt as Administrator
2. Navigate to the project directory:
   ```cmd
   cd C:\path\to\StudentManagementSystem
   ```

3. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```

4. Activate the virtual environment:
   ```cmd
   venv\Scripts\activate
   ```

#### macOS/Linux
1. Open Terminal
2. Navigate to the project directory:
   ```bash
   cd /path/to/StudentManagementSystem
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Step 3: Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
cd src
pip install -r requirements.txt
```

This will install:
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.5
- Werkzeug 2.3.7
- Jinja2 3.1.2
- And other dependencies

### Step 4: Initialize the Database

The database will be automatically created when you first run the application. The system will create:
- SQLite database file: `student_management.db`
- Default admin user with credentials: `admin` / `admin123`

### Step 5: Run the Application

1. Ensure you're in the `src` directory and virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```

3. You should see output similar to:
   ```
   Default admin created: username='admin', password='admin123'
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5000
   * Running on http://[your-ip]:5000
   ```

### Step 6: Access the Application

1. Open your web browser
2. Navigate to: `http://localhost:5000`
3. You should see the Student Management System home page

## First Time Setup

### Login to Admin Panel
1. Click "Admin Login" on the home page
2. Use the default credentials:
   - **Username**: `admin`
   - **Password**: `admin123`
3. You'll be redirected to the dashboard

### Add Sample Data
1. Navigate to "Students" and click "Add New Student"
2. Fill in sample student information
3. Navigate to "Courses" and click "Add New Course"
4. Create sample courses

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Python is not recognized"
**Solution**: 
- Ensure Python is installed and added to PATH
- Try using `python3` instead of `python`
- Reinstall Python with "Add to PATH" option checked

#### Issue: "pip is not recognized"
**Solution**:
- Ensure pip is installed with Python
- Try using `python -m pip` instead of `pip`

#### Issue: "Permission denied" errors
**Solution**:
- Run Command Prompt/Terminal as Administrator
- Check file permissions in the project directory

#### Issue: "Module not found" errors
**Solution**:
- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`
- Check Python version compatibility

#### Issue: "Port 5000 already in use"
**Solution**:
- Kill the process using port 5000
- Or modify `app.py` to use a different port:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)
  ```

#### Issue: Database errors
**Solution**:
- Delete the `student_management.db` file and restart the application
- Check file permissions in the project directory

### Performance Issues

#### Slow Loading
- Ensure you have sufficient RAM available
- Close unnecessary applications
- Check internet connection for CDN resources

#### Database Performance
- The SQLite database is suitable for development and small deployments
- For production use, consider PostgreSQL or MySQL

## Development Setup

### For Development Work

1. **Enable Debug Mode**: Already enabled in `app.py`
2. **Code Editor**: Use Visual Studio Code with Python extension
3. **Browser Developer Tools**: Use for frontend debugging

### File Structure Understanding
```
StudentManagementSystem/
├── README.md                 # Project overview
├── INSTALLATION_GUIDE.md     # This file
├── documentation/            # Project documentation
├── certificates/            # Required certificates
├── screenshots/             # Application screenshots
└── src/                     # Source code
    ├── app.py              # Main Flask application
    ├── requirements.txt    # Python dependencies
    ├── static/             # CSS, JS, images
    ├── templates/          # HTML templates
    └── student_management.db # SQLite database (created at runtime)
```

## Security Considerations

### Default Credentials
**Important**: Change the default admin password after first login by modifying the `init_db()` function in `app.py`.

### Production Deployment
For production use:
1. Change the `SECRET_KEY` in `app.py`
2. Use environment variables for sensitive data
3. Use a production WSGI server like Gunicorn
4. Implement HTTPS
5. Use a production database (PostgreSQL/MySQL)

## Backup and Maintenance

### Database Backup
The SQLite database file `student_management.db` contains all your data. To backup:
1. Stop the application
2. Copy the `student_management.db` file to a safe location
3. Restart the application

### Regular Maintenance
- Keep Python and dependencies updated
- Regular database backups
- Monitor application logs
- Update security configurations

## Getting Help

### Documentation
- Check the `documentation/` folder for detailed project information
- Review the code comments in `app.py` for technical details

### Common Resources
- Flask Documentation: https://flask.palletsprojects.com/
- Python Documentation: https://docs.python.org/
- Bootstrap Documentation: https://getbootstrap.com/

### Support
For technical issues:
1. Check this troubleshooting section
2. Review the project documentation
3. Consult the Flask and Python documentation
4. Check online forums and communities

## Uninstallation

To remove the Student Management System:

1. **Stop the application** (Ctrl+C in the terminal)
2. **Deactivate virtual environment**:
   ```bash
   deactivate
   ```
3. **Delete the project folder** and all its contents
4. **Remove Python virtual environment** (if no longer needed)

## Next Steps

After successful installation:
1. Explore the application features
2. Add sample data to test functionality
3. Review the documentation for detailed feature explanations
4. Consider customizations for your specific needs

## Version Information

- **Application Version**: 1.0.0
- **Python Version**: 3.8+
- **Flask Version**: 2.3.3
- **Database**: SQLite 3.x
- **Frontend**: Bootstrap 5.1.3

---

**Note**: This installation guide is part of the NIELIT project submission and follows the institutional guidelines for project documentation and setup procedures.