import requests

# ====== YOUR DETAILS ======
BOT_TOKEN = "8460172500:AAG9hHAaVi9CsAP0Vdje9dDA_LhyZ8XCHbw"
CHAT_ID = 880622327
# ==========================

def send_message(message):
    url = f"https://api.telegram.org/bot{8460172500:AAG9hHAaVi9CsAP0Vdje9dDA_LhyZ8XCHbw}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    print(response.text)

def check_jobs():
    url = "https://www.naukri.com/devops-engineer-jobs"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if "DevOps Engineer" in response.text:
        send_message("🚀 New DevOps Job Found!\nhttps://www.naukri.com/devops-engineer-jobs")
    else:
        print("No jobs found")

if __name__ == "__main__":
    check_jobs()
