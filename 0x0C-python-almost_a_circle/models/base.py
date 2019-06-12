#!/usr/bin/python3
"""This module creates the Base class"""


import json
from os import path


class Base:
    """A class named Base

    Attributes:
    attr1(__nb_objects): number of objects
    attr2(id): object id
    """
    __nb_objects = 0

    def reset_objects():
        """Resets number of objects for testing"""
        Base.__nb_objects = 0

    def __init__(self, id=None):
        """Initiliazes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_dictionaries = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
                file.write(Base.to_json_string(list_dictionaries))
            return
        for model in list_objs:
            list_dictionaries.append(model.to_dictionary())
        with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
            file.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts list of dictionaries to json string"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """converts json string to object"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance based on a dictionary"""
        if cls.__name__ == "Rectangle":
            object = cls(1, 1)
            object.update(**dictionary)
            return object

        if cls.__name__ == "Square":
            object = cls(1)
            object.update(**dictionary)
            return object

    @classmethod
    def load_from_file(cls):
        """loads a list of instances from a json file"""
        if path.exists(cls.__name__ + ".json") is False:
            return []
        with open(cls.__name__ + ".json", "r",  encoding='utf-8') as file:
            listofinstances = []
            objectlist = cls.from_json_string(file.read())
            for dict in objectlist:
                objectdict = {}
                for key, value in dict.items():
                    objectdict[key] = value
                listofinstances.append(cls.create(**objectdict))
            return listofinstances
