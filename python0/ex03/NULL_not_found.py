def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print("Nothing: None <class 'NoneType'>")
            return(0)
        case float():
            print("Cheese: nan <class 'float'>")
            return(0)
        case "":
            print("Empty: <class 'str'>")
            return(0)
        case False:
            print("Fake: False <class 'bool'>")
            return(0)
        case 0:
            print("Zero: 0 <class 'int'>")
            return(0)
        case _:
            print("Type not Found")
    return 1