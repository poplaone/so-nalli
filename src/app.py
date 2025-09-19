"""
Student Management System - Main Application
NIELIT Project by [Student Name]
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///student_management.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.Text)
    date_of_birth = db.Column(db.Date)
    enrollment_date = db.Column(db.Date, default=datetime.utcnow)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10), unique=True, nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, default=3)
    description = db.Column(db.Text)

class Grade(db.Model):
    grade_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    grade = db.Column(db.String(2))
    semester = db.Column(db.String(20))
    academic_year = db.Column(db.String(9))

# Routes
@app.route('/')
def index():
    """Home page route"""
    if 'admin_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login route"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and check_password_hash(admin.password_hash, password):
            session['admin_id'] = admin.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout route"""
    session.pop('admin_id', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """Dashboard route"""
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    # Get statistics
    total_students = Student.query.count()
    total_courses = Course.query.count()
    total_grades = Grade.query.count()
    
    return render_template('dashboard.html', 
                         total_students=total_students,
                         total_courses=total_courses,
                         total_grades=total_grades)

@app.route('/students')
def students():
    """Students list route"""
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    """Add new student route"""
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            student = Student(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                phone=request.form['phone'],
                address=request.form['address'],
                date_of_birth=datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
            )
            db.session.add(student)
            db.session.commit()
            flash('Student added successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            flash('Error adding student!', 'error')
    
    return render_template('add_student.html')

@app.route('/courses')
def courses():
    """Courses list route"""
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    """Add new course route"""
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            course = Course(
                course_code=request.form['course_code'],
                course_name=request.form['course_name'],
                credits=int(request.form['credits']),
                description=request.form['description']
            )
            db.session.add(course)
            db.session.commit()
            flash('Course added successfully!', 'success')
            return redirect(url_for('courses'))
        except Exception as e:
            flash('Error adding course!', 'error')
    
    return render_template('add_course.html')

def init_db():
    """Initialize database with sample data"""
    with app.app_context():
        db.create_all()
        
        # Create admin user if not exists
        if not Admin.query.first():
            admin = Admin(
                username='admin',
                password_hash=generate_password_hash('admin123')
            )
            db.session.add(admin)
            db.session.commit()
            print("Default admin created: username='admin', password='admin123'")
        
        # Add sample students if none exist
        if Student.query.count() == 0:
            sample_students = [
                Student(
                    first_name="John",
                    last_name="Doe",
                    email="john.doe@email.com",
                    phone="(555) 123-4567",
                    address="123 Main Street, New York, NY 10001",
                    date_of_birth=datetime(2000, 5, 15).date(),
                    enrollment_date=datetime(2023, 9, 1).date()
                ),
                Student(
                    first_name="Jane",
                    last_name="Smith",
                    email="jane.smith@email.com",
                    phone="(555) 987-6543",
                    address="456 Oak Avenue, Los Angeles, CA 90210",
                    date_of_birth=datetime(1999, 12, 8).date(),
                    enrollment_date=datetime(2023, 9, 1).date()
                ),
                Student(
                    first_name="Mike",
                    last_name="Johnson",
                    email="mike.johnson@email.com",
                    phone="(555) 456-7890",
                    address="789 Pine Road, Chicago, IL 60601",
                    date_of_birth=datetime(2001, 3, 22).date(),
                    enrollment_date=datetime(2023, 9, 15).date()
                ),
                Student(
                    first_name="Sarah",
                    last_name="Williams",
                    email="sarah.williams@email.com",
                    phone="(555) 321-9876",
                    address="321 Elm Street, Houston, TX 77001",
                    date_of_birth=datetime(2000, 8, 10).date(),
                    enrollment_date=datetime(2023, 8, 20).date()
                ),
                Student(
                    first_name="David",
                    last_name="Brown",
                    email="david.brown@email.com",
                    phone="(555) 654-3210",
                    address="654 Maple Drive, Phoenix, AZ 85001",
                    date_of_birth=datetime(1998, 11, 5).date(),
                    enrollment_date=datetime(2023, 9, 10).date()
                ),
                Student(
                    first_name="Emily",
                    last_name="Davis",
                    email="emily.davis@email.com",
                    phone="(555) 789-0123",
                    address="987 Cedar Lane, Philadelphia, PA 19101",
                    date_of_birth=datetime(2001, 7, 18).date(),
                    enrollment_date=datetime(2023, 9, 5).date()
                )
            ]
            
            for student in sample_students:
                db.session.add(student)
            
            db.session.commit()
            print(f"Added {len(sample_students)} sample students")
        
        # Add sample courses if none exist
        if Course.query.count() == 0:
            sample_courses = [
                Course(
                    course_code="CS101",
                    course_name="Introduction to Computer Science",
                    credits=3,
                    description="Fundamental concepts of computer science including programming basics, algorithms, and data structures."
                ),
                Course(
                    course_code="MATH201",
                    course_name="Calculus I",
                    credits=4,
                    description="Differential and integral calculus with applications to science and engineering."
                ),
                Course(
                    course_code="ENG101",
                    course_name="English Composition",
                    credits=3,
                    description="Academic writing skills, critical thinking, and communication techniques."
                ),
                Course(
                    course_code="PHYS101",
                    course_name="General Physics I",
                    credits=4,
                    description="Mechanics, thermodynamics, and wave motion with laboratory component."
                ),
                Course(
                    course_code="CHEM101",
                    course_name="General Chemistry",
                    credits=4,
                    description="Atomic structure, chemical bonding, stoichiometry, and basic organic chemistry."
                ),
                Course(
                    course_code="HIST101",
                    course_name="World History",
                    credits=3,
                    description="Survey of world civilizations from ancient times to the present."
                ),
                Course(
                    course_code="BIO101",
                    course_name="Introduction to Biology",
                    credits=4,
                    description="Cell biology, genetics, evolution, and ecology with laboratory work."
                ),
                Course(
                    course_code="ART101",
                    course_name="Art Appreciation",
                    credits=2,
                    description="Introduction to visual arts, art history, and aesthetic principles."
                )
            ]
            
            for course in sample_courses:
                db.session.add(course)
            
            db.session.commit()
            print(f"Added {len(sample_courses)} sample courses")
        
        # Add sample grades if none exist
        if Grade.query.count() == 0:
            students = Student.query.all()
            courses = Course.query.all()
            
            if students and courses:
                sample_grades = [
                    Grade(student_id=1, course_id=1, grade="A", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=1, course_id=2, grade="B+", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=2, course_id=1, grade="A-", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=2, course_id=3, grade="A", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=3, course_id=1, grade="B", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=3, course_id=4, grade="B+", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=4, course_id=2, grade="A", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=4, course_id=5, grade="A-", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=5, course_id=3, grade="B+", semester="Fall 2023", academic_year="2023-2024"),
                    Grade(student_id=6, course_id=1, grade="A", semester="Fall 2023", academic_year="2023-2024"),
                ]
                
                for grade in sample_grades:
                    db.session.add(grade)
                
                db.session.commit()
                print(f"Added {len(sample_grades)} sample grades")

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)