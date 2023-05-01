import os
import smtplib
import uuid as uuid
from flask import current_app
from email.mime.text import MIMEText
from werkzeug.utils import secure_filename


def send_email(subject, sender, recipients, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, 'jarjbcedbedjhmzs')
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()

        print("Email sent.")
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
    

def save_image(image_file):
    image_filename = secure_filename(image_file.filename)
    image_filename_UUID = str(uuid.uuid1()) + '_' + image_filename
    image_path = os.path.join(current_app._get_current_object().root_path, current_app.config.get('PROFILE_PIC_FOLDER'), image_filename_UUID)
    image_file.save(image_path)
    return image_filename_UUID


def delete_image(image_filename):
    image_path = os.path.join(current_app._get_current_object().root_path, current_app.config.get('PROFILE_PIC_FOLDER'), image_filename)
    if (os.path.exists(image_path)):
        os.remove(image_path)


def generate_password(length):
    random_uuid = uuid.uuid4()
    password = str(random_uuid).replace('-', '')[:length]
    print(password)
    return password