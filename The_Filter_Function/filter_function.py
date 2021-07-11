import collections
from pprint import pprint
from typing import Sized

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

# Return an iterator yielding those items in the iterable for which the function is true.
filter_scientist = filter(lambda x: x.nobel is True, scientists)
pprint(filter_scientist)  # <filter object at 0x7f8e7f8d5f60>
pprint(tuple(filter_scientist))  # (Scientist(name='Ada Lovelace',...
print("")
# we can make the filter more specific by filtering on a specific field
filter_field = filter(lambda x: x.field ==
                      'physics' and x.nobel is True, scientists)
pprint(tuple(filter_field))
print("")

# another posible way to do the same is to use a for loop
# we can use the for loop to iterate over the items in the iterable
# and check if the condition is true
for x in scientists:
    if x.nobel is True:
        print(x)
print("")

# another way is by using a function to filter the items


def filter_nobel(x):
    return x.nobel is True


# we created a reusable function to filter the items
pprint(tuple(filter(filter_nobel, scientists)))
print("")

# Filetering List Comprehensions
# we can do the same with list comprehensions
# we can use the list comprehension to iterate over the items in the iterable
# and check if the condition is true
pprint(tuple(x for x in scientists if x.nobel is True))
