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


class MergeSort(Sort):

    def __init__(self, data=None, size=15):
        super().__init__(data=data, size=size)
        self._i = 0
        self._j = 0
        self._k = 0
        self._L = []    # temp right and left arrays for merging
        self._R = []
        self._n1 = 0
        self._n2 = 0
        self._merged = True
        self._cur_size = 1
        self._left = 0

    def update(self):
        """
        implements the merge sort algorithm
        1 step of the merge sort algorithm is implemented, and updates the number array accordingly,
        every time update() is called
        """
        left = "left"
        n = self.size()
        if not self.is_sorted():
            mid = self._left + self._cur_size - 1
            right = min(self._left + 2*self._cur_size - 1, n-1)
            self._merge(self._left, mid, right)
            if self._merged:
                self._increment(left)

    def _merge(self, left, mid, right):
        self._n1 = mid - left + 1
        self._n2 = right - mid
        if self._merged:
            self._init_temp_arrays(left, mid)
            self._merged = False
            self._k = left

        i = "i"
        j = "j"
        k = "k"
        if self._i < self._n1 and self._j < self._n2:
            if self._L[self._i] <= self._R[self._j]:
                self._data[self._k] = self._L[self._i]
                self._increment(i)
            else:
                self._data[self._k] = self._R[self._j]
                self._increment(j)
            self._increment(k)

        elif self._i < self._n1:
            self._data[self._k] = self._L[self._i]
            self._increment(i)
            self._increment(k)

        elif self._j < self._n2:
            self._data[self._k] = self._R[self._j]
            self._increment(j)
            self._increment(k)
        else:
            self._merged = True
            self.i = 0
            self.j = 0

    def _init_temp_arrays(self, left, mid):
        self._L = [0] * self._n1
        self._R = [0] * self._n2

        for i in range(0, self._n1):
            self._L[i] = self._data[left + i]

        for j in range(0, self._n2):
            self._R[j] = self._data[mid + 1 + j]

    def _increment(self, index):
        if index == "i":
            self._i += 1
        elif index == "k":
            self._k += 1
        elif index == "left":
            if self._left + 2*self._cur_size < self.size()-1:
                self._left += 2*self._cur_size
            else:
                self._left = 0
                self._cur_size *= 2
        else:
            self._j += 1

    @staticmethod
    def sort_type():
        """
        returns a string containing the type of sort algorithm used
        """
        return "Merge Sort Algorithm"


class SelectionSort(Sort):

    def __init__(self, data=None, size=15):
        super().__init__(data=data, size=size)
        self._current = 0
        self._min = 9999

    def update(self):
        """
        implements the merge sort algorithm
        1 step of the merge sort algorithm is implemented, and updates the number array accordingly,
        every time update() is called
        """
        if not self.is_sorted():
            if self._min > self._data[self._current]:
                self._min = self._current
                if self._current == self.size()-1:
                    self._data[self._min], self._data[self._current] = self._data[self._current], self._data[self._min]
                    self._min = 9999
                    self._current = 0
                self._increment_current()



            # minimum_i = self._current + np.argmin(self._data[self._current:])
            # self._data[minimum_i], self._data[self._current] = self._data[self._current], self._data[minimum_i]
            # self._current += 1

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

    def update(self):
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
            if self._current+1 < self._size-1:
                self._current += 1
            else:
                self._forward = False
        else:
            if self._current - 1 > self._start - 1:
                self._current -= 1
            else:
                self._forward = True

    @staticmethod
    def sort_type():
        """
        returns a string containing the type of sort algorithm used
        """
        return "Cocktail Sort Algorithm"

    def get_current(self):
        return self._current
