#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel

"""Module containing the program for the command interpreter"""


class HBNBCommand(cmd.Cmd, BaseModel):
    """Class to oversee the command interpreter"""

    __file_path = 'file.json'

    def __init__(self):
        """Instantiate the loop with a prompt everytime"""
        super().__init__()
        self.prompt = '(hbnb)'

    def help_create(self):
        """Method to overwrite given documentation"""

        print("\nCreates a new instance, saves it to a file")
        print("Use: create <class name>\n")

    def do_create(self, cl=None):
        """Method to control the creation of a new instance"""

        if cl == "BaseModel":
            BM = BaseModel()
            print(BM.id)
            BM.save()
        elif cl == '':
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """Method to overwrite the given documentation"""

        print("\nPrint the str representation of a specified instance")
        print("Use: show <class name> <id>\n")

    def do_show(self, arg=None):
        """Method to print the str representation of an instance"""

        if arg == '':
            print("** class name missing **")
            return

        try:
            cl, id = arg.split(' ')
        except Exception:
            if arg == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            return

        if cl == "BaseModel":
            if id == '':
                print("** instance id missing **")
            else:
                with open(self.__file_path, 'r') as file:
                    saved_instances = json.load(file)
                try:
                    instance_id = f"{cl}.{id}"
                    value = saved_instances[instance_id]
                    print(json.dumps(value))
                except Exception:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_destroy(self):
        """Method to overwrite the given documentation"""

        print("\nDeletes an instance based on class name and id")
        print("Use: destroy <class name> <id>\n")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        if arg == '':
            print("** class name missing **")
            return

        try:
            cl, id = arg.split(' ')
        except Exception:
            if arg == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            return
        if cl == "BaseModel":
            with open(self.__file_path, 'r') as file:
                saved_instances = json.load(file)
                try:
                    instance_id = f"{cl}.{id}"
                    del(saved_instances[instance_id])
                except Exception:
                    print("** no instance found **")
                    return
            with open(self.__file_path, 'w') as file:
                json.dump(saved_instances, file)

        else:
            print("** class doesn't exist")

    def do_all(self, arg):
        """Method to print str of all saved instances"""

        if arg == '' or arg == 'BaseModel':
            try:
                with open(self.__file_path, 'r') as file:
                    saved_instances = json.load(file)
                    for instance in saved_instances.keys():
                        key = json.dumps(instance)
                        value = json.dumps(saved_instances[instance])
                        print("{}: {}".format(key, value))
            except Exception:
                pass
        else:
            print("** class doesn't exist **")




    def do_quit(self, arg):
        """quit: command to exit the interpreter"""

        return True

    def do_EOF(self, arg):
        """EOF: Command to exit the interpreter"""

        return True

    def emptyline(self):
        """Overwritwe the default command given to an emptyline"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
