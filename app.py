import os
from flask import Flask
from cnpj import CnpjRequest
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__, static_url_path='')


@app.route("/api/cnpj/<cnpj>")  # @variavel.metodo('/caminho')
def get_data(cnpj):
    return CnpjRequest().get_data(cnpj)


if __name__ == '__main__':
    app.run(debug=True)
