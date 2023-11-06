import nested_dictt 

json_dict = nested_dictt.json_dict

#print(json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"))
# Integers used to calculate the sum of salaries of all the managers
sum=0
number_of_employees = 0 

for manager in json_dict.get("Employees")[0].get("Managers"): 
    for classes,values in manager.items():
        if classes == "L1":
            for salaries in values:
                if salaries.get("Name")[0].lower() in 'aeiou':  
                    for names,salary in salaries.items(): 
                        if names == "Salary": 
                            number_of_employees += 1 
                            sum += salary
        if classes in("L2","L3"): 
            if values.get("Name")[0].lower() in 'aeiou':
                for name,salary in values.items(): 
                    if name == "Salary":
                        number_of_employees += 1 
                        sum += salary

for developer in json_dict.get("Employees")[0].get("Developers"): 
    for values in developer.values():
        for salaries in values:
            if salaries.get("Name")[0].lower() in 'aeiou':
                for keys,values in salaries.items(): 
                    if keys == "Salary":
                        number_of_employees += 1
                        sum += values


print(f"Average Salary of Employees are : {sum}")

