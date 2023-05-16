#!/usr/bin/python3
"""Creating a base class"""


import json
import os
import csv
import turtle

class Base:
    """The base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None and len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            return []
        else:
            list = []
            list = [items.to_dictionary() for items in list_objs]
            with open("{}.json".format(cls.__name__), "w") as file:
                file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        """
        if json_string is None and len(json_string) == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            staff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in staff]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        with open(cls.__name__ + ".csv", "w") as csv_file:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in csv"""
        lst = []
        if os.path.exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        lst.append(i)
        return lst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        """
        turtle.getscreen()
        turtle.shape("turtle")
        for rect in list_rectangles:
            turtle.pencolor(red)
            turtle.setpos(rect.x, rect.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rect.height)
                turtle.left(90)
                turtle.forward(rect.width)
                turtle.left(90)
            turtle.penup()
        for sq in list_squares:
            turtle.pencolor(blue)
            turtle.setpos(sq.x, sq.y)
            turtle.pendown()
            for i in range(4):
                turtle.foward(sq.height)
                turtle.left(90)
            turtle.penup()
        turtle.exitonclick()
