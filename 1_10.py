import json
import os
import numpy as np
import matplotlib.pyplot as plt

def f(x):

    return (np.sin(3*np.pi*x))*(np.sin(3*np.pi*x))*(np.sin(3*np.pi*x))+((x-1)**2)*(1+(np.sin(3*np.pi))*(np.sin(3*np.pi)))

#параметры
x_values = np.linspace(-10, 10, 1000)
#расчёт координат
y_values = f(x_values)
data = [{"x": x, "y": y} for x, y in zip(x_values, y_values)]
#cоздание директории
if not os.path.exists('results'):
    os.makedirs('results')
#сохранение в JSON
with open('results/function_values.json', 'w') as file:
    json.dump({"data": data}, file)
#построение графика функции
plt.figure(figsize=(16, 9))
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
#plt.xscale('symlog')
plt.grid(1)
plt.legend()
plt.savefig('results/function_plot.png')
plt.show()
