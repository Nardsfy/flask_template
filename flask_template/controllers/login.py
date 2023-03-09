from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from flask_template import app, login_manager
from flask_template.models.user import User
from flask_template.dao.loginDao import getUser, getUserById
from flask_template.others.format import responseJSON

@login_manager.user_loader
def load_user(id):              
    v_get_user_by_id = getUserById(id)    
    if (v_get_user_by_id['status'] == 'F'): return v_get_user_by_id
    if (not v_get_user_by_id['result']): return None
    
    return User(v_get_user_by_id['result'][0]['u_id'], v_get_user_by_id['result'][0]['u_username'], v_get_user_by_id['result'][0]['u_role'])

@app.route('/login', methods=['GET', 'POST'])
def login():         
    if (current_user.is_authenticated):
        return redirect(url_for('dashboard'))

    if (request.method == 'GET'):
        return render_template('login.html', title=app.config['MYPROJECT_TITLE'])
    else:        
        v_username = request.form.get('username')
        v_password = request.form.get('password')    

        # Check from database
        v_get_user = getUser(v_username, v_password)        
        if (v_get_user['status'] == 'F'): return v_get_user
        if (not v_get_user['result']): return responseJSON(400, 'F', 'Username and Password not match.', [])
                
        user = User(v_get_user['result'][0]['u_id'], v_get_user['result'][0]['u_username'], v_get_user['result'][0]['u_role'])                                
        login_user(user)
        return redirect(url_for('dashboard'))            
    
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return render_template('login.html', title=app.config['MYPROJECT_TITLE'])