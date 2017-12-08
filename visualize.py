import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sort as srt
import numpy as np
from collections import defaultdict

cs = "cocktailsort"
ss = "selectionsort"
bs = "bubblesort"


def visualize(x):
    """
    takes in an array of sort objects and creates the animation
    :return:
    """
    n = len(x)
    fig, ax = plt.subplots(n, 1, figsize=(5, 7))
    b = [0] * n
    steps = defaultdict(lambda: 0)     # keeps track of the number of steps for the algorithms to sort
    # keeps track of which algorithms are done sorting.
    # Makes running animation faster since sorted arrays need not be updated
    sorted_display = [False] * n
    if n == 1:
        ax = [ax]
    for i in range(n):
        b[i] = ax[i].bar(range(x[i].size()), x[i].data(), align='center', alpha=0.5, color="black")
        ax[i].axis('off')
        ax[i].set_title(x[i].sort_type())

    def animate(k):
        for j in range(n):
            if x[j].is_sorted():
                if not sorted_display[j]:
                    b[j].remove()   # remove existing bar plot
                    time_label = "Step Count: %s" % str(steps[j])
                    ax[j].text(8, 8, time_label)
                    b[j] = ax[j].bar(range(x[j].size()), x[j].data(), align='center', alpha=0.5, color='green')
                    sorted_display[j] = True
            else:
                b[j].remove()
                x[j].update()
                steps[j] += 1   # increment the number of steps
                b[j] = ax[j].bar(range(x[j].size()), x[j].data(), align='center', alpha=0.5, color='black')
                b[j][x[j].get_current()].set_color('r')
        return b,

    ani = animation.FuncAnimation(fig, animate, frames=100, blit=False, interval=1)
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


def three_init(size=20, reverse=False, nearly_sorted=False, few_unique=False):
    """
    the idea using the types of lists used were taken from https://www.toptal.com/developers/sorting-algorithms
    creates an animation of the 3 algorithms sorting the same array side-by-side
    NOTE: this does not show the actually relative time complexity of the 3 algorithms!
    additional parameters allows user to specify the type of array to be sorted.
    If parameters are empty, then a random array is generated.
    """
    if reverse:
        d = reverse_array(size)
    if nearly_sorted:
        d = nearly_sorted_array(size)
    if few_unique:
        d = few_unique_array(size)
    x = [srt.BubbleSort(data=d), srt.CocktailSort(data=d), srt.SelectionSort(data=d)]
    visualize(x)


def reverse_array(size):
    """
    generates a random array that is sorted-reverse
    """
    d = np.random.randint(0, 100, size)
    return np.sort(d)[::-1]


def nearly_sorted_array(size):
    """
    generates an array that is almost sorted
    """
    d = np.random.randint(0, 100, size)
    g = np.random.choice(size, size // 4)
    d.sort()
    for index in g:
        d[index] = np.random.randint(0, 100)
    return d


def few_unique_array(size):
    """
    generates an array where few of the elements are unique
    """
    d = np.array([])
    while len(d) < size:
        num = np.random.randint(0, 100)
        count = np.random.randint(0, size//4)
        d1 = np.empty(count)
        d1.fill(num)
        d = np.concatenate([d, d1])
    np.random.shuffle(d)
    return d

three_init(20, reverse=True)