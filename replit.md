# JFAC Farmers - Flask Web Application

## Overview
This is a Flask web application for "JFAC Farmers - A group of farmers with a purpose". The project was originally an empty GitHub repository and has been set up as a functional web application in the Replit environment.

## Recent Changes (September 11, 2025)
- Created complete Flask web application from empty repository
- Set up project structure with templates, static files, and main application
- Configured Flask to run on port 5000 with host 0.0.0.0 for Replit proxy compatibility
- Added responsive design with farmer-themed green color scheme
- Configured deployment for Autoscale deployment target
- Set up workflow to run the application automatically

## Project Architecture
- **Framework**: Flask 3.0.0 with Werkzeug 3.0.1
- **Structure**: Standard Flask application layout
  - `main.py`: Main Flask application with routes
  - `templates/`: HTML templates (base.html, index.html, about.html)
  - `static/css/`: CSS styling (style.css)
  - `requirements.txt`: Python dependencies
- **Routes**:
  - `/`: Home page with mission and features
  - `/about`: About page with organization details
  - `/api/status`: JSON API endpoint for status checking
- **Deployment**: Configured for Replit Autoscale with command `python main.py`

## Technical Configuration
- **Host**: 0.0.0.0 (required for Replit proxy)
- **Port**: 5000 (Replit standard)
- **Debug Mode**: Controlled by FLASK_DEBUG environment variable (secure parsing)
- **Development**: Flask dev server via `python main.py`
- **Production**: Gunicorn WSGI server via deployment config
- **Workflow**: "Flask App" configured and running for development

## Current State
The application is fully functional and running successfully. All routes are working, the UI is responsive, and the application is ready for use and deployment.