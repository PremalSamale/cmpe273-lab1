import asyncio
import requests

#Reference:http://skipperkongen.dk/2016/09/09/easy-parallel-http-requests-with-python-and-asyncio/

url = 'https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5'
async def main():
    loop = asyncio.get_event_loop()
    results = []
    for index in range(0,3):
        results.append(loop.run_in_executor(None, requests.get, url))
    response = []
    for index in range(0,3):
        response.append(await results[index])
    print("Response1:",response[0].headers.get('Date'))
    print("Response2:",response[1].headers.get('Date'))
    print("Response3:",response[2].headers.get('Date'))
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
