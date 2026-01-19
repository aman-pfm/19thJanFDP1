
# print("Aman Kumar Dubey is best person in the world")
# print("Param sir is very helpful in nature..")

class Person:
    def __init__(self,name,department):
        # self.__name=name
        self.name=name
        self.department=department
    
    def get_details(Khud):
        return f"Details \n\nName: {Khud.name} Department: {Khud.department}"


P1= Person("Aman", "CSE")
# print(P1._Person__name)
# print(P1.name)
print(P1.get_details())
