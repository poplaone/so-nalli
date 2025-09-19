# 🎓 Student Management System

A modern, responsive Student Management System built with Flask and enhanced with glassmorphism design. This project was developed as part of the NIELIT O-Level course by **Sonal Chauhan**.

![Student Management System](https://img.shields.io/badge/Python-Flask-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 🌟 Features

### 🎨 Modern UI/UX
- **Glassmorphism Design** - Beautiful translucent effects with backdrop blur
- **Mobile-First Responsive** - Perfect experience on all devices
- **Dark/Light Theme Support** - Adaptive color schemes
- **Smooth Animations** - Engaging micro-interactions
- **Toast Notifications** - Modern feedback system

### 👨‍🎓 Student Management
- **Student Registration** - Add new students with detailed information
- **Student Profiles** - Comprehensive student information display
- **Search & Filter** - Real-time search across all student data
- **Bulk Operations** - Efficient management of multiple records

### 📚 Course Management
- **Course Creation** - Add courses with detailed descriptions
- **Course Catalog** - Beautiful grid layout with search functionality
- **Credit System** - Track course credits and requirements
- **Course Statistics** - Monitor enrollment and completion rates

### 📊 Dashboard Analytics
- **Real-time Statistics** - Live system metrics and insights
- **Interactive Charts** - Visual data representation
- **System Status** - Monitor application health
- **Activity Timeline** - Track recent system events

### 🔐 Authentication & Security
- **Admin Authentication** - Secure login system
- **Session Management** - Proper user session handling
- **Input Validation** - Comprehensive data validation
- **CSRF Protection** - Security against cross-site attacks

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python src/app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Default admin credentials: `admin` / `password`

## 📁 Project Structure

```
student-management-system/
├── src/
│   ├── app.py                 # Main Flask application
│   ├── models.py              # Database models
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Enhanced responsive styles
│   │   ├── js/
│   │   │   └── script.js      # Interactive functionality
│   │   └── images/            # Project images
│   └── templates/
│       ├── base.html          # Base template with navigation
│       ├── index.html         # Landing page
│       ├── dashboard.html     # Admin dashboard
│       ├── students.html      # Student management
│       ├── courses.html       # Course management
│       └── ...               # Other templates
├── documentation/             # Project documentation
├── certificates/             # Academic certificates
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5 + Custom CSS
- **Icons**: Font Awesome 6
- **Fonts**: Inter (Google Fonts)

## 📱 Responsive Design

The application is built with a mobile-first approach:

- **Mobile (320px+)**: Optimized touch interface
- **Tablet (768px+)**: Enhanced layout with sidebars
- **Desktop (1024px+)**: Full-featured dashboard experience
- **Large Screens (1440px+)**: Maximized content area

## 🎨 Design Features

### Glassmorphism Effects
- Translucent backgrounds with backdrop blur
- Subtle borders and shadows
- Layered depth perception
- Modern aesthetic appeal

### Interactive Elements
- Hover animations and transitions
- Loading states for better UX
- Smooth page transitions
- Responsive feedback

### Color Scheme
- Primary: Indigo (#4f46e5)
- Secondary: Cyan (#06b6d4)
- Success: Emerald (#10b981)
- Warning: Amber (#f59e0b)
- Danger: Red (#ef4444)

## 📊 Features Overview

### Dashboard
- System analytics with real-time data
- Quick action buttons
- Activity timeline
- System status monitoring

### Student Management
- Add/Edit/Delete students
- Advanced search and filtering
- Student profile modals
- Bulk operations

### Course Management
- Course catalog with grid layout
- Real-time search functionality
- Course details modals
- Credit tracking system

## 🔧 Configuration

### Database Configuration
The application uses SQLite by default. To use a different database:

1. Update the `SQLALCHEMY_DATABASE_URI` in `app.py`
2. Install the appropriate database driver
3. Run the application to create tables

### Environment Variables
Create a `.env` file for configuration:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///student_management.db
DEBUG=True
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sonal Chauhan**
- Registration: 1668886
- Roll Number: 8559025357
- Course: NIELIT O-Level
- Institution: Vertex Institute

## 🙏 Acknowledgments

- NIELIT for the O-Level curriculum
- Vertex Institute for guidance and support
- Flask community for excellent documentation
- Bootstrap team for the responsive framework

## 📞 Support

If you have any questions or need support, please:
1. Check the [Issues](https://github.com/yourusername/student-management-system/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

## 🔄 Updates

### Version 1.0.0 (Current)
- Initial release with full functionality
- Modern glassmorphism design
- Mobile-responsive interface
- Complete CRUD operations
- Authentication system
- Dashboard analytics

---

⭐ **Star this repository if you found it helpful!**

Made with ❤️ by Sonal Chauhan for NIELIT O-Level Project