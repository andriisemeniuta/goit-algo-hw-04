def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1
                
        if count != 0:
            average = total / count
        else:
            average = 0
        return total, average
        
    except FileNotFoundError:
        return 0, 0
