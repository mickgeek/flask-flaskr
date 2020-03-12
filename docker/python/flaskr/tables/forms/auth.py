from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField(u'Username', [validators.required(), validators.Length(min=3, max=15)])
    password = PasswordField(u'Password', [validators.required(), validators.Length(min=5, max=30)])
