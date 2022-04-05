from flask import Flask,render_template,url_for


app=Flask(__name__)
app.config['SECRET_KEY'] = "cc7c83c25c81641609b40dbaf2038e12"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)