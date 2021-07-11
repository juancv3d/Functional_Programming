import collections
from pprint import pprint

# Dictionary
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
    {'name': 'Marie Curie', 'field': 'physics', 'born': 1867, 'nobel': True},
]
# print(scientists)
# Dictionaries are mutable, so we can modify them by accessing them with a key.
scientists[0]['name'] = 'Ed Lovelace'
print(scientists)

# We can also make typo error in the dictionary. We can also make typo errors and there is no validation.
# {'nime': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False}
# A better way to implement this is by using the collections module
Scientists = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])
# By doing this we can now create an instance of the scientist.
ada = Scientists(name="Ada Lovelace", field="math", born=1815, nobel=False)
# we created an object called ada, which is an immutable object.
print(ada.name)
print(ada.field)

# Danger Zone: Mixing mutable and immutable data structures
# When we mix mutable and immutable data structures, we can get unexpected results.
scientists = [
    Scientists(name="Ada Lovelace", field="math", born=1815, nobel=False),
    Scientists(name="Emmy Noether", field="math", born=1882, nobel=False),
]
# Now we have a scientists list, and while we cannot modify the individual elements, we can still modify the whole list.
# for example we can delete the second element of the list.
del scientists[1]
print(scientists)

# Best way to implement this is by using tuples.
scientists = (
    Scientists(name="Ada Lovelace", field="math", born=1815, nobel=False),
    Scientists(name="Emmy Noether", field="math", born=1882, nobel=False),
    Scientists(name="Marie Curie", field="physics", born=1867, nobel=True),
    Scientists(name="Tu Youyou", field="chemistry", born=1930, nobel=True),
    Scientists(name="Ada Yonath", field="chemistry", born=1939, nobel=True),
    Scientists(name="Vera Rubin", field="astronomy", born=1928, nobel=False),
    Scientists(name="Sally Ride", field="physics", born=1951, nobel=False),
)
pprint(scientists)
# With this tuple of scientists we cannot modify the individual elements. but still we can access them.
# del scientists[1] wont work
