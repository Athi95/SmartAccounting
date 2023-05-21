from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)


app.secret_key = 'anu'
@app.route('/')
def home():
    return render_template('home.html')
#Admin login

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = 'true'
            return redirect(url_for('admin_home'))
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('admin_login.html', error=error)
    else:
        return render_template('admin_login.html')

#Admin home

@app.route('/admin/home', methods=['GET', 'POST'])
def admin_home():
    if 'logged_in' in session and session['logged_in']:
        return render_template('admin_home.html')
    else:
        return redirect('/admin/login')


