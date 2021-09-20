def greeting(name: str) -> str:
    return "Hello " + name


def addition(int1=0, int2=0):
    return int1 + int2


def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


# standard 1
def capture_first_name_from_cmd_line():
    return

