from flask import Flask, request, render_template, send_from_directory
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'smart.dm.services@gmail.com'
app.config['MAIL_PASSWORD'] = 'iwqpgbcscftrbjua'
mail = Mail(app)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(name, email, phone, message)
    msg = Message(subject='New Contact Form Submission', sender=app.config['MAIL_USERNAME'], recipients=['smart.dm.services@gmail.com'], body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
    mail.send(msg)
    return "Thank you for contacting us!"
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('', 'sitemap.xml')
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('static', 'robots.txt')
if __name__ == '__main__': app.run(debug=True)