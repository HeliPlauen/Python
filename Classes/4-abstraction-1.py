
# Abstraction
class Data:
    def __init__(self, country, name, age, gender, weight, heigh):
        self.__country = country
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__weight = weight
        self.__heigh = heigh
        self.__dict = self.__dictionary()

    @property
    def dict(self):
        return self.__dict

    def __dictionary(self):
        data_as_dict = {}
        data_as_dict["country"] = self.__country
        data_as_dict["name"] = self.__name
        data_as_dict["age"] = self.__age
        data_as_dict["gender"] = self.__gender
        data_as_dict["weight"] = self.__weight
        data_as_dict["heigh"] = self.__heigh
        return data_as_dict

    def show_data(self):
        return f"{self.__country}, {self.__name}, {self.__age}, {self.__gender}, {self.__weight}, {self.__heigh}"


class DataBase:
    def __init__(self):
        self.__elements = [
            Data("Ukraine", "Oleg", 41, "man", 90, 183),
            Data("Ukraine", "Yaroslava", 10, "girl", 45, 164),
            Data("Ukraine", "Liuba", 73, "woman", 60, 160)
        ]

    def read_data(self, critenia:dict):
        searched_data_list = []
        key = list(iter(critenia))[0]  
        for element in self.__elements:
            if element.dict.get(key) == critenia.get(key):
                searched_data_list.append(element)
        for data in searched_data_list:
            print("Choosen data: " + "{" + data.show_data() + "}")

    def write_data(self, element):
        if isinstance(element, Data):
            self.__elements.append(element)
            print("Success!!!")
        else:
            print("Wrong argument!!!")

    def database_show(self):
        print("----------------------------------------------------")
        print(f"The elements list is: " + "{")
        for element in self.__elements:                
            print("     " + "{" + element.show_data() + "}")
        print("}")
        print("----------------------------------------------------")


database = DataBase()
search_parameter = {"age": 41}

database.read_data(search_parameter)
cat = Data("Poland", "Murka", 3, "cat", 3, 20)
database.write_data(cat)
database.database_show()

# database.__elements.append(cat)  - we cannot add new element using __elements!!!
my_future_wife = Data("Litva", "Lenka", 41, "woman", 60, 170)
database.write_data(my_future_wife)
database.database_show()
database.read_data(search_parameter)

search_parameter = {"country": "Ukraine"}
database.read_data(search_parameter)



