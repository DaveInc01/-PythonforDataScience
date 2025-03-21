def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}

    ft_list[1] = "World!"

    tuple_2 = ("Hello", "Armenia!")
    ft_tuple = tuple_2
    ft_set2 = {"Hello", "Yerevan!"}
    ft_set = ft_set2
    ft_dict["Hello"] = "42Yerevan!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()


