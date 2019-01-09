from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import form
from wtforms import TextField
from wtforms.validators import Required
app=Flask(__name__)
app.config['SECRET_KEY']='HARF TO GUESS STRING'
Bootstrap =Bootstrap(app)
class NameForm(Form):
    name=Nextfield("what is your name?",validators=[Required()])
@app.route('/',methods=['GET','POST'])
@app.route('/index',method=['GET','POST'])
def index():
    name=Name
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=""
        return render_template('index.html',form=form,name=name)
if __name__=='main__':
    app.run(debug=True)

















    
