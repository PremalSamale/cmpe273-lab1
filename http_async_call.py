
import asyncio
import requests

#Reference:http://skipperkongen.dk/2016/09/09/easy-parallel-http-requests-with-python-and-asyncio/

async def main():
    loop = asyncio.get_event_loop()
    result1 = loop.run_in_executor(None, requests.get, 'https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5')
    result2 = loop.run_in_executor(None, requests.get, 'https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5')
    result3 = loop.run_in_executor(None, requests.get, 'https://webhook.site/d56af0d6-4354-4f3c-9e7d-bd3f87364bc5')
    response1 = await result1
    response2 = await result2
    response3 = await result3
    print("Response1:",response1.headers.get('Date'))
    print("Response2:",response2.headers.get('Date'))
    print("Response3:",response3.headers.get('Date'))
loop = asyncio.get_event_loop()
loop.run_until_complete(main())