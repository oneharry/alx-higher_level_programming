#!/usr/bin/python3
""" Define Square class, an inheritance of Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Define Square class
        A subclass of Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the object when an instance is created"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns info about the object """
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Return the value of size """
        return self.width

    @size.setter
    def size(self, size):
        """
            Set the value of size
            Assign the same value to width and height
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
            Functions update the value of object attributes
            Args:
            *args: variable arguments
            **kwargs: keyword variable arguments
        """
        try:
            if not args and args == ():
                for key, val in kwargs.items():
                    if key == "id":
                        if val is None:
                            self.__init__(self.width, self.height, self.x,
                                          self.y)
                        self.id = val
                    elif key == "size":
                        self.size = val
                    elif key == "x":
                        self.x = val
                    elif key == "y":
                        self.y = val
            elif args and len(kwargs):
                le = len(args)
                if args[0] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                self.id = args[0]
                if le > 1:
                    self.size = args[1]
                if le > 2:
                    self.x = args[2]
                if le > 3:
                    self.y = args[3]
        except Exception:
            raise

    def to_dictionary(self):
        """
            Functions returns the dictionary representation of Square class
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
