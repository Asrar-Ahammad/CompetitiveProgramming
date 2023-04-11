''' Practice Question '''
# 1
month = ['January', 'Feburary', 'March','April','May']
expense = [2200, 2350, 2600, 2310, 2190]
# Q1
print('Extra :',expense[1]-expense[0])
# Q2
total = 0
i = 0
while i<3:
    total = expense[i]+total
    i+=1
print('First quater expense :', total)
# Q3
for i in expense:
    if i == 2000:
        print(month[expense.index(i)])
# Q4
month.append('June')
expense.append(1980)
# Q5
expense[month.index('April')] = expense[month.index('April')]+200
print('Expense in April :', expense[month.index('April')])

# 2
heros=['Spider man','Thor','Hulk','Iron man','Captain america']

# Q1
print('length :',len(heros))
# Q2
heros.append('Black panther')
print(heros)
# Q3
heros.remove('Black panther')
heros.insert(3,'Black panther')
print(heros)
# Q4
heros = ['Doctor Strange' if item == 'Thor' or item == 'Hulk' else item for item in heros]
print(heros)
# Q5
heros.sort()
print(heros)