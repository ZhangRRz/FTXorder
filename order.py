from rest.client import FtxClient
import time
api_key = 'QhWqAoqGhoYEyk-SuM3KEEHaBIASQD5ZoPRN_rxR'
api_secret = 'K_yvxOFRsoLJ9UEGSyQl-xpV5hQEKMWQUu-hMT2j'
client = FtxClient(api_key=api_key, api_secret=api_secret)


while(1):
    market = 'BTC/USD'
    side = 'buy'
    price = 1.00
    size = 0.0001
    type0 = 'limit'
    ioc_flag = True  # 不成交則立即撤單

    order_data = client.place_order(market=market, side=side,
                                    price=price, size=size, type=type0, ioc=ioc_flag)

    print(time.time())
