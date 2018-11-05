from flask import render_template
from prog import app
from prog.models import AF

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
