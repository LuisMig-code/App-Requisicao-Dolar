from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

dados_alta = None
dados_baixa = None
dados_var = None
dados_timestamp = None
dados_create_date = None
dados_cotacao = None


def realizaReqCambio():
    # Faz uma requisição para a API
    response = requests.get(f'https://economia.awesomeapi.com.br/last/USD')
    if response.status_code == 200:
        dados = response.json()
        dados = dados['USDBRL']

        dados_alta = dados['high']
        dados_baixa = dados['low']
        dados_var = dados['varBid']
        dados_cotacao = dados['bid']
        dados_timestamp = dados['timestamp']
        dados_create_date = dados['create_date']

        return (
            dados_alta,
            dados_baixa,
            dados_var,
            dados_timestamp,
            dados_create_date,
            dados_cotacao,
        )

    else:
        print('Erro ao fazer a requisição:', response.status_code)


(
    dados_alta,
    dados_baixa,
    dados_var,
    dados_timestamp,
    dados_create_date,
    dados_cotacao,
) = realizaReqCambio()


@app.route('/')
def index():
    return render_template(
        'index.html',
        alta=dados_alta,
        baixa=dados_baixa,
        cotacao=dados_cotacao,
        var=dados_var,
        timestamp=dados_timestamp,
        created_date=dados_create_date,
    )


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
