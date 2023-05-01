def average(salary):
    if len(salary) == 1:
        return salary[0]
    if len(salary)>=2:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/len(salary)

salary = [4000,3000,1000,2000]
print(average(salary))