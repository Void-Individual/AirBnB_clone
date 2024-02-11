#!/usr/bin/python3
import cmd
import json
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.base_model import BaseModel

"""Module containing the program for the command interpreter"""


class HBNBCommand(cmd.Cmd, BaseModel):
    """Class to oversee the command interpreter"""

    valid_classes = {'BaseModel': BaseModel,
                     'User': User,
                     'Place': Place,
                     'Amenity': Amenity,
                     "City": City,
                     'Review': Review,
                     "State": State
                     }

    def __init__(self):
        """Instantiate the loop with a prompt everytime"""
        super().__init__()
        self.prompt = '(hbnb) '

    def help_create(self):
        """Method to overwrite given documentation"""

        print("\nCreates a new instance, saves it to a file")
        print("Use: create <class name>\n")

    def do_create(self, cl=None):
        """Method to control the creation of a new instance"""

        if cl in self.valid_classes:
            active_class = self.valid_classes[cl]()
            storage.save()
            print(active_class.id)
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
            if cl in self.valid_classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            return

        if cl in self.valid_classes:
            if id == '':
                print("** instance id missing **")
            else:
                try:
                    instance_id = f"{cl}.{id}"
                    stored = storage.all()
                    value = stored[instance_id]
                    print(value)
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
            if cl in self.valid_classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            return

        if cl in self.valid_classes:
            saved_instances = storage.all()
            try:
                instance_id = f"{cl}.{id}"
                del saved_instances[instance_id]
                storage.save()
            except Exception:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist")

    def do_all(self, arg):
        """Method to print str of all saved instances"""

        stored = storage.all()
        list_st = []
        if arg == '':
            for key in stored.keys():
                value = stored[key]
                st = f"{value}"
                list_st.append(st)
            if len(list_st) != 0:
                print("{}".format(list_st))
        elif arg in self.valid_classes:
            for key in stored.keys():
                cl_name, inst_id = key.split('.')
                if cl_name == arg:
                    value = stored[key]
                    st = f"{value}"
                    list_st.append(st)
            if len(list_st) != 0:
                print("{}".format(list_st))

        else:
            print("** class doesn't exist **")

    def help_update(self):
        """Method to overwrite the default help"""

        print("\nUpdates or add attributes to an instance")
        print('Usage: update <class name> <id>'
              ' <attribute name> "<attribute value>"\n')

    def do_update(self, arg):
        """Method to add or update attributes of an instance"""

        if arg == '':
            print("** class name missing **")
            return

        split_arg = arg.split()
        cl = ''
        id = ''
        att_name = ''
        att_value = ''
        for idx, st in enumerate(split_arg):
            if idx == 0:
                cl = st
            elif idx == 1:
                id = st
            elif idx == 2:
                att_name = st
            elif idx == 3:
                att_value = st
            elif idx > 3:
                break

        if cl not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if id == '':
            print("** instance id missing **")
            return

        stored = storage.all()
        instance_id = f"{cl}.{id}"
        try:
            obj = stored[instance_id]
        except Exception:
            print("** no instance found **")
            return

        if att_name == '':
            print("** attribute name missing **")
            return

        if att_value == '':
            print("** value missing **")
            return

        setattr(obj, att_name, att_value)

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
