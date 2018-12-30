from flask import Flask, session, request, render_template

app = Flask(__name__)
app.secret_key = 'abhinav'

@app.route('/')
def index():
	return render_template('index.html')



if __name__ == '__main__':
	app.run("0.0.0.0",port=2609,threaded = True)

