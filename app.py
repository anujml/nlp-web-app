from flask import Flask, render_template, request
import db

app = Flask(__name__)

dbo = db.Database()


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/perform_registration', methods=['GET', 'POST'])
def perform_registration():
  user_ka_naam = request.form.get('username')
  user_ka_password = request.form.get('password')
  user_ka_confirmpassword = request.form.get('confirmpassword')
  response = dbo.insert(user_ka_naam, user_ka_password,
                        user_ka_confirmpassword)

  if response:
    return "Registration Successful"
  else:
    return "Email Already Exits"


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
