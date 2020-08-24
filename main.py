from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        return redirect('/index')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    return redirect('/home')


@app.route('/home')
def home():
    return render_template('main.html')


@app.route('/input')
def input():
    return render_template('diet_input.html')


@app.route('/files')
def files():
    return render_template('myfiles.html')


@app.route('/preview')
def preview():
    return render_template('preview.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug = True)
#    app.run(host='127.0.0.1', port=8080, debug=True)
