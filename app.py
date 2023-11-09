from flask import Flask, redirect, render_template, request, url_for
import json
import db

app = Flask(__name__)

dbo = db.Database()


@app.route('/')
def index():
  return render_template('register.html')


@app.route('/perform_registration', methods=['GET', 'POST'])
def perform_registration():
  user_ka_email = request.form.get('emailaddress')
  user_ka_naam = request.form.get('username')
  user_ka_password = request.form.get('password')
  response = dbo.insert(user_ka_naam, user_ka_email, user_ka_password)

  if response:
    return render_template('login.html', username=user_ka_naam)
  else:
    return render_template('register.html', error='Username already exists')


@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/perform_login', methods = ['GET','POST'])
def perform_login():
  user_ka_email = request.form.get('email')
  user_ka_password = request.form.get('password')
  with open('users.json', 'r') as rf:
    users = json.load(rf)

  if user_ka_email in users:
    if users[user_ka_email][1] == user_ka_password:
      return 'logged in succesfully'
    else:
      return render_template('login.html', error='Incorrect password')
  else:
    return render_template('login.html', error='User does not exist. Kidly register first')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
