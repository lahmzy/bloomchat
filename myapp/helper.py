import random
from django.contrib.auth.models import User
def randoms():
    array=""
    for i in range(1,8):
        num=random.randint(1,10)
        array+=str(num)
    return array