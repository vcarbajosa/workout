# -*- encoding: utf-8 -*-
# Este achivo tiene dos funciones principales
#   - Convierte el directorio en un modulo de pyton, según el estandar
#   - Registra en el pool las clases del modulo
#
# El Pool se puede ver como "una imagen sincronizada en memoria" de la base de datos.
# Tryton siguel el patrón "Active Record". Se encarga de la creación de las tablas y de la relación entre la
# representacion en memoria de la entidad y sus respectivas columnas en la base de datos. Asímismo se encarga
# de la sincronizacion de los datos cargados en memoria y su persistencia en la base de datos
# El Pool debe ser consciente de la existencia de las clases de entidad

from trytond.pool import Pool
from .workout import Exercise, Muscle



def register():
    Pool.register(
        Exercise,Muscle,
        module='workout', type_='model'
    )

