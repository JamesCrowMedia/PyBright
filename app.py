from flask import Flask, render_template
from rfoutlet import codesend


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle/<code>')
def toggle():
	codesend("4543795")
	return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
