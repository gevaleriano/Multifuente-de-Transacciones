import os
from flask import Flask
from views.routes import views_bp

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.register_blueprint(views_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
