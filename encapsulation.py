class Encapsulation:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    @property
    def method_to_access_private(self):
        return self.__private

    @method_to_access_private.setter
    def method_to_access_private(self, value):
        self.__private = value


encapsulated_object = Encapsulation()
print(encapsulated_object.public)
print(encapsulated_object._protected)
print(encapsulated_object.method_to_access_private)

encapsulated_object.method_to_access_private = "I am a modified private value"
print(encapsulated_object.method_to_access_private)
