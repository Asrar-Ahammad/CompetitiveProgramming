person = {'Name':'Linus', 
          'Age':21}
print(person)

print(person['Age'])

print(person.get('Hobbies'))

print(person.get('Hobbies', ['Swimming', 'coding']))
print(person)

person['Name'] = 'Denis'
print(person)

person['Hobbies'] = ['Swimming', 'coding']
print(person)

print(person.pop('Name'))
print(person)

person1 = {}
print(type(person1))

for a in person:
    print(a)
    print(person[a])
