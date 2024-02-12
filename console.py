#!/usr/bin/python3
"""
Module for the interpreter
"""

import shlex
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Interpreter class
    """
    prompt = '(hbnb) '
    valid_classes = [
        "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
    ]
    valid_cmd = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by typing EOF (Ctrl+D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')
            if cls[0] in self.valid_classes and cmd[0] in self.valid_cmd:
                arg = cmd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{command[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string of an instance based on the class name and id"""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        all_objects = storage.all()
        command = shlex.split(arg)
        ls = []
        if len(command) == 0:
            for key, value in all_objects.items():
                ls.append(str(value))
            if len(ls) != 0:
                print(ls)
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = command[0]
            for key in all_objects.keys():
                instance = key.split('.')
                if class_name == instance[0]:
                    value = all_objects[key]
                    ls.append(str(value))
            if len(ls) != 0:
                print(ls)

    def do_update(self, arg):
        """Updates an instance"""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
            return
        if command[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        key = "{}.{}".format(command[0], command[1])
        key = key.split(',')
        key = key[0]
        if key not in all_objects:
            print("** no instance found **")
            return
        obj = all_objects[key]
        if len(command) < 3:
            print("** attribute name missing **")
            return
        attr = command[2].split(',')
        attr = attr[0]
        if len(command) < 4:
            print("** value missing **")
            return
        value = command[3].split(',')
        value = value[0]
        setattr(obj, attr, value)
        obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_instances = storage.all()
            print(len(class_instances))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
