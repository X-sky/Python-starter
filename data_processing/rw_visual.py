import matplotlib.pyplot as plt

from random_walk import RandomWalk


def draw_plot():
    # Create a random walk instance and fill it
    rw = RandomWalk(50_000)
    rw.fill_walk()
    # plot all the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots()

    ax.scatter(
        rw.x_values,
        rw.y_values,
        s=1,
        c=range(rw.num_points),
        cmap=plt.cm.Blues,
        edgecolors="none",
    )

    def emphasize_point(idx, **scatter_args):
        """Emphasize a point in the plot"""
        final_args = dict(s=10, edgecolors="none", c="red")
        final_args.update(scatter_args)
        ax.scatter(
            rw.x_values[idx],
            rw.y_values[idx],
            **final_args,
        )

    emphasize_point(0, c="green")
    emphasize_point(-1, c="red", s=120)
    plt.show()


if __name__ == "__main__":
    draw_plot()
