import collections
from pprint import pprint

Scientists = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = (
    Scientists(name="Ada Lovelace", field="math", born=1815, nobel=False),
    Scientists(name="Emmy Noether", field="math", born=1882, nobel=False),
    Scientists(name="Marie Curie", field="physics", born=1867, nobel=True),
    Scientists(name="Tu Youyou", field="chemistry", born=1930, nobel=True),
    Scientists(name="Ada Yonath", field="chemistry", born=1939, nobel=True),
    Scientists(name="Vera Rubin", field="astronomy", born=1928, nobel=False),
    Scientists(name="Sally Ride", field="physics", born=1951, nobel=False),
)

# The map function is a higher-order function that takes a function and an iterable as arguments, and returns an iterator that applies the function to each element of the iterable.
# Stops when the iterable is exhausted.
# We ususally use map to apply a function to all the elements of a list.
# and then we can use the list function to convert the result to a list.
names_and_ages = tuple(map(
    lambda x:
    {'name': x.name, 'age': 2021 - x.born},
    scientists
))
# this took the original tuple, and created a new tuple with the results of the map function applied to each element of the original tuple.
pprint(names_and_ages)
# ({'age': 206, 'name': 'Ada Lovelace'},
#  {'age': 139, 'name': 'Emmy Noether'},
#  {'age': 154, 'name': 'Marie Curie'},
#  {'age': 91, 'name': 'Tu Youyou'},
#  {'age': 82, 'name': 'Ada Yonath'},
#  {'age': 93, 'name': 'Vera Rubin'},
#  {'age': 70, 'name': 'Sally Ride'})

# To make this more pythonic, we can use list comprehensions.
names_and_ages = [{'name': x.name, 'age': 2021 - x.born} for x in scientists]
pprint(names_and_ages)
# [{'age': 206, 'name': 'Ada Lovelace'},
#  {'age': 139, 'name': 'Emmy Noether'},
#  {'age': 154, 'name': 'Marie Curie'},
#  {'age': 91, 'name': 'Tu Youyou'},
#  {'age': 82, 'name': 'Ada Yonath'},
#  {'age': 93, 'name': 'Vera Rubin'},
#  {'age': 70, 'name': 'Sally Ride'}]
names_and_ages = [{'name': x.name.upper(), 'age': 2021 - x.born} for x in scientists]
pprint(names_and_ages)