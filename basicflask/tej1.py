from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
   dic={"tejal":100}
   print(dic)
    return render_template('temp2.html',index=dic)
if __name__=='__main__':
    app.run(debug=True)
