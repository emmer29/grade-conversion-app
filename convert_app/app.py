from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=['POST','GET'])

def index():
    user_name=''
    cgpa =''
    if request.method=='POST' \
        and 'maxgrade' in request.form \
        and 'mingrade' in request.form \
        and 'obtgrade' in request.form \
        and 'yourname' in request.form:
        maxcgp=float(request.form.get('maxgrade'))
        min_cgp=float(request.form.get('mingrade'))
        act_cgp=float(request.form.get("obtgrade"))
        user_name=str(request.form.get('yourname'))
        cgpa = round((((maxcgp - act_cgp)/(maxcgp-min_cgp))*3+1),2)
    

    return render_template("index.html", user_name=user_name, cgpa=cgpa)