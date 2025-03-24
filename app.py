from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# oshxona route
@app.route('/category/1/')
def oshxona():
    return render_template('oshxona.html')

# shkaf va gerderob route
@app.route('/category/2/')
def shkaf():
    return render_template('shkaf.html')

# bolalar uchun route
@app.route('/category/3/')
def bolalar():
    return render_template('bolalar.html')

# yumshoq route
@app.route('/category/4/')
def yumshoq():
    return render_template('yumshoq.html')

# yotoqxona route
@app.route('/category/5/')
def yotoqxona():
    return render_template('yotoqxona.html')

# eshiklar route
@app.route('/category/6/')
def eshiklar():
    return render_template('eshiklar.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)