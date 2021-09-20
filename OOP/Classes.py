class Dog:

    animal_kind = "canine" # class variable

    def bark(self):
        return "Woof!"


Dog.animal_kind = "dolphin"

fido = Dog()
lassie = Dog()
Matthew = Dog()
Danny = Dog()


fido.animal_kind = "Big Dog"

print(fido.animal_kind)
print(lassie.animal_kind)