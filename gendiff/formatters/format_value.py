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


def transform_var_json(element):
    three_horsemen = ['true', 'null', 'false']
    element = format_value(element)
    if isinstance(element, str):
        if len(element) > 0:
            if (element.endswith('"') and element.startswith('"') 
                or element.endswith("'") and element.startswith("'") 
                or element in three_horsemen):
                element = element    
            else:
                element = f'"{element}"'
        elif len(element) < 1:
            element = f'"{element}"'
        else: 
            element = element
    return element
