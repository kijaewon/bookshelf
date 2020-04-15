from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('index.html')



if __name__=='__main__' :
    app.run('localhost', 5000, debug=True)

    