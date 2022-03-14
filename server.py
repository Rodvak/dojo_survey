from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'appleapple'


@app.route('/')
def index():
    return render_template('index.html')

# 
@app.route('/result', methods = ['post'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])


@app.route('/goback')
def go_back():
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)