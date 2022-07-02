#!/usr/bin/python3
"""
importing all necessary classes and modules
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    command interpreter for the class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Method called when an empty line
        """
        pass

    def do_create(self, arg):
        """Creates a new instance
        """
        if arg == "":
            print("** class name missing **")

        elif arg not in storage.classes():
            print("** class doesn't exist **")

        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        """
        if arg == "":
            print("** class name missing **")

        else:
            arguments = arg.split()

            if arguments[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(arguments) < 2:
                print("** instance id missing **")

            else:
                instance = arguments[0] + "." + arguments[1]

                if instance not in storage.all():
                    print("** no instance found **")

                else:
                    print(storage.all()[instance])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        if arg == "":
            print("** class name missing **")

        else:
            arguments = arg.split()

            if arguments[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(arguments) < 2:
                print("** instance id missing **")

            else:
                instance = arguments[0] + "." + arguments[1]

                if instance not in storage.all():
                    print("** no instance found **")

                else:
                    del storage.all()[instance]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        string = []

        if arg == "" or arg in storage.classes():
            for key, value in storage.all().items():
                if arg in key:
                    string.append(str(value))

            print(string)

        elif arg not in storage.classes():
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        if arg == "":
            print("** class name missing **")

        else:
            arguments = arg.split()

            if arguments[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(arguments) < 2:
                print("** instance id missing **")

            else:
                instance = arguments[0] + "." + arguments[1]

                if instance not in storage.all():
                    print("** no instance found **")

                elif len(arguments) < 3:
                    print("** attribute name missing **")

                elif len(arguments) < 4:
                    print("** value missing **")

                else:
                    if arguments[2] != "id":
                        for key, value in storage.all().items():
                            if key == instance:
                                setattr(value, arguments[2],
                                        eval(arguments[3]))
                                value.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
