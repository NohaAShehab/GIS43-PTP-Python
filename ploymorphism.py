

### overloading  ((no explicit overlaoding))  ### install package dispatch
#
# ## overriding

class Person:
    def speak(self):
        print("I am a person ")

class Engineer(Person):
    # def speak(self):
    #     super().speak()
    #     print("I am an engineer ")
    # def speak(self,message):
    #     super().speak()
    #     print(f"I am an engineer {message}")
    pass
e = Engineer()
e.speak()