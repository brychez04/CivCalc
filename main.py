from TrussComponents import *
from Gaussian import Gaussian as g

joint1 = Joint(1, 1)
joint2 = Joint(2, 2)

member = Member(joint1, joint2)

print(joint1)
print(joint2)
print(member)

coefficients = [[3, -1],[1, 2]]
equal_values = [1, 12]

results = g.solve(coefficients, equal_values)
print(results)





