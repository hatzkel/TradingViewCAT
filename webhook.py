from actions import send_order, parse_webhook
from auth import get_token
from flask import Flask, request, abort

# Create Flask object called app.
app = Flask(__name__)

# Create root to easily let us know its on/working
@app.route('/')
def root()
    return 'online'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Parse the string data from tradingview into a python dict
        data = parse_webhook(request.get_data(as_text=True))
        # Check that the key is correct
        if get_token() == data['key']
            print(' [Alert Received'] ')
            print ('POST Received:', data)
            send_order(data)
            return '', 200
        else:
        abort(403)
    else:
        abort(400)

if __name__ == '__main__'
    app.run()