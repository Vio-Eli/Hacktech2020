#File: ./app.py
from flask import Flask, render_template, request, jsonify, make_response, json
from pusher import pusher

app = Flask(__name__)

import pusher

pusher_client = pusher.Pusher(
  app_id='960032',
  key='bc5c21a8a4fc2990fe4a',
  secret='8ee5b28ecc6d94779c91',
  cluster='us3',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})

name = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    global name
    name = request.args.get('username')
    return render_template('play.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/end')
def end():
    return render_template('end.html')

@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
    auth = pusher.authenticate(
    channel=request.form['channel_name'],
    socket_id=request.form['socket_id'],
    custom_data={
    u'user_id': name,
    u'user_info': {
    u'role': u'player'
    }
    }
    )
    return json.dumps(auth)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)

        name = ''
