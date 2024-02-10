#!usr/bin/python3
from models.base import Base


"""Defines a rectangle class."""


class Rectangle(Base):
    """Represent a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self,value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """Retrieves the x of a Rectangle instance."""
        return self.__x

    @x.setter
    def x(self,value):
        """Sets the x of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance (value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """Retrieves the y of a Rectangle instance."""
        return self.__y

    @y.setter
    def y(self,value):
        """Sets the y of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance (value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of rectanglue"""
        return self.width * self.height

    def display(self):
        """dsiplay the rectanglue"""
        for y in range(self.y):
            print("")
        for num in range(self.height):
            print(" "*self.x,end="")
            print("#"*self.width)

    def update(self, *args, **kwargs):
        if (args) :
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        elif (kwargs and len(kwargs)!=0):
            for k,v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x =v
                if k == "y":
                    self.y = v
                


    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

                


    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x,self.y,self.width,self.height))

    

