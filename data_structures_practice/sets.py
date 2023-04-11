# Sets are mutable
animals = {'tiger', 'dog', 'elephant', 'lion', 'dog'}
print(animals)
print(len(animals))

mammals = set()
print(mammals)

birds = set(['sparrow', 'crow', 'pegion'])
print(birds)

animals.add('monkey')
print(animals)

new_list = ['Rhino', 'dog', 'crane']
animals.update(new_list,{'dolphins'})
print(animals)

animals.discard('dog') # Remove shows an error if element is not in set. Discard donot show error if element is not in set
print(animals)

# find item in set
print('tiger' in animals)
print('ferret' in animals)
for animal in animals:
    print(animal)

domestic_animal = {'dog', 'cat', 'elephant'}
wild_animal = {'tiger', 'lion', 'elephant'}

new_animals = domestic_animal.union(wild_animal)
new_animals = domestic_animal | wild_animal # Union |
print(new_animals)

new_animals = domestic_animal.intersection(wild_animal)
new_animals = domestic_animal&wild_animal
print(new_animals)

animals.clear()
print(animals)