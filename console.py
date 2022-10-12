#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Write a program called console.py that contains the entry point of the
    command interpreter
    """
    prompt = "(hbnb)"

    def quit(self, args):
        """
        Quit the command interpreter
        """
        return True

    def EOF(self, args):
        """
        End the command interpreter
        """
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
