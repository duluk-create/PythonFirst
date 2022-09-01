
from matplotlib import pyplot as plt
plt.xkcd()
ages_x = range(25, 36)
dev_y = [38296, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45296, 48000, 53752, 54320, 60200, 65000, 67316, 68828, 69317, 78648, 83752]
js_dev_y = [2296, 38000, 43752, 54320, 60200, 75000, 87316, 98828, 109317, 110048, 112752]

#Datensätze

plt.plot(ages_x, dev_y, linestyle='--', marker='.', label='All Devs')
plt.plot(ages_x, js_dev_y, color='#adad3b', label='JavaScript', linewidth=3)
plt.plot(ages_x, py_dev_y, marker='o', label='Python')
plt.legend()

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.grid(True)

plt.tight_layout()

plt.show()
