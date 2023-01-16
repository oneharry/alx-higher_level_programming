#!/usr/bin/python3
""" Define a class Base with only init func"""
import json


class Base:
    """
        A class Base
        Has one private class attribute and id instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize an instance of the class Base"""
        self.__class__.__nb_objects += 1
        try:
            if id is None:
                self.id = self.__class__.__nb_objects
            elif int(id) <= 0 or type(int(id)) is not int:
                raise TypeError("Inavlid!")
            elif int(id) > 0 and int(id) < self.__class__.__nb_objects:
                raise TypeError("Invalid!")
            else:
                self.id = int(id)
        except (ValueError, TypeError):
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A statit method.
            Returns the JSON representation of the list_dictionary
            Args:
                list_dictionary: A list of dictionaries
        """
        if list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            A class method 
            Writes the JSON representation of object lists to a filr
            Write to filename <Class name>.json
        """
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class Method
            Returns all instance with its attributes set
            Rectangle and Square sub classes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                my_class = cls(1, 1)
            else:
                my_class = cls(1)
        my_class.update(**dictionary)
        return my_class

    @classmethod
    def load_from_file(cls):
        """ Class method
            Returns a list of instance
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []
