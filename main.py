import requests
 
url = 'YOUR WEBHOOK' # Your Discord Webhook Here
 
data = {
    'content' : 'YOUR MESSAGE', # Your Message Here
    'username' : 'YOUR USERNAME' # Your Username Here
}
 
requests.post(url, json = data)
