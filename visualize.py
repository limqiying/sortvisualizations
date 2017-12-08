import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sort as srt
import numpy as np
from functools import partial

cs = "cocktailsort"
ss = "selectionsort"
bs = "bubblesort"


def single_init(alg, size):
    """
    creates an animation of the single specific sorting algorithm
    :param size: size of the randomly-generated array
    """
    global fig, x, n
    fig, ax = plt.subplots()
    if alg == cs:
        x = srt.CocktailSort(size=size)
    elif alg == ss:
        x = srt.SelectionSort(size=size)
    else:
        x = srt.BubbleSort(size=size)
    n = plt.bar(range(x.size()), x.data(), align='center', alpha=0.5, color="black")
    plt.title(x.sort_type())
    plt.axis('off')
    plt.grid(True)
    interval = 2000/size
    ani = animation.FuncAnimation(fig, animate, frames=10, repeat=True, blit=False, interval=interval)
    plt.show()


def three_init(size):
    """
    creates an animation of the 3 algorithms sorting the same array side-by-side
    NOTE: this does not show the actually relative time complexity of the 3 algorithms!
    """
    global fig, x, b, ax
    fig, ax = plt.subplots(3, 1)
    d = np.random.randint(0, 100, size)
    x = [srt.BubbleSort(data=d), srt.CocktailSort(data=d), srt.SelectionSort(data=d)]
    b = [0]*3
    for i in range(3):
        b[i] = ax[i].bar(range(x[i].size()), x[i].data(), align='center', alpha=0.5, color="black")
        ax[i].axis('off')
        ax[i].set_title(x[i].sort_type())
    ani = animation.FuncAnimation(fig, animate_3, frames=100, repeat=True, blit=False, interval=1)
    plt.show()


def animate(i):
    global n
    n.remove()
    if x.is_sorted():
        n = plt.bar(range(x.size()), x.data(), align='center', alpha=0.5, color='green')
    else:
        x.update()
        n = plt.bar(range(x.size()), x.data(), align='center', alpha=0.5, color='black')
        n[x.get_current()].set_color('r')
    return n,


def animate_3(i):
    global b, x
    for bi in b:
        bi.remove()
    for i in range(3):
        if x[i].is_sorted():
            b[i] = ax[i].bar(range(x[i].size()), x[i].data(), align='center', alpha=0.5, color='green')
        else:
            x[i].update()
            b[i] = ax[i].bar(range(x[i].size()), x[i].data(), align='center', alpha=0.5, color='black')
    return b,

three_init(size=20)

