import asyncio
import aiohttp

from client.db import db


async def make_request(url, retries=3):
    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as res:
                    response = await res.json()
                    return response['result']['index_price']

        except aiohttp.ClientError as e:
            print(f"An error occurred during the request: {e}")
        except KeyError:
            print("Invalid response format.")

        await asyncio.sleep(1)

    # All retries failed
    raise Exception(f"Failed to retrieve index price after {retries} attempts.")


async def main():
    url_btc = 'https://test.deribit.com/api/v2/public/get_index_price?index_name=btc_usd'
    url_eth = 'https://test.deribit.com/api/v2/public/get_index_price?index_name=eth_usd'

    tasks = []
    async with aiohttp.ClientSession() as session:
        tasks.append(asyncio.create_task(make_request(url_btc)))
        tasks.append(asyncio.create_task(make_request(url_eth)))

        results = await asyncio.gather(*tasks)

        # recording to db
        db.add_rows('BTC', results[0])
        db.add_rows('ETH', results[1])

        print(f"BTC price: {results[0]}")
        print(f"ETH price: {results[1]}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

