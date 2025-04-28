import smtplib
from flask import Flask, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CORS(app, resourses = {
    r"/sumbit-form":{
        "origins":["https://sevrin-de.github.io/anket/"],
        "methods":["POST"],
        "allow_headers":["Content-Type"]
    }
})

def send_email(form_data):
    sender = "fodan608@gmail.com"
    password = "pwyf lxsy zdyg yham"

    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = sender
    message['Subject'] = "Новые данные из формы"
    
    email_body = f"""
    <h1>Новые данные из формы:</h1>
    <p><strong>Имя:</strong> {form_data.get('name', 'Не указано')}</p>
    <p><strong>Кличка питомца:</strong> {form_data.get('nameEnimail', 'Не указано')}</p>
    <p><strong>Возраст:</strong> {form_data.get('number', 'Не указано')}</p>
    <p><strong>Email:</strong> {form_data.get('email', 'Не указано')}</p>
    <p><strong>Телефон:</strong> {form_data.get('phone', 'Не указано')}</p>
    <p><strong>Порода:</strong> {form_data.get('poroda', 'Не указано')}</p>
    <p><strong>Пол:</strong> {form_data.get('gender', 'Не указано')}</p>
    """
    
    message.attach(MIMEText(email_body, 'html'))

    print("Отправляемый JSON:", jsonify({"success": True, "message": "Данные отправлены!"}).data)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, sender, message.as_string())
        server.quit()
        return True
    except Exception as ex:
        print(f"Ошибка при отправке email: {ex}")
        return False

@app.route('/submit-form', methods=['POST'])
def handle_form():
    try:
        form_data = request.form.to_dict()
        if send_email(form_data):
            return jsonify({"success": True, "message": "Данные отправлены!"})
        else:
            return jsonify({"success": False, "message": "Ошибка отправки"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
