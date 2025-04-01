def format_value(element):
    if isinstance(element, bool):
        element = str(element).lower()
    elif isinstance(element, type(None)):
        element = 'null'
    else:
        element = element
    return element


def check_if_dic(element):
    return isinstance(element, dict)
