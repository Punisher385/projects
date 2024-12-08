my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
    "key6": "value6",
    "key7": "value7",
    "key8": "value8",
    "key9": "value9",
    "key10": "value10"}
my_dict["key2"] = "new_value2"
my_dict["key7"] = "new_value7"
my_dict.pop("key3", None)
my_dict["key4"] = None

print(my_dict)