import numpy as np

values:np.ndarray = np.random.randint(1, 50, 20)

odd:list[int] = []
even:list[int] =[]

for i in values:
    if divmod(i,2)[1] == 0:
        even.append(i)
    else:
        odd.append(i)

print("EVEN NUMBERS:", even)
print("ODD NUMBERS:", odd)
