
# WAP to create the following dataset using numpy and pandas
# sapid Fname Lname Subject Teacher Marks
# use matplotlib/seaborn to draw the visualization plots

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l1=["Hey", 123, "HI007"]
n1=np.array([l1])
print(n1)
d=pd.DataFrame(data=np.arange(0,70).reshape(10,7))
print(d)
data = {
    "sapid": [500124835, 500123727, 500123751],
    "Fname": ["Abhay", "Adarsh", "Ayush"],
    "Lname": ["butola", "gusain", "rawat"],
    "Subject": ["C", "Python", "Physics"],
    "Teacher": ["Bhawana", "Sajid", "Kailash"],
    "Marks": [97, 99, 81]
}

df=pd.DataFrame(data, index=[1,2,3])

print(df)

# Visualization using Matplotlib
plt.figure(figsize=(8, 6))
plt.bar(df['Fname'], df['Marks'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.show()
