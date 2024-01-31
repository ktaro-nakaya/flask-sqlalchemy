from flask import Flask
from alchemy import bp_alchemy

app = Flask(__name__, static_url_path='/')
app.register_blueprint(bp_alchemy)

if __name__ == '__main__':
    app.run()