import time
import multiprocessing
from rest.client import FtxClient


api_key = 'QhWqAoqGhoYEyk-SuM3KEEHaBIASQD5ZoPRN_rxR'
api_secret = 'K_yvxOFRsoLJ9UEGSyQl-xpV5hQEKMWQUu-hMT2j'
client = FtxClient(api_key=api_key, api_secret=api_secret)


book = client.get_orderbook(market='POLIS/USD', depth=100)


for i in reversed(book['asks']):
    print(i)
