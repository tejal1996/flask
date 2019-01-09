from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    name='teju'
    return render_template('tm.html',name=name)
if __name__=='__main__':
    app.run(debug=True)
