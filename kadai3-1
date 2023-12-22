import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib 
data = [[3231, 1452], [3747, 1796], [3726, 1894], [5853, 2584], [8866, 2735], [10913, 3447]]

x = np.array([u[0] for u in data])
y = np.array([u[1] for u in data])

annotations = ["2014年", "2015年", "2016年", "2017年", "2018年", "2019年"]

plt.scatter(x,y)
plt.title("年度別のオープンキャンパスの参加者数と志願者数")
plt.xlabel("志願者数")
plt.ylabel("参加者数")
plt.grid(True)

for i, label in enumerate(annotations):
    plt.annotate(label, (x[i], y[i]))

plt.show()