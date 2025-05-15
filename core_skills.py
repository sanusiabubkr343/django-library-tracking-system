from datetime import datetime, timedelta
import random

rand_list = []
for i in range(20):
    x = random.randint(1, 20)
    rand_list.append(x)
list_comprehension_below_10 = [item for item in rand_list if item < 10]
list_comprehension_below_10 = filter(lambda x: x < 10, rand_list)


print(datetime.now() + timedelta(days=14))
