#!/usr/bin/python3
"""FileStorage Module for Basemodel"""
import json

class FileStorage():
    """filestorage class for storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all return the object"""
        return self.__objects

    def new(self, obj):
        """new method that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        key: return name and id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save method serializes __objects to the JSON file
        create a file if not existing
        write into the file of serialized json object
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """relode method deserializes the JSON file to __objects 
        try: only if the JSON file (__file_path) exists ; otherwise, do nothing. 
        except: If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as my_file:
                new_dict = json.load(my_file)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split(',')
                    obj_cls = BaseModel
                    obj = obj_cls(**value)
                    self.new(obj)

        except FileNotFoundError:
            pass

