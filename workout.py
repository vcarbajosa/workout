# -*- encoding: utf-8 -*-
# Este archivo respresenta la base del modulo.
# Contiene la definicion de las entidades. Aqui definiremos nuestros modelos que se mapearan a la base de datos

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

# El diccionario __all__ debe contener todas nuestras clases

__all__ = ['Exercise','Muscle']

class Exercise(ModelSQL,ModelView):
    "Exercises"
    # __name__ es un atributo especial que define el nombre del objeto en tryton
    # por convencion lo llamaremos nombredemodulo.nombredeclase
    # creara en la base de datos una tabla que se llamara nombredemodulo_nombredeclase
    __name__ = 'workout.exercise'

    # Campos:
    # La definicion de los campos se hará como atributos de clase de tipo trytond.model.fields

    # el tipo fields.Char se alamacenará en la base de datos como un varchar
    name = fields.Char('Exercise')
    # el tipo fields.Text se alamacenará en la base de datos como un Text
    description = fields.Text('Description')

class Muscle(ModelSQL,ModelView):
    "Muscle"
    __name__='workout.muscle'
    name = fields.Char('Muscles')
