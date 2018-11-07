from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TextForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    comment = TextAreaField('Article', validators=[DataRequired()])
    submit = SubmitField('Submit')
