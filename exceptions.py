try:
    total = 10 + "10"
except(TypeError, ValueError, IndexError):
    print(f"You can't add a string with an integer value")




class CustomError(Exception):
    pass
raise CustomError("Our Custom error message")