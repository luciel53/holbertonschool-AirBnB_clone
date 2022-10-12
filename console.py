#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of
the command interpreter
"""
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """
    prompt command
    """
    prompt = "(hbnb) "

    list_classes = {"BaseModel": BaseModel}

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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if args == "":
            print("** class name missing **")
        elif args not in self.list_classes:
            print("** class doesn't exist **")

        else:
            new_instance = self.list_classes[args]()
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        if args == "":
            print("** class name missing **")
        elif args.split(" ")[0] not in self.list_classes:
            print("** class doesn't exist **")
        elif len(args.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args.split(" ")[0], args.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                 print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id. (save the change
        into the JSON file).
        """
        if args == "":
            print("** class name missing **")
        elif args.split(" ")[0] not in self.list_classes:
            print("** class doesn't exist **")
        elif len(args.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args.split(" ")[0], args.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
