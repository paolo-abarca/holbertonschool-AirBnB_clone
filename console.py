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

    def do_count(self, arg):
        """
        method that counts all instances of a class
        """
        count = 0
        if arg not in storage.classes():
            print("** class doesn't exist **")

        else:
            for key, value in storage.all().items():
                key_class = key.split(".")
                if arg in key_class:
                    count = count + 1

            print(count)

    def do_BaseModel(self, arg):
        """
        retrieve all instances of the BaseModel
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("BaseModel")

        elif arguments[1] == "count()":
            self.do_count("BaseModel")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "BaseModel" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "BaseModel" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "BaseModel" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)

    def do_User(self, arg):
        """
        retrieve all instances of the User
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("User")

        elif arguments[1] == "count()":
            self.do_count("User")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "User" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "User" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "User" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)

    def do_State(self, arg):
        """
        retrieve all instances of the State
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("State")

        elif arguments[1] == "count()":
            self.do_count("State")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "State" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "State" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "State" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)

    def do_City(self, arg):
        """
        retrieve all instances of the City
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("City")

        elif arguments[1] == "count()":
            self.do_count("City")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "City" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "City" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "City" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)

    def do_Amenity(self, arg):
        """
        retrieve all instances of the Amenity
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("Amenity")

        elif arguments[1] == "count()":
            self.do_count("Amenity")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "Amenity" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "Amenity" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "Amenity" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)

    def do_Place(self, arg):
        """
        retrieve all instances of the Place
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("Place")

        elif arguments[1] == "count()":
            self.do_count("Place")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "Place" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "Place" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "Place" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)

    def do_Review(self, arg):
        """
        retrieve all instances of the Review
        class using: <class name>.all()
        """
        arguments = arg.split(".")

        if arguments[1] == "all()":
            self.do_all("Review")

        elif arguments[1] == "count()":
            self.do_count("Review")

        else:
            a = arguments[1].split("(\"")
            my_arg = a[1].split("\"")

            if a[0] == "show":
                real_argum = "Review" + " " + my_arg[0]
                self.do_show(real_argum)

            elif a[0] == "destroy":
                real_argum = "Review" + " " + my_arg[0]
                self.do_destroy(real_argum)

            else:
                if a[0] == "update":
                    real_argum2 = "Review" + " " + my_arg[0] + " "\
                            + my_arg[2] + " " + "\"" + my_arg[4] + "\""

                    self.do_update(real_argum2)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
