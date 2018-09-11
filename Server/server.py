from app import create_app
from config import Config


if __name__ == '__main__':
    app = create_app(Config)

    app.run(host='127.0.0.1', port=5000, debug=True)

