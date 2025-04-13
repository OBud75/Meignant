from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
	return 'Welcome to flask application'

@app.route('/test')
def test():
	return 'This is test rute of myapp flask application'

if __name__ == '__main__':
	app.run('0.0.0.0', port=5000)