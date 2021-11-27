import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data = { 'Corretora' : 'exchange',
         'Preço' : 'BTC',
         'Operação' : 'Compra' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})