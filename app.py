from flask import Flask
from flask import jsonify
from LobbyFunctions.create_lobby import create_lobby

app = Flask(__name__)


# This method generates a unique URL for the players
# to connect to this URL with
@app.route('/create-lobby')
def create_new_lobby():
    new_url = create_lobby()
    response = jsonify({
        'url': new_url,
    }).status = 201

    return response


if __name__ == '__main__':
    app.run()
