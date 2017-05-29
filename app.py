from flask import *
from rfoutlet import codesend


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle/<code>')
def toggle(code):
	codesend(code)
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
