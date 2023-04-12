#!/usr/bin/python3

"""
Square class module
Usage: ./square.py
"""


class square():
    """
    The Square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """The constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_the_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String reresentation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """This should be fun"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_the_square())
