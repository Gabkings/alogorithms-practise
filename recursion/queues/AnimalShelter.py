class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def __str__(self):
        dogs = [str(x) for x in self.dogs]
        cats = [str(x) for x in self.cats]

        return "Dog ".join(dogs) +"\n "+"cat ".join(cats)

    def enqueue(self, animal, type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequeueAny(self):
        if len(self.dogs) == 0:
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)
    
    def dequeueCat(self):
        if len(self.cats) is not 0:
            return self.cats.pop(0)
        return None
    
    def dequeueDog(self):
        if len(self.dogs) is not 0:
            return self.dogs.pop(0)
        return None

sampleShelter = AnimalShelter()
sampleShelter.enqueue(1, "Cat")
sampleShelter.enqueue(2, "Cat")
sampleShelter.enqueue(3, "Cat")
sampleShelter.enqueue(2, "Dog")
sampleShelter.enqueue(3, "Dog")
print(sampleShelter)

print(sampleShelter.dequeueAny())
print(sampleShelter)