import nested_dictt 

json_dict = nested_dictt.json_dict

#print(json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"))
# Integers used to calculate the sum of salaries of all the managers
sum=0 
number_of_developers= 0 


for developer in json_dict.get("Employees")[0].get("Developers"): 
    for values in developer.values():
        for salaries in values:
            for keys,values in salaries.items(): 
                if keys == "Salary":
                    sum += values



print(f"Total Salary of Developers are : {sum}")

