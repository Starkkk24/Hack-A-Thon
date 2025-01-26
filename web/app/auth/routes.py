from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
import requests
import json

app1_bp = Blueprint('app1', __name__, template_folder='templates', static_folder="static")
url = "http://127.0.0.1:5500/auth/web"
@app1_bp.route('/')
def index():
    return "dcfvgbhj"


@app1_bp.route('/reg', methods=["GET",  "POST"])
def reg():
    if 'user' in session:
        return redirect(url_for("app2.index"))
    
    t = ["", ""]
    if request.method == 'POST':
        # Collect form data
        
        url1 = url + "/reg"
        
        user = request.form.get('u')       # Field name: u
        name = request.form.get('n')     # Field name: n
        dept = request.form.get('o')  # Field name: o
        code = request.form.get('c')     # Field name: c
        c_code = request.form.get('cc')  # Field name: cc
        t = [user, name]
        if code != c_code:
            return render_template("reg.html", t1=t, error="password mismatch")
        else: 
            data = {
                "user": user,
                "name": name,
                "dept": dept,
                "code": code,
                "under": ""
            }   
            print(data)
            response = requests.post(url1, data=data)
            ma = response.text
            if ma[0] == False:
                return render_template("reg.html", t1=t, error=" unknown error")
            else:
                res = json.loads(ma)
                res = res["message"]
                ma = res
                print(res)
                if ma[1].startswith("M"):
                    print(ma)
                    session['user'] = [ma[1], ma[2], ma[3], "M"]
                    session.permanent = True
                    return redirect(url_for("app2.index"))
                elif ma[1].startswith("C"):
                    session['user'] = [ma[1], ma[2], ma[3], "C"]
                    session.permanent = True
                    return "to customer page"
                elif ma[1].startswith("S"):
                    session['user'] = [ma[0], ma[1], ma[2], "S", ma[5]]
                    session.permanent = True
                    return redirect(url_for("app3.index"))
                
                else:
                    return "nothing"
            # session['user'] = request.form['username']
            # session.permanent = True 
            
            """
            @app.route('/')
            def home():
                if 'user' in session:
                    return f"Hello, {session['user']}! Your session is permanent. <br> <a href='/logout'>Logout</a>"
                return "You are not logged in. <a href='/login'>Login</a>"

            @app.route('/login', methods=['GET', 'POST'])
            def login():
                if request.method == 'POST':
                    session.permanent = True  # Make the session permanent
                    session['user'] = request.form['username']
                    return redirect(url_for('home'))
                        return render_template("log.html")
        """            
                    
    return render_template("reg.html", t1=t)

@app1_bp.route('/log', methods=["GET", "POST"])
def log():
    t = []
    url1 = url + "/log"
    if 'user' in session:
        return redirect(url_for("app2.index"))
    if request.method == 'POST':
        user = request.form.get('n')       # Field name: u
        code = request.form.get('c')
        params = {
            "userid": user,
            "code": code
        }
        response = requests.get(url1, params=params)
        ma = response.text
        print(ma)
        res = json.loads(ma)
        res = res["message"]
        ma = res
        print(ma)
        if not ma[0]:
            return render_template("log.html", t1=t, error=" unknown error")
        else:
            
            print(ma)
            lo = ma[1][0][0]
            ma = ma[1][0]
            if lo.startswith("M"):
                print(ma)
                session['user'] = [ma[0], ma[1], ma[2], "M"]
                session.permanent = True
                return redirect(url_for("app2.index"))
            elif lo.startswith("C"):
                session['user'] = [ma[0], ma[1], ma[2], "C"]
                session.permanent = True
                return "to customer page"
            elif lo.startswith("S"):
                session['user'] = [ma[0], ma[1], ma[2], "S", ma[5]]
                session.permanent = True
                return redirect(url_for("app3.index"))
            else:
                return "nothing"
            
    return render_template("log.html")


@app1_bp.route('/logout')
def logout():
    if 'user' in session:    
        session.pop('user', None)
        return redirect(url_for('app1.reg'))
    else:
        return redirect(url_for('app1.reg'))



"""
    
    if ma[1][0].startswith("M"):
                print(ma)
                session['user'] = [ma[1], ma[2], ma[3], "M"]
                session.permanent = True
                return redirect(url_for("app2.index"))
            elif ma[1][0].startswith("C"):
                session['user'] = [ma[1], ma[2], ma[3], "C"]
                session.permanent = True
                return "to customer page"
            elif ma[1][0].startswith("S"):
                session['user'] = [ma[1], ma[2], ma[3], "S"]
                session.permanent = True
                return "to the site page"
            else:
                return "nothing"""