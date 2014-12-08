"""Stage 3
This code returns a new array containing only the strings that do not start with that prefix. """
def main():
    array = ["9803qpzQ","533g34gP","533FoyRC","666LBces","980YkOCy","9805N0Ka"]
    prefix = "533"
    newarray = []
    #checks if item starts with prefix or not. If it starts with prefix, it does not include it in the new array
    for item in array:
      if not item.lower().startswith(prefix):
        newarray.append(item)
    return newarray
main()

