# app/__init__.py — Application Factory e registro dos Blueprints
from flask import Flask

def create_app():
    # Cria a instância do Flask
    app = Flask(__name__)
    # Chave de sessão (trocar em produção)
    app.config["SECRET_KEY"] = "dev"

    # ===== Registro dos Blueprints =====
    # Importa aqui para evitar import circular
    from app.blueprints.pred.routes import pred_bp
    from app.blueprints.graph.routes import graph_bp
    from app.blueprints.auth.routes import auth_bp
    from app.blueprints.user.routes import user_bp

    # Registra cada módulo com seu prefixo
    app.register_blueprint(pred_bp, url_prefix="/pred")
    app.register_blueprint(graph_bp, url_prefix="/graph")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")

    # Rota simples de home para facilitar testes
    @app.route("/")
    def home():
        # Renderiza uma base com links
        from flask import render_template
        return render_template("base.html")

    return app
