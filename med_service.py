import time
import json
import os
from datetime import datetime
from twilio.rest import Client

# Twilio Credentials (Twilio Dashboard se copy karein)
ACCOUNT_SID ='ACbcd5184737bfbcaaeae2e1f4401fded3'
AUTH_TOKEN ='3774b8dabd20bb8711794740672b1364'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886' # Twilio ka sandbox number

def send_whatsapp_alert(med_name, phone_number):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=f"🚨 MED-ALERT: Time to take your {med_name}!",
        from_=TWILIO_WHATSAPP_NUMBER,
        to=f"whatsapp:{phone_number}"
    )
    print(f"✅ Alert sent to {phone_number}")

def run_service():
    print("🚀 Med-Alert Service is running...")
    while True:
        now = datetime.now().strftime("%H:%M")
        
        try:
            # Website se save kiya hua data read karna
            with open("med_data.json", "r") as f: meds = json.load(f)
            with open("user_data.json", "r") as f: user = json.load(f)
            
            for m in meds:
                if m['time'] == now:
                    # 1. Laptop par alarm bajega
                    os.system("osascript -e 'beep 3'") 
                    # 2. WhatsApp par notification jayega
                    send_whatsapp_alert(m['name'], user['phone'])
                    time.sleep(60) # Ek minute ka break taaki bar bar na baje
        except:
            pass
        
        time.sleep(10)

if __name__ == "__main__":
    run_service()