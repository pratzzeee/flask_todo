from flask import render_template, redirect, request
from flasktodo import app, db
from flasktodo.models import Todo


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        user_1 = Todo(title = title, desc = desc)
        db.session.add(user_1)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('home.html', allTodo=allTodo)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        user_1 = Todo.query.filter_by(sno=sno).first()
        user_1.title = title
        user_1.desc = desc
        db.session.add(user_1)
        db.session.commit()
        return redirect('/')

    user_1 = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', user_1=user_1)

@app.route('/delete/<int:sno>')
def delete(sno):
    user_1 = Todo.query.filter_by(sno=sno).first()
    db.session.delete(user_1)
    db.session.commit()
    return redirect('/')
