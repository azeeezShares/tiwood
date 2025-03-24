from flask import Flask, flash, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8zddfxec]/'

# PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://azeeez:1122@localhost/tiwood_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    furniture_type = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"<Request {self.name} - {self.furniture_type}>"
    


@app.route('/', methods=['get', 'post'])
def home():
    
    if request.method.lower() == 'post':
        furniture_options = {
            "1": "Oshxona mebellari",
            "2": "Shkaf va garderob",
            "3": "Bolalar mebeli",
            "4": "Yumshoq mebellar",
            "5": "Yotoqxona mebellari",
            "6": "Eshiklar"
        }
        if request.form.get("name") and request.form.get("phone") and request.form.get("furniture_type") and request.form.get("furniture_type") in furniture_options.keys():
            new_order = Request(name=request.form.get("name"), phone=request.form.get("phone"), furniture_type=furniture_options[request.form.get("furniture_type")])
            db.session.add(new_order)
            db.session.commit()
            return render_template("success.html")
    
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

@app.route("/johihubdh", methods=["GET", "POST"])
def admin_data():
    if request.method.lower() == 'post':
        if request.form.get("username") == "secretController" and request.form.get("password") == "mx+1998":
            session["logged"] = True
            return render_template("admin_data.html", context={"data":Request.query.all()})
        else:
            flash("Invalid username or password!", "error")
            return render_template("admin_login.html")
            
    
    if not session.get("logged") == True: return render_template("admin_login.html")
    else: return render_template("admin_data.html", context={"data":Request.query.all()})

@app.route("/logout-jdjd", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)