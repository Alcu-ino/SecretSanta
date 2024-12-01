import smtplib
import random
from email.mime.text import MIMEText


SMTP_SERVER = 'smtp.service.com'
SMTP_PORT = 587  

EMAIL_ADDRESS = '<email>'
EMAIL_PASSWORD = '<password>' 

emails = ['ex1@mail.com','ex2@mail.com']

def generate_random_pairs(emails):
    names = [email.split("@")[0] for email in emails]
    shuffled_names = names[:]
    while True:
        random.shuffle(shuffled_names)
        if all(shuffled_names[i] != names[i] for i in range(len(names))):
            break
    return dict(zip(emails, shuffled_names))

def send_email(to_email, from_email, from_password, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(from_email, from_password)
            
            msg = MIMEText(message)
            msg['Subject'] = 'Il tuo amico segreto'
            msg['From'] = from_email
            msg['To'] = to_email
            
            server.sendmail(from_email, to_email, msg.as_string())
            print(f"Email inviata a {to_email}")
    except Exception as e:
        print(f"Errore durante l'invio dell'email a {to_email}: {e}")

def main():
    pairs = generate_random_pairs(emails)
    for email, assigned_name in pairs.items():
        message = f"Ciao! Il tuo amico segreto è: {assigned_name}."
        send_email(email, EMAIL_ADDRESS, EMAIL_PASSWORD, message)

if __name__ == "__main__":
    main()