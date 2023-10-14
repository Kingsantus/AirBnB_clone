#!/usr/bin/python3
"""console module that accept input and process"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class help process cmd input"""
    prompt = '(hbnb) '
    __classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]

    def do_create(self, arg):
        """Create a new instance of basemodel, save it and print"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance  = eval(args[0] + '()')
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """method that removes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")
    
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        all_objs = models.storage.all()
        if len(args) == 0:
            print([str(value) for value in all_objs.values()])
        elif args[0] in HBNBCommand.__classes:
            class_name = args[0]
            instances = [str(value) for key, value in all_objs.items() if key.split('.')[0] == class_name]
            print(instances)
        else:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        args = arg.split()
        all_objs = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = all_objs.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def default(self, line):
        """Handle commands in the format of <class name>.all(), 
        <class name>.count(), <class name>.show(<id>), 
        <class name>.destroy(<id>), 
        <class name>.update(<id>, 
        <attribute name>, <attribute value>), and 
        <class name>.update(<id>, <dictionary representation>)
        """
        if '.' in line:
            parts = line.split('.')
            class_name = parts[0]
            command = parts[1]
            if command == "all()":
                if class_name in self.__classes:
                    self.do_all(class_name)
                else:
                    print("** class doesn't exist **")
            elif command == "count()":
                if class_name in self.__classes:
                    count = sum(1 for key in models.storage.all() if key.startswith(class_name + "."))
                    print(count)
                else:
                    print("** class doesn't exist **")
            elif parts[1].startswith("show(") and parts[1].endswith(")"):
                if class_name in self.__classes:
                    show_id = parts[1][parts[1].find("(")+1:parts[1].find(")")]
                    self.do_show(f"{class_name} {show_id}")
                else:
                    print("** class doesn't exist **")
            elif parts[1].startswith("destroy(") and parts[1].endswith(")"):
                if class_name in self.__classes:
                    destroy_id = parts[1][parts[1].find("(")+1:parts[1].find(")")]
                    self.do_destroy(f"{class_name} {destroy_id}")
                else:
                    print("** class doesn't exist **")
            elif parts[1].startswith("update(") and parts[1].endswith(")"):
                if class_name in self.__classes:
                    update_args = parts[1][parts[1].find("(") + 1:parts[1].rfind(")")].split(", ")
                    if len(update_args) == 2 and "{" in update_args[1] and "}" in update_args[1]:
                        update_id = update_args[0]
                        dictionary_rep = eval(update_args[1])
                        for key, value in dictionary_rep.items():
                            self.do_update(f"{class_name} {update_id} {key} {value}")
                    elif len(update_args) >= 3:
                        update_id = update_args[0]
                        attr_name = update_args[1]
                        attr_value = update_args[2]
                        self.do_update(f"{class_name} {update_id} {attr_name} {attr_value}")
                    else:
                        print("** incorrect format for dictionary representation **")
                else:
                    print("** class doesn't exist **")
            else:
                super().default(line)
        else:
            super().default(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
