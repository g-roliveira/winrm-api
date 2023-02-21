from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import getpass
import winrm

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('host', required=True, help="IP do servidor remoto")
parser.add_argument('user', required=True, help="Nome do usuário")
parser.add_argument('password', required=True, help="Senha do usuário")
parser.add_argument('transport', required=False, default='ntlm', help="Tipo de transporte: ntlm, kerberos ou credssp")
parser.add_argument('command', required=True, help="Comando no Windows")

class Winrm(Resource):
    def post(self):
        args = parser.parse_args()
        winrm_host = args['host']
        winrm_user = args['user']
        winrm_pass = args['password']
        transport_mode = args['transport']
        command = args['command']

        if transport_mode == 'kerberos':
            # Cria um contexto Pywinrm com autenticação Kerberos
            session = winrm.Session(winrm_host, auth=('kerberos', (winrm_user, winrm_pass)))
        else:
            # Cria uma sessão do WinRM com autenticação NTLM ou CredSSP
            session = winrm.Session(winrm_host, auth=(winrm_user, winrm_pass), transport=(transport_mode), server_cert_validation='ignore')

        # Executa o comando 'ipconfig /all'
        result = session.run_cmd(command)

        # Retorna o resultado como um objeto JSON
        return jsonify({
            'status_code': result.status_code,
            'output': result.std_out.decode()
        })

# Adiciona o recurso à API
api.add_resource(Winrm, '/winrm')

if __name__ == '__main__':
    app.run(debug=True)
