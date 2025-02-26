
def total_salary(path) :
    salaries = []
    with open(path, 'r') as file :
        for line in file :
            _, salary = line.split(",")
            salaries.append(int(salary))
    return (sum(salaries), sum(salaries) / len(salaries))

print(total_salary('salary.txt'))