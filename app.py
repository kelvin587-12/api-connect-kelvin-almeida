from flask import Flask, jsonify, request
from routes.connect_routes import connect_bp

# Criação da aplicação
app = Flask(__name__)

# Registro das rotas de usuários
app.register_blueprint(connect_bp)


# Middleware global para interpretar JSON
@app.before_request
def parse_json_body():
    if request.method in ("POST", "PUT", "PATCH") and request.is_json:
        request.get_json()


# Rota para testar o servidor
@app.get("/")
def health_check():
    return jsonify(
        {
            "status": "success",
            "message": "API Connect está funcionando."
        }
    ), 200


# Inicialização do servidor
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


    
    