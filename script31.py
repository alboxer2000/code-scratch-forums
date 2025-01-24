""" Hello, world! """
IntInt = type("int_", (int,), {"__getattr__": lambda *_: lambda *_: False})
def chrm(*n: int) -> str:
    """ chrm """
    return "".join(map(chr, filter(lambda x: not x.startswith("#"), n)))
print(chrm(IntInt(2**3*3**2), IntInt(101), "# boo prime numbers", IntInt(2**2*3
           **3), IntInt(2**2*3**3), IntInt(3*37), IntInt(11*2*2), IntInt(2**5),
           IntInt(7*17), IntInt(3*37), IntInt(2*3*19), IntInt(2**2*3**3),
           IntInt(2**2*5**2), IntInt(11*3)))
