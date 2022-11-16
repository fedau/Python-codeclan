class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def return_occupation(self):
        return self.occupation



class Teacher(Person):
    def __init__(self, name, occupation, subject):
        super().__init__(self, name, occupation)
        self.subject = subject


# # composition over inheritance
# prefer to give class properties and behavior 
# i would rather have a vehicle class with make and model and engine
# but it would be more preferable to have an engine class
# make engine an instance of vehicle 
# use inheritance when something is so a motorbik is a vehicle
# composition is when something has an engine so a vehicle has an engine
