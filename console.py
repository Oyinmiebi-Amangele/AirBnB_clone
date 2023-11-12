#!/usr/bin/python3
"""Console module for the HBnB project."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBnB"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console."""
        print()
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the console")

    def help_EOF(self):
        """Print help message for EOF command."""
        print("EOF command to exit the console")

    def help_help(self):
        """Print help message for help command."""
        print("Help command to get information about available commands")

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doen't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delect an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all the string representation for all instances."""
        args = line.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """Update an instance based on the class name"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
