import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig  # Add this import statement
from datetime import datetime
from collections import OrderedDict

figure_format = "png"  # You can switch to "eps" for EPS format.
figure_dpi = 300
figure_transp = False

def plot_scores(player1: OrderedDict, player2: OrderedDict, rounds: int):
    scores = [list(player1.items()), list(player2.items())]
    fig, axes = plt.subplots(nrows=2, ncols=1)
    plt.suptitle("War Card Game Simulation Player Scores ",
                 weight='bold',
                 position=(0.5, 1))
    fig.set_size_inches(8, 4)
    plt.tight_layout(h_pad=1)
    for i in range(2):
        ax = axes[i]
        ax.set_title("Player " + str(i+1),
                     style='italic',
                     size='medium')
        ax.set_xlim(0, rounds)
        if i == 1:
            ax.set_xlabel("Round")
        ax.set_ylim(0, 52)
        ax.set_ylabel("Cards Held")
        x, y = zip(*scores[i])
        ax.plot(x, y, color='black')  # Fixed plotting x and y correctly.

    # If you want transparent backgrounds, a different file format, etc. then change these settings accordingly.
    savefig(str(datetime.now().strftime("%m-%d-%Y-%H-%M-%S.")) + figure_format,
            pad_inches=0.0,
            dpi=figure_dpi,
            format=figure_format,
            transparent=figure_transp)

    plt.close(fig)

# Example usage:
player1 = OrderedDict([(1, 26), (2, 24), (3, 22), (4, 20), (5, 18)])
player2 = OrderedDict([(1, 26), (2, 28), (3, 30), (4, 32), (5, 34)])
plot_scores(player1, player2, 5)
