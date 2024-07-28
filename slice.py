def slice(string):

    if string[0] == '"' or string[0] == "'":
        string = string[1:]
    if string[-1] == '"' or string[-1] == "'":
        string = string[:-1]

    return string