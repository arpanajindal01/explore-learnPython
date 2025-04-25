def example_function():
    """ Variable with a local scope
    is only accessible inside a function
    where it is actually defined """

    local_var = "I am a local variable"
    print(f"Inside the example_function: {local_var}")


example_function()

global_var = "I am a global variable"
print(f"Before the global variable value is modified: {global_var}")

def global_variable_example_function():
    """ A Global variable can be accessed
    anywhere in the file, to modify the value
    of the global variable across the file and not
    in a specific function or place we use the
    keyword "global" in front of  the variable
    to assign new value to the variable globally """

    global global_var
    global_var = "I am modified global variable"
    print(f"Inside the global variable example function: {global_var}")


global_variable_example_function()
print(f"Outside the global variable example function: {global_var}")
