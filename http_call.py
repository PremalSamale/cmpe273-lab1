import requests

url = 'https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5'
response_list = []
for index in range(0,3):
    response_list.append(requests.get(url))

print('Response1:', response_list[0].headers.get('Date'))
print('Response2:', response_list[1].headers.get('Date'))
print('Response3:', response_list[2].headers.get('Date'))
