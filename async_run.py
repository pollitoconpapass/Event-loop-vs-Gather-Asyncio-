import asyncio
import aiohttp
import os
import time

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT']
results = []

start = time.time()
async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print("Working on symbol {}".format(symbol))
            response = await session.get(url.format(symbol, api_key), ssl = False)
            results.append(await response.json())

loop = asyncio.get_event_loop()#-> event loop
loop.run_until_complete(get_symbols()) #-> get_symbols function is running inside of a loop
loop.close()

asyncio.run(get_symbols())


end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
#print("YOU DID IT!")
