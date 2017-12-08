import numpy as np


class Sort:
    """
    Contains an array of numbers and methods to retrieve information on array
    """

    def __init__(self, data=None, size=15):
        """
        If data is specified, initializes an array as specified by data
        If size is specified, initializes an array of specified size
        Otherwise, initialize a random array with default size 15
        :param data: A numpy array of integers
        :param size: int
        """
        if data is None:
            self._data = np.random.randint(0, 100, size)
            self._size = size
        else:
            self._data = np.array(data)
            self._size = len(data)

    def is_sorted(self, left_i=None, right_i=None):
        """
        Returns boolean indicating if class array[l_i:r_i] is sorted
        if no array is input, checks if entire class array is sorted
        """
        if left_i is None and right_i is None:
            return np.all(self._data[:-1] <= self._data[1:])
        else:
            array = self._data[left_i:right_i]
            return np.all(array[:-1] <= array[1:])

    def data(self):
        """
        returns the numpy array
        """
        return self._data

    def size(self):
        """
        returns the size of the array
        """
        return self._size


class BubbleSort(Sort):

    def __init__(self, data=None, size=15):
        super().__init__(data=data, size=size)
        self._i = 0
        self._j = 0

    def update(self):
        """
        implements the bubble sort algorithm
        1 step of the bubble sort algorithm is implemented, and updates the number array accordingly,
        every time update() is called
        """
        if not self.is_sorted():
            if self._data[self._j] > self._data[self._j + 1]:
                    self._data[self._j], self._data[self._j+1] = self._data[self._j+1], self._data[self._j]
                    self._increment_j()
            else:
                self._increment_j()

    def _increment_i(self):
        if self._i < self.size()-1:
            self._i += 1

    def _increment_j(self):
        if self._j < self._size - self._i - 2:
            self._j += 1
        else:
            self._increment_i()
            self._j = 0

    def get_current(self):
        """
        returns the index of the array at which the algorithm is currently at
        """
        return self._j

    @staticmethod
    def sort_type():
        """
        returns a string containing the type of sort algorithm used
        """
        return "Bubble Sort Algorithm"


class SelectionSort(Sort):

    def __init__(self, data=None, size=15):
        super().__init__(data=data, size=size)
        self._current = 0   # pointer to where the algorithm is at
        self._min = 0   # pointer to the index at where the current minimum is at
        self._sorting_index = 0     # keeps track of the index up to where the list has been sorted

    def update(self):
        """
        implements the merge sort algorithm
        1 step of the merge sort algorithm is implemented, and updates the number array accordingly,
        every time update() is called
        """
        if not self.is_sorted():
            # if the current index has a smaller value than the current minimum, update the current minimum
            if self._data[self._min] > self._data[self._current]:
                self._min = self._current
            # if we have reached the end of the list, then swap the smallest element we find to the front of our array
            if self._current == self.size()-1:
                # swap the smallest element in the list with the item at the fro
                self._data[self._min], self._data[self._sorting_index] = self._data[self._sorting_index], self._data[self._min]
                self._sorting_index += 1    # update sorting index since now one more element is sorted
                self._min = self._sorting_index
                self._current = self._sorting_index - 1
            self._increment_current()   # increments the current counter

    @staticmethod
    def sort_type():
        """
        returns a string containing the type of sort algorithm used
        """
        return "Selection Sort Algorithm"

    def _increment_current(self):
        self._current += 1

    def get_current(self):
        """
        returns the index of the array at which the algorithm is currently at
        """
        return self._current


class CocktailSort(Sort):

    def __init__(self, data=None, size=15):
        super().__init__(data=data, size=size)
        self._current = 0
        self._forward = True
        self._start = 0
        self._end = self.size()

    def update(self):
        print(self._start)
        """
        implements the cocktail sort algorithm
        1 step of the cocktail sort algorithm is implemented, and updates the number array accordingly,
        every time update() is called
        """
        if not self.is_sorted():
            if self._data[self._current] > self._data[self._current+1]:
                self._data[self._current], self._data[self._current+1] = self._data[self._current+1], self._data[self._current]
                self._increment_current()
            else:
                self._increment_current()

    def _increment_current(self):
        """
        updates position of the current pointer index
        """
        if self._forward:
            if self._current+1 < self._end - 1:
                self._current += 1
            else:
                self._forward = False
                self._end -= 1
        else:
            if self._current - 1 > self._start - 1:
                self._current -= 1
            else:
                self._start += 1
                self._forward = True

    @staticmethod
    def sort_type():
        """
        returns a string containing the type of sort algorithm used
        """
        return "Cocktail Sort Algorithm"

    def get_current(self):
        return self._current
