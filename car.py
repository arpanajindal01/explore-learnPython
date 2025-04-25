class Car:
    """
    Created a class, and declared a __init__ method inside that,
    which is a constructor and calls it itself,
    as soon as the objects are created and arguments are passed

    """
    wheels = 4                      # wheels here is a class attribute
    def __init__(self, maker, model, year):     # all the three maker, model, and year are the instance attribute,
                                                # we define them only when we initialize the class.
                                                # When we create new instance of the class.
        self.maker = maker
        self.model = model
        self.year = year
