import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [v**2 for v in x_values]
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Reds)


# 设置图表标题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis="both", which="major", labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig("test.png", bbox_inches="tight")
