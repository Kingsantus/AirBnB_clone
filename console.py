#!/usr/bin/python3
"""console module that accept input and process"""
import cmd
from models.base_model import BaseModel

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
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

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
