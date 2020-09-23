def abbrevName(name):
    y = name.split()
    first_name = y[0]
    last_name = y[1]
    return first_name[0].upper() + "." + last_name[0].upper()
