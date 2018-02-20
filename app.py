from flask import Flask, jsonify, abort
app = Flask(__name__)
@app.route('/')
def index():
	return "welcome to adaptyou analyti server API"
@app.route('/api/test')
def check():
    return jsonify({'active': 'true'})
if __name__ == "__main__":
	app.run()
