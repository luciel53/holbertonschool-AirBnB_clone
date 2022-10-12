#!/usr/bin/python3
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Write a program called console.py that contains the entry point of the
    command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit the command interpreter
        """
        return True

    def do_EOF(self, args):
        """
        End the command interpreter
        """
        return True

    def emptyline(self):
        """
        Empty the line of the command interpreter
        """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
