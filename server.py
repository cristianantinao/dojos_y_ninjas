from app_flask import app
from app_flask.controladores import controlador_dojos, controlador_ninja

if __name__ == '__main__':
    app.run(debug=True)