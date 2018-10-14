from Tkinter import *
from visualize import *


class MyGui:

    def __init__(self, master):
        self.master = master
        master.title("Sorting Visualization")

        self.entered_number = 0

        self.label = Label(master, text="Enter number of Element of the array:")

        vcmd = master.register(self.validate)  # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.bubble_sort_button = Button(master, text="Bubble Sort Single", command=lambda: self.bubble_sort_alone())
        self.select_sort_button = Button(master, text="Selection Sort Single", command=lambda: self.select_sort_alone())
        self.cocktail_sort_button = Button(master, text="CockTail Sort Single",
                                           command=lambda: self.cocktail_sort_alone())

        self.random_button = Button(master, text="Random", command=lambda: self.random_init())
        self.reverse_button = Button(master, text="Array is reversed sorted", command=lambda: self.reverse_init())
        self.few_unique_button = Button(master, text="Array has a few unique elements",
                                        command=lambda: self.fewUnique_init())
        self.almost_sorted_button = Button(master, text="Array is almost sorted",
                                           command=lambda: self.almostSorted_init())

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W + E)

        self.bubble_sort_button.grid(row=2, column=0)
        self.select_sort_button.grid(row=2, column=1)
        self.cocktail_sort_button.grid(row=2, column=2, sticky=W + E)
        self.random_button.grid(row=3, column=1)
        self.reverse_button.grid(row=4, column=1)
        self.few_unique_button.grid(row=5, column=1)
        self.almost_sorted_button.grid(row=6, column=1)

    def bubble_sort_alone(self):
        size = self.entered_number if self.entered_number > 0 else 20
        single_init(bs, size)

    def select_sort_alone(self):
        size = self.entered_number if self.entered_number > 0 else 20
        single_init(ss, size)

    def cocktail_sort_alone(self):
        size = self.entered_number if self.entered_number > 0 else 20
        single_init(cs, size)

    def random_init(self):
        size = self.entered_number if self.entered_number > 0 else 20
        three_init(size=size)

    def reverse_init(self):
        size = self.entered_number if self.entered_number > 0 else 20
        three_init(size=size, reverse=True)

    def fewUnique_init(self):
        size = self.entered_number if self.entered_number > 0 else 20
        three_init(size, nearly_sorted=True)

    def almostSorted_init(self):
        size = self.entered_number if self.entered_number > 0 else 20
        three_init(size, few_unique=True)

    def validate(self, new_text):

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False


root = Tk()
my_gui = MyGui(root)
root.mainloop()
