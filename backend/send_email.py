import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_email(email, asset_id, name):
    app_pwd = os.environ.get("app_pwd")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("msganawberihun10@gmail.com", app_pwd)
    message = f"Hey {name},\n Your certificate is ready you can get it using this id {asset_id}"
    s.sendmail("msganawberihun10@gmail.com", email, message)
    s.quit()
