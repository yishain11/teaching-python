# general abstract class

from abc import ABC, abstractmethod


class Animal(ABC):

    # bad - forcing implementation - what if im breathing diff?
    def breath(self, name):
        pass

    # better - abstract
    @abstractmethod
    def abs_breath(self):
        pass


class Dog(Animal):
    def abs_breath(self):
        pass


d = Dog()

d.abs_breath()


# create cars dealership - 3 types of cars. i want each car to have start, stop that will change the state
