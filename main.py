import os
import json
import config
from binance.client import Client
from binance.enums import *
from flask import Flask, request, jsonify

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET, tld='us')


def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print(f"enviando a ordem... {order_type} - {side} {quantity} {symbol}")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        print("ocorreu uma exceção de erro - {}".format(e))
        return False

    return order

@app.route("/", methods=['GET'])
def index():
    return "<h1>Olá Mundo!</h1>"

@app.route("/webhook", methods=['GET'])
def deploy():

    data = json.loads(request.data)

    if data['senha'] != config.WEBHOOK_PASSFRASE:
        return {
            "code": "Erro",
            "message": "Senha incorreta, tente novamente!"
        }
    print(data['ticker'])
    print(data['bar'])

    side = data['strategy']['order_action'].upper()
    quantidade = data['strategy']['order+contracts']
    order_response = order(side, quantidade, "BTCBUSD")
    if order_response:
        return {
            "code": "Ok",
            "message": "Ordem executada"
        }
    else:
        print('Ocorreu uma falha com a ordem!')
        return {
            "code": "Erro",
            "message": "Falha na ordem"
        }

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

# @app.route("/webhook", methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         print(request.json)
#         return 'success', 200
#     else:
#         abort(400)
#
# if __name__  == '__main__':
#     app.run(debug=True)

if __name__  == '__main__':
    main()

