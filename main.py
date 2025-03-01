import requests
 
url = 'https://discord.com/api/webhooks/1345524399171965059/IyK_di0ECo0wWhYiAYlmMY4As3Gmsm_K6Z8JG-IYje7DplqwTqHlY8LMF3s5nCh2X-Lm' # Your Discord Webhook Here
 
data = {
    'content' : 'YOUR MESSAGE', # Your Message Here
    'username' : 'YOUR USERNAME' # Your Username Here
}
 
requests.post(url, json = data)
