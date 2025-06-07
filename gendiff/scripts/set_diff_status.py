from ..formatters.format_value import check_if_dic


def set_recursive(dict):
    dictionary = {}
    status = 'untouched'
    children = []
    if check_if_dic(dict):
        for key in dict:
            val = dict[key]
            if check_if_dic(val):
                status = 'nested'
                children.append(set_recursive(val))
                value = {
                    'status': status,
                    'children': children}
                dictionary[key] = value
            else:
                status = 'untouched'
                old_value = dict[key]
                new_value = None
                value = {
                    'status': status,
                    'old_value': old_value,
                    'new_value': new_value}
                dictionary[key] = value
    children = []
    return dictionary


def set_status(dic1,
               dic2,
               deepnees=0):  # noqa: C901
    list1 = sorted(list(set(list(dic1.keys()) + list(dic2.keys()))))
    dictionary = {}
    children = []
    children_main = []
    if deepnees == 0:
        status = 'root'
        key = 'root'
        children_main.append(
            set_status(
                dic1,
                dic2,
                deepnees=deepnees + 1))
        value = {
            'status': status,
            'children': children_main}
        dictionary[key] = value
        return dictionary
    else:
        for key in list1:
            # если ключ в словаре1 и его значение - словарь, 
            # или если ключ в словаре2 и его значение - словарь
            if (key in dic1 and check_if_dic(dic1[key]) 
                or key in dic2 and check_if_dic(dic2[key])):
                # если ключ в словаре1, но не в словаре2
                if key in dic1 and key not in dic2:
                    status = 'removed_dic'
                    children.append(set_recursive(dic1[key]))
                    value = {
                        'status': status,
                        'children': children}
                # если ключ в словаре2, но не словаре1
                elif key in dic2 and key not in dic1:
                    status = 'added_dic'
                    children.append(set_recursive(dic2[key]))
                    value = {
                        'status': status,
                        'children': children}
                # если ключ в словаре1 и словаре2, 
                # где 1 из случаев - его значение - не словарь
                elif (key in dic1 and key in dic2 
                      and not check_if_dic(dic1[key])
                      or not check_if_dic(dic2[key])):
                    status = 'changed'
                    old_value = dic1[key]
                    new_value = dic2[key]
                    if check_if_dic(dic1[key]):
                        status = 'untouched_dic'
                        children.append(set_recursive(dic1[key]))
                        old_value = {
                            'status': status,
                            'children': children}
                    elif check_if_dic(dic2[key]):
                        status = 'untouched_dic'
                        children.append(set_recursive(dic2[key]))
                        new_value = {
                            'status': status,
                            'children': children}
                    status = 'changed'
                    value = {
                        "status": status,
                        "old_value": old_value,
                        "new_value": new_value}
                    children = []
                else:
                    status = 'nested'
                    if key in dic1 and check_if_dic(dic1[key]):
                        if key in dic2 and check_if_dic(dic2[key]):
                            children.append(set_status(
                                dic1[key],
                                dic2[key],
                                deepnees=deepnees + 1))
                        else:
                            children.append(set_status(
                                dic1[key],
                                {},
                                deepnees=deepnees + 1))
                    elif key not in dic1:
                        if key in dic2 and check_if_dic(dic2[key]):
                            children.append(set_status(
                                {}, 
                                dic2[key],
                                deepnees=deepnees + 1))
                    value = {
                        'status': status,
                        'children': children}
                dictionary[key] = value
                children = []
            else:
                if key not in dic1:
                    status = 'added'
                    old_value = None
                    new_value = dic2[key]
                elif key not in dic2:
                    status = 'removed'
                    old_value = dic1[key]
                    new_value = None
                elif dic1[key] != dic2[key]:
                    status = 'changed'
                    old_value = dic1[key]
                    new_value = dic2[key]
                    if check_if_dic(dic1[key]):
                        if check_if_dic(dic2[key]):
                            old_value = set_status(dic1[key],
                                                   dic2[key],
                                                   deepnees=deepnees + 1)
                            new_value = set_status(dic2[key],
                                                   dic1[key],
                                                   deepnees=deepnees + 1)
                else:
                    status = 'untouched'
                    old_value = dic1[key]
                    new_value = None
                value = {
                    "status": status,
                    "old_value": old_value,
                    "new_value": new_value}
                dictionary[key] = value
    return dictionary
