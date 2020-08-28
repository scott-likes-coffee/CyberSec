#!/usr/bin/python3
# import this is a random number generator
import random

# choices the magic 8 ball can produce

choices = ("Cannot predict now!", "Ask again later!", "Yes!", "No!", "Give up!", "IDK ask your mother!", \
"I am not qualified to take on your human issues")
# set value as variable using random number generator
# generate a random number using choices beginning from 1st item to last
value = random.randint(0,len(choices)-1)
# random answer
print(choices[value])
