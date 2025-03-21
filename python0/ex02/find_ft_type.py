def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            print("List : <class 'list'>")
        case tuple():
            print("Tuple : <class 'tuple'>")
        case set():
            print("Set : <class 'set'>")
        case dict():
            print("Dict : <class 'dict'>")
        case str():
            print(f"{object} is in the kitchen : <class 'str'>")
        case _:
            print("Type not found")
    return 42