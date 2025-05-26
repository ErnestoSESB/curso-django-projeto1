# from inspect import signature
#tentar fazer com o signature

from random import randint
import random
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))
images = [
    '/static/recipes/images/hamburger.webp',
    '/static/recipes/images/salgado.jpg',
    '/static/recipes/images/pizza.jpg',
    '/static/recipes/images/sobremesa.jpg',
    '/static/recipes/images/sorvete.jpg',
    '/static/recipes/images/torta.jpg',
    '/static/recipes/images/jantar.jpg',
    '/static/recipes/images/doces.jpg',
]
categories = [
    'café da manhã',
    'almoço',
    'janta',
    'lanche da tarde',
    'petisco',
    'sobremesa',
]

def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=30),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': randint(1,20),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.random_element(categories),
        },
        #'category': {
         #   'name': fake.word()
        #},
        'cover': {
            'url': random.choice(list(images))
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())