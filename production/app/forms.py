from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField
from wtforms.validators import Required


class MainForm(FlaskForm):
    number_of_cities = IntegerField("Numero de ciudades", validators=[Required()])
    number_of_colors = IntegerField("Numero de colores", validators=[Required()])
    number_of_relations = IntegerField('Numero de relaciones', validators=[Required()])
    relations = TextAreaField("Relaciones; Coloque las relaciones con el siguiente formato: '1-2, 3-4, 4-5'")
    submit = SubmitField('enviar')
