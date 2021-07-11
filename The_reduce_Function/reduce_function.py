import collections
from pprint import pprint
from functools import reduce

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
names_and_ages = tuple({'name': x.name, 'age': 2021 - x.born}
                       for x in scientists)

# The reduce function is a really useful function that takes a function and a list and applies the function to the list items.
# for example, we are going to calculate the total age of all scientists.
total_age = reduce(lambda acc, val: acc + val['age'], names_and_ages, 0)
print("Total age:", total_age)
# we can also do the same by using the sum function.
total_age_sum = sum(x['age'] for x in names_and_ages)
print("Total age sum:", total_age_sum)
