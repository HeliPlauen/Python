
dict_data = {
    "a": {"1": ["a1-1", "a1-2", "a1-3"], "2": ["a2-1", "a2-2", "a2-3"], "3": ["a3-1", "a3-2", "a3-3"]}, 
    "b": {"1": ["b1-1", "b1-2", "b1-3"], "2": ["b2-1", "b2-2", "b2-3"], "3": ["b3-1", "b3-2", "b3-3"]},
    "c": {"1": ["c1-1", "c1-2", "c1-3"], "2": ["c2-1", "c2-2", "c2-3"], "3": ["c3-1", "c3-2", "c3-3"]}
}


def get_element(dict_data, keys, count=0):
    if count < len(keys):
        return get_element(dict_data[keys[count]], keys, count + 1)
    return dict_data

gotten_element = get_element(dict_data, ["b", "3", 0])
print(gotten_element)


def get_element_2(dict_data, keys):
    new_dict = dict_data
    for key in keys:
        new_dict = new_dict[key]
    return new_dict

gotten_element_2 = get_element_2(dict_data, ["a", "1", 2])
print(gotten_element_2)