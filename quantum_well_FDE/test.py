a = [18.26619881799087, 56.36602123117598, 94.46584364966519, 132.5656660695614, 170.66548848904804, 208.76531089976075, 246.86513331721383, 284.9649557358776]

import matplotlib.pyplot as plt
x = range(0, len(a), 1)
# y = [a[n, 1] for n in range(eigenVectors[0].size)]
fig, ax = plt.subplots()
ax.plot(x, a)
fig.savefig("test.png")
plt.show()