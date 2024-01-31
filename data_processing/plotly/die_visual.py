from plotly.graph_objects import Bar, Layout
import plotly.offline as offline

# import plotly.io as pio
from die import Die

# pio.renderers.default = "browser"


def draw_plot():
    # Create a D6
    die = Die()

    # make some rolls and save the results in a list
    results = []
    for _ in range(1000):
        result = die.roll()
        results.append(result)

    # analyze the results
    frequencies = []
    for value in range(1, die.num_sides + 1):
        frequencies.append(results.count(value))

    x_values = list(range(1, die.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {"title": "Result"}
    y_axis_config = {"title": "Frequency of the result"}
    my_layout = Layout(
        title="Roll a D6 1000 times", xaxis=x_axis_config, yaxis=y_axis_config
    )
    offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
    # got error
    # Figure(data=data, layout=my_layout).show(renderer="browser")


if __name__ == "__main__":
    draw_plot()
