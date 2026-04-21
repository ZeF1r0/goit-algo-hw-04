def total_salary(path):
    total = 0
    count = 0
    try:
        
        with open(path, encoding = 'utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
                

    except FileNotFoundError:
        return 0, 0
    
    except ValueError:
        return 0, 0
    
    average = total / count if count else 0
    return total, average

data = 'E:/python_Projects/goit-algo-hw-04/Task_1/salary.txt'
total, average = total_salary(data)
print(total, average)
