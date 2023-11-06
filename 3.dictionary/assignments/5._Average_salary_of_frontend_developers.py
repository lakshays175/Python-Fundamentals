import nested_dictt 

json_dict = nested_dictt.json_dict

#print(json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"))
# Integers used to calculate the sum of salaries of all the managers
sum=0 
number_of_frontend_developers= 0 

for developer in json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"): 
    for keys,values in developer.items():
        if keys == "Salary": 
            number_of_frontend_developers +=1
            sum+= values

print(f"Average Salary of Frontend Developers are : {sum/number_of_frontend_developers}")


        