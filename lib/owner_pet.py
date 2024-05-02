class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if self.check_pet_type(pet_type):
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            self.get_all_pets(self)
        else:
            raise Exception("Not Applicable")

    def check_pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not in approved Pet Types!')
        else:
            return True       

    @classmethod
    def get_all_pets(cls, pet):
        cls.all.append(pet)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("N/A")
        pet.owner = self
        self.pet_list.append(pet)

    # def get_sorted_pets(self):
    #     print(self.pet_list)
    def get_sorted_pets(self):
        sorted_list  = sorted(self.pets(), key = lambda pet:pet.name)
        return sorted_list
    


        # sorted_pets = sorted(self.pet_list)
        # print(self.pet_list)
