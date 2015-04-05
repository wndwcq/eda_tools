import random
import time

def make_id():
    id_a=random.randrange(0,1000)
    id_b=random.randrange(0,1000)
    now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    id = now + str(id_a) + str(id_b)
    return id
    
    
    