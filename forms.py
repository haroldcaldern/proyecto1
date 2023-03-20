from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from flask_wtf.file import FileAllowed
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class FormVideoGame(FlaskForm):
    title = StringField("Title",validators=[DataRequired("Tienen que agregar un titulo")])
    description = StringField("Description",validators=[DataRequired("Tienen que agregar uns descripcion del juego")])
    photo = FileField('Selecciona imagen:', validators=[FileRequired('Es necesario selecionar un archivo de imagén'),FileAllowed(['jpg','png'],'Archivos válidos jpg o png únicamente')])
    submit = SubmitField('Submit')