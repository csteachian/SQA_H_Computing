height = [1.87 for i in range(10)]
weight = [75 for i in range(10)]
BMI = [0 for i in range(10)]

# Passing parallel arrays to a function - messy!
def calculateBMI(weight, height, BMI, size):
    for i in range(size):
        BMI[i] = weight[i] / (height[i] ** 2)
    return BMI
  

# What if we pass them in wrong order?
calculateBMI(height, weight, BMI, 10)  # Disaster!

