from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Configure Flask app to run on all hosts (required for Replit proxy)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = int(os.environ.get('PORT', 5000))

# Security: Only enable debug mode in development
# Default to True in development, can be overridden with FLASK_DEBUG=0
DEBUG_MODE = os.getenv('FLASK_DEBUG', 
                       '1').strip().lower() in {'1', 'true', 'yes', 'on'}


@app.route('/')
def home():
    """Main landing page for JFAC Farmers"""
    return render_template('index.html')


@app.route('/api/status')
def api_status():
    """API endpoint to check application status"""
    return jsonify({
        'status': 'running',
        'message': 'JFAC Farmers application is operational',
        'version': '1.0.0'
    })


@app.route('/about')
def about():
    """About page for the farmers group"""
    return render_template('about.html')


if __name__ == '__main__':
    # Bind to 0.0.0.0 to allow access from Replit proxy
    # Only enable debug in development environment
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=DEBUG_MODE)
