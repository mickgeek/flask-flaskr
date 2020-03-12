from wtforms import Form, StringField, TextAreaField, validators


class NewPostForm(Form):
    title = StringField(u'Title', [validators.required(), validators.length(min=1, max=100)])
    text = TextAreaField(u'Text', [validators.required(), validators.length(min=5, max=500)])
