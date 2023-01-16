from flask import Flask,render_template, request, redirect,session
app=Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def rootform():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] =request.form['name']
    session['age']= request.form['age']
    session['location']=request.form['location']
    session['belts']= request.form['belts']
    session['language']=request.form['language']
    session['comments']=request.form['comments']
    print(session)
    return redirect('/result') 

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/go_back')
def goback():
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)