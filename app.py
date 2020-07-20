from flask import Flask , render_template

app = Flask(__name__)
app.debug-True

@app.route('/')
def index():
    print("success")
    # return = "TEST"
    return render_template('about.html', hello = "GaryKim")

    @app.route('/about')
def about():
    print("success")
    # return = "TEST"
    return render_template('about.html', hello = "GaryKim")

     @app.route('/articles')
def articles():
    print("success")
    # return = "TEST"
    return render_template('articles.html', hello = "GaryKim")

if __name__=='__main__':
    # app.run(host='0.0.0.0', post='8080')
    app.run()