#!/usr/bin/python3
"""Console module for the HBnB project."""
import cmd


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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
