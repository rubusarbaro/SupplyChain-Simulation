class Entity:
    def __init__(self):
        pass

class Company(Entity):
    def __init__(self):
        pass

class Consumer(Entity):
    def __init__(self):
        pass

class Manufacturer(Entity):
    def __init__(self):
        pass

class Transport(Entity):
    def __init__(self):
        pass

class Facility:
    def __init__(self):
        pass

class Plant(Facility):
    def __init__(self):
        pass

class Warehouse(Facility):
    def __init__(self):
        pass

class Machine:
    def __init__(self):
        pass

class Material:
    def __init__(self):
        pass

class Raw_Material(Material):
    def __init__(self):
        pass

class Assembly(Material):
    def __init__(self):
        pass

class Final_Product(Material):
    def __init__(self):
        pass

class Transport:
    self.air : None
    self.motor : None
    self.rail : None
    self.sea : None
