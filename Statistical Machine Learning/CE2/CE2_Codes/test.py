import matplotlib.pyplot as plt
import pacal as pc

X1 = pc.UniformDistr(0, 1)
X2 = pc.UniformDistr(1, 2)
X = 0
for i in range(0, 10):
    X += (pc.UniformDistr(i, i + 1))
X.plot()
pc.show()
