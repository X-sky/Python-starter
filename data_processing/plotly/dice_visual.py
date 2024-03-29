from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

# Creates double D6s
die_1 = Die()
die_2 = Die(10)

# Make some rolls and save the results in a list
results = []
for roll_num in range(50_000):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

# Visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="Results of rolling two D6 dice 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d6.html")
