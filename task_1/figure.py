import abc
from math import pi, sqrt

class Figure(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def set_params(self, data: list):
        pass

class Circle(Figure):
    def __init__(self, data: list):
        self.params = {"r": data[0]}

    def set_params(self, data: list):
        self.params = {"r": data[0]}
        return self

    def is_circle(self):
        return self.params["r"] > 0

    def area(self):
        if self.is_circle():
            return pi * self.params["r"] ** 2
        return("Warn: the figure can't be circle")

class Triangle(Figure):
    def __init__(self, data: list):
        self.params = {"s1": data[0], "s2": data[1], "s3": data[2]}

    def set_params(self, data: list):
        self.params = {"s1": data[0], "s2": data[1], "s3": data[2]}
        return self

    def is_triangle(self):
        if self.params["s1"] + self.params["s2"] > self.params["s3"]:
            if self.params["s1"] + self.params["s3"] > self.params["s2"]:
                if self.params["s3"] + self.params["s2"] > self.params["s1"]:
                    if self.params["s3"] > 0  and self.params["s2"] > 0 and self.params["s1"] > 0:
                        return True
        return False

    def area(self):
        if self.is_triangle():
            p = sum(self.params.values()) / 2
            return sqrt(p * (p - self.params["s1"]) * (p - self.params["s2"]) * (p - self.params["s3"]))
        return("Warn: the figure can't be triangle")

    def rect_check(self):
        hypotenuse = max(self.params.values())
        catheter_1 = min(self.params.values())
        catheter_2 = sum(self.params.values()) - hypotenuse - catheter_1
        return hypotenuse ** 2 == catheter_1 ** 2 + catheter_2 ** 2


