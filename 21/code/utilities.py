import os
import inspect

################################################################
####                   File Management                      ####
################################################################

def get(use_example : bool = False):
    day = __caller_day__(inspect.stack()[1])
    if use_example: return get_example(day)
    else:           return get_input(day)

def get_as_int_list(use_example : bool = False):
    day = __caller_day__(inspect.stack()[1])
    data = get_example(day) if use_example else get_input(day)
    return [int(x) for x in data.split("\n") if x != ""]

def get_input(day : int):
    path = __build_path__("input", __input_filename__(day))
    return __read_file__(path)

def get_example(day : int):
    path = __build_path__("example", __example_filename__(day))
    return __read_file__(path)

def __input_filename__(day : int) -> str:
    return "input_" + str(day).zfill(2) + ".txt"

def __example_filename__(day : int) -> str:
    return "example_" + str(day).zfill(2) + ".txt"

def __build_path__(folder : str, item : str):
    path = os.path.abspath(__file__)        # File Location
    path = os.path.dirname(path)            # Folder Location
    path = os.path.dirname(path)            # One Folder Up
    return os.path.join(path, folder, item)

def __read_file__(path : str):
    file = open(path, 'r')  # open
    content = file.read()   # read
    file.close()            # close
    return content

def __caller_day__(frame) -> str:
    filename = frame[0].f_code.co_filename  # path
    filename = os.path.basename(filename)   # file name
    return filename.split('.')[0]


