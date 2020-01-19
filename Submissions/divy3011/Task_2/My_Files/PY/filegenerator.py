import os

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
# print(type(randomString(10)))
for i in range(100):
    fd=open((randomString(10)+'.rss'),'w')
    fd.close()