from scipy.ndimage import maximum_filter
import numpy
import random

result = ""
random_num = []
for _ in range(6):
    n = []
    for _ in range(4):
        randnum = random.randint(1,15)
        n.append(randnum)

        result += f" |[fill={randnum}]| "
        result += "&"
    randnum = random.randint(1,15)

    n.append(randnum)
    result += f" |[fill={randnum}]| \\\\"
    result += "\n"

    random_num.append(n)

print(result)
random_num = numpy.array(random_num)
filtered = maximum_filter(random_num, size=2, mode="constant", cval=0)
mask = (filtered == random_num)
y, x = mask.nonzero()
for coordinate in range(len(y)):
    print(f"""\\draw plot[only marks,mark=x,mark size=6pt] (mat-{y[coordinate] + 1}-{x[coordinate] + 1}); """)


