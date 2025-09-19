# 🚀 Deployment Guide

## ⚠️ Important: Cloudflare Pages Limitation

**Cloudflare Pages only supports static sites** (HTML, CSS, JS). Your Student Management System is a **Flask application** that requires a Python server to run.

## 🎯 Recommended Deployment Platforms

### 1. **Render (Recommended - Free Tier Available)**

**Steps:**
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Click "New +" → "Web Service"
4. Connect your GitHub repository: `poplaone/student-management-system`
5. Configure:
   - **Name**: `student-management-system`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python src/app.py`
   - **Instance Type**: `Free`

**Environment Variables:**
```
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
```

### 2. **Railway (Easy One-Click Deploy)**

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect it's a Python app
6. Deploy automatically!

**Environment Variables:**
```
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
```

### 3. **Heroku (Popular Choice)**

**Steps:**
1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create student-management-system`
4. Set environment variables:
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=your-super-secret-key-here
   ```
5. Deploy: `git push heroku main`

### 4. **PythonAnywhere (Python-Specific)**

**Steps:**
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code via Git or file manager
3. Create a web app with Flask
4. Configure WSGI file to point to your app
5. Set environment variables in web app settings

## 🔧 Pre-Deployment Checklist

- [x] Updated `app.py` for production
- [x] Created `requirements.txt`
- [x] Added `Procfile` for Heroku
- [x] Added `render.yaml` for Render
- [x] Added `railway.json` for Railway
- [x] Environment variables configured
- [x] Database initialization included

## 🌐 If You Must Use Cloudflare Pages (Static Only)

**Note**: This will only show the frontend without Flask functionality.

### Cloudflare Pages Settings:
```
Framework preset: None
Build command: echo "Static site"
Build output directory: /
Root directory: /
Environment variables: (none needed)
```

**Limitations:**
- No database functionality
- No user authentication
- No form submissions
- Only static HTML/CSS/JS

## 🔐 Security Notes

1. **Change default admin password** after first login
2. **Use strong SECRET_KEY** in production
3. **Enable HTTPS** (most platforms do this automatically)
4. **Regular backups** of your database

## 📊 Post-Deployment

After successful deployment:

1. **Test all functionality**:
   - Login with admin/admin123
   - Add students and courses
   - Check dashboard statistics

2. **Change default credentials**:
   - Login as admin
   - Change password immediately

3. **Monitor performance**:
   - Check application logs
   - Monitor response times
   - Set up error tracking

## 🆘 Troubleshooting

### Common Issues:

**1. Module not found errors**
- Ensure all dependencies are in `requirements.txt`
- Check Python version compatibility

**2. Database errors**
- Database will be created automatically on first run
- Check file permissions for SQLite

**3. Port binding errors**
- App is configured to use PORT environment variable
- Most platforms set this automatically

**4. Static files not loading**
- Ensure static files are in `src/static/` directory
- Check file paths in templates

## 📞 Support

If you encounter issues:
1. Check platform-specific documentation
2. Review application logs
3. Test locally first
4. Check environment variables

## 🎉 Success!

Once deployed, your Student Management System will be accessible via:
- **Render**: `https://student-management-system.onrender.com`
- **Railway**: `https://student-management-system.up.railway.app`
- **Heroku**: `https://student-management-system.herokuapp.com`

**Default Login**: `admin` / `admin123`

---

**Remember**: Change the default password immediately after deployment!