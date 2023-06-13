
from client.derbit_client import make_request


async def test_price_is_float():
    url = 'https://test.deribit.com/api/v2/public/get_index_price?index_name=btc_usd'
    result = await make_request(url)
    assert isinstance(result, float)
