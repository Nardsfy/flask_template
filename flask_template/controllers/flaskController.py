from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from flask_template import app
from flask_template.dao.flaskDao import getUser

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():      
    return render_template('flaskTemplate.html', title=app.config['MYPROJECT_TITLE'])