#!/usr/bin/python3
"""
main prrroject module
"""
import ast
import shlex
import re
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_dict_brk(split_cmd):
    """
    Splits the curly braces for the update method
    """
    dict_brk = re.search(r"\{(.*?)\}", split_cmd)

    if dict_brk:
        splited_id = shlex.split(split_cmd[:dict_brk.span()[0]])
        id = [i.strip(",") for i in splited_id][0]

        string_info = dict_brk.group(1)
        try:
            the_param = ast.literal_eval("{" + string_info + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, the_param
    else:
        awamer = split_cmd.split(",")
        if awamer:
            try:
                id = awamer[0]
            except Exception:
                return "", ""
            try:
                attr_name = awamer[1]
            except Exception:
                return id, ""
            try:
                attr_value = awamer[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    exist_clss = ["BaseModel", "User", "Amenity",
                  "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        Close the cli
        """
        return True

    def do_quit(self, arg):
        """
        Close the cli
        """
        return True

    def do_create(self, arg):
        """Crreatew bew obj
        Args:
            arg (dict): attrebutes
        """
        try:
            asm_cls = arg.split(" ")[0]
            if len(asm_cls) == 0:
                print("** class name missing **")
                return
            if asm_cls and asm_cls not in self.exist_clss:
                print("** class doesn't exist **")
                return

            all_args = {}
            awamer = arg.split(" ")
            for i in range(1, len(awamer)):
                key = awamer[i].split("=")[0]
                value = awamer[i].split("=")[1]
                if value.startswith('"'):
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except Exception:
                        continue
                all_args[key] = value

            if all_args == {}:
                created_obj = eval(asm_cls)()
            else:
                created_obj = eval(asm_cls)(**all_args)
            storage.new(created_obj)
            print(created_obj.id)
            storage.save()
        except Exception:
            return

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <asm_cls> <id>
        """
        awamer = shlex.split(arg)

        if len(awamer) == 0:
            print("** class name missing **")
        elif awamer[0] not in self.exist_clss:
            print("** class doesn't exist **")
        elif len(awamer) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(awamer[0], awamer[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <asm_cls> <id>
        """
        awamer = shlex.split(arg)

        if len(awamer) == 0:
            print("** class name missing **")
        elif awamer[0] not in self.exist_clss:
            print("** class doesn't exist **")
        elif len(awamer) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(awamer[0], awamer[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        objects = storage.all()

        awamer = shlex.split(arg)

        if len(awamer) == 0:
            for key, value in objects.items():
                print(str(value))
        elif awamer[0] not in self.exist_clss:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == awamer[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()

        awamer = shlex.split(arg)

        if arg:
            incoming_asm_cls = awamer[0]
        count = 0

        if awamer:
            if incoming_asm_cls in self.exist_clss:
                for obj in objects.values():
                    if obj.__class__.__name__ == incoming_asm_cls:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <asm_cls> <id> <attribute_name> "<attribute_value>"
        """
        awamer = shlex.split(arg)

        if len(awamer) == 0:
            print("** class name missing **")
        elif awamer[0] not in self.exist_clss:
            print("** class doesn't exist **")
        elif len(awamer) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(awamer[0], awamer[1])
            if key not in objects:
                print("** no instance found **")
            elif len(awamer) < 3:
                print("** attribute name missing **")
            elif len(awamer) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                dict_brk = re.search(r"\{(.*?)\}", arg)

                if dict_brk:
                    # added to catch errors
                    try:
                        string_info = dict_brk.group(1)

                        the_param = ast.literal_eval("{" + string_info + "}")

                        the_key = list(the_param.keys())
                        attribute_values = list(the_param.values())
                        try:
                            key_one = the_key[0]
                            val_one = attribute_values[0]
                            setattr(obj, key_one, val_one)
                        except Exception:
                            pass
                        try:
                            key_a = the_key[1]
                            attr_value2 = attribute_values[1]
                            setattr(obj, key_a, attr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attr_name = awamer[2]
                    attr_value = awamer[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                obj.save()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        arg_list = arg.split('.')

        cls_nm = arg_list[0]

        amr = arg_list[1].split('(')

        cmd_met = amr[0]

        split_cmd = amr[1].split(')')[0]

        all_meth = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_met in all_meth.keys():
            if cmd_met != "update":
                return all_meth[cmd_met]("{} {}".format(cls_nm, split_cmd))
            else:
                if not cls_nm:
                    print("** class name missing **")
                    return
                try:
                    inst_id, the_param = split_dict_brk(split_cmd)
                except Exception:
                    pass
                try:
                    invo = all_meth[cmd_met]
                    return invo(f"{cls_nm} {inst_id} {the_param}")
                except Exception:
                    pass
        else:
            print(f"*** Unknown syntax: {arg}")
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
