#!/usr/bin/python3
"""console module that accept input and process"""
import cmd
import models
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class help process cmd input"""
    prompt = '(hbnb) '
    __classes = [
            "BaseModel"
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
