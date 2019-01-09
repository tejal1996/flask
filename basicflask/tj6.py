from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    name='teju'
    sname=['maths','java']
    v=[70,80]
    return render_template('tm.html',name=name,sname=sname,v=v)
if __name__=='__main__':
    app.run(debug=True)
