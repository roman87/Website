from flask import render_template, request
from prog import app, db
from prog.models import AF, Comment
from prog.forms import CommentForm

@app.route('/')
def main():
    title = "Hi, Roman!"
    text = "Begin to work"
    return render_template('article.html', title=title, text=text)

@app.route('/first', methods=['GET', 'POST'])
def first():
    art = AF.query.get(1)
    title = art.title
    text = art.article
    form = CommentForm()
    if request.method == "POST":
        c = Comment(name=form.name.data, comment=form.comment.data, article=art)
        db.session.add(c)
        db.session.commit()
    return render_template('article.html', title=title, text=text)

@app.route('/second', methods=['GET', 'POST'])
def second():
    art = AF.query.get(2)
    title = art.title
    text = art.article
    return render_template('article.html', title=title, text=text)

@app.route('/third', methods=['GET', 'POST'])
def third():
    art = AF.query.get(3)
    title = art.title
    text = art.article
    return render_template('article.html', title=title, text=text)


