import requests

response1 = requests.get('https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5')
response2 = requests.get('https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5')
response3 = requests.get('https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5')
print("Response1:",response1.headers.get('Date'))
print("Response2:",response2.headers.get('Date'))
print("Response3:",response3.headers.get('Date'))