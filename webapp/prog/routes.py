from flask import render_template, request, redirect, url_for
from prog import app, db
from prog.models import AF, Comment
from prog.forms import CommentForm, TextForm

@app.context_processor
def pass_art():
    articles = AF.query.all()
    return dict(articles=articles)

@app.route('/', methods=['GET', 'POST'])
def main():
    title = "HI, ROMAN!"
    text = "CREATE AN ARTICLE HERE!"
    form = TextForm()
    if request.method == "POST":
        a = AF(title=form.name.data, article=form.comment.data)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('article.html', title=title, text=text, form=form)

@app.route('/<n>', methods=['GET', 'POST'])
def article(n):
    art = AF.query.get(int(n))
    title = art.title
    text = art.article
    com = art.comments.all()
    form = CommentForm()
    if request.method == "POST":
        c = Comment(name=form.name.data, comment=form.comment.data, article=art)
        db.session.add(c)
        db.session.commit()
        return redirect('/{}'.format(int(n)))
    return render_template('article.html', title=title, text=text, form=form, com=com)

