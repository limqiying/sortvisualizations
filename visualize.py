import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sort as srt
import numpy as np

cs = "cocktailsort"
ss = "selectionsort"
bs = "bubblesort"


def visualize(x):
    """
    takes in an array of sort objects and creates the animation
    :return:
    """
    n = len(x)
    fig, ax = plt.subplots(n, 1)
    b = [0] * n
    if n == 1:
        ax = [ax]
    for i in range(n):
        b[i] = ax[i].bar(range(x[i].size()), x[i].data(), align='center', alpha=0.5, color="black")
        ax[i].axis('off')
        ax[i].set_title(x[i].sort_type())

    def animate(k):
        for bi in b:
            bi.remove()
        for j in range(n):
            if x[j].is_sorted():
                b[j] = ax[j].bar(range(x[j].size()), x[j].data(), align='center', alpha=0.5, color='green')
            else:
                x[j].update()
                b[j] = ax[j].bar(range(x[j].size()), x[j].data(), align='center', alpha=0.5, color='black')
                b[j][x[j].get_current()].set_color('r')
        return b,

    ani = animation.FuncAnimation(fig, animate, frames=100, repeat=True, blit=False, interval=1)
    plt.show()


def single_init(alg, size):
    """
    creates an animation of the single specific sorting algorithm
    :param size: size of the randomly-generated array
    """
    if alg == cs:
        x = srt.CocktailSort(size=size)
    elif alg == ss:
        x = srt.SelectionSort(size=size)
    else:
        x = srt.BubbleSort(size=size)
    visualize([x])


def three_init(size, reverse=False, nearly_sorted=False, few_unique=False):
    """
    the idea using the types of lists used were taken from https://www.toptal.com/developers/sorting-algorithms
    creates an animation of the 3 algorithms sorting the same array side-by-side
    NOTE: this does not show the actually relative time complexity of the 3 algorithms!
    """
    d = np.random.randint(0, 100, size)
    if reverse:
        d = np.sort(d)[::-1]
    if nearly_sorted:
        g = np.random.choice(size, size//4)
        d.sort()
        for index in g:
            d[index] = np.random.randint(0,100)
    if few_unique:
        d = np.array([])
        while len(d) < size:
            num = np.random.randint(0, 100)
            count = np.random.randint(0, size//4)
            d1 = np.empty(count)
            d1.fill(num)
            d = np.concatenate([d,d1])
            print(d)
        np.random.shuffle(d)
        
    x = [srt.BubbleSort(data=d), srt.CocktailSort(data=d), srt.SelectionSort(data=d)]
    visualize(x)


three_init(size=20,few_unique=True)