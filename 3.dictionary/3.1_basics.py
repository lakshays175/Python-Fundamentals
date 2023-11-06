# demo_dict = {
#     "data": ["ram","krishna","bhanu"]
# }

# list_data = demo_dict.get("data")

# #for item in list_data:
#     #print(item.upper()[0])

# """
# demo_dict2 = {
#     "data": [
#         {"name":"ram"},
#         {"name":"krishna"},
#         {"name":"bhanu"}
#     ]
# }

# output_list =demo_dict2.get("data")
# for item in output_list:
#     #print(item.get("name"))
#     #print(item)
# """

# emp_data = {
#     "data": [
#         {
#             "name":"ram",
#             "salary":100
#         },
#         {
#             "name":"krishan",
#             "salary":400
#         },
#         {
#             "name":"lakshay",
#             "salary":500
#         }
#     ]
# }

# output_list = emp_data.get("data")
# #print(output_list[0])
# sum=0
# for emp in output_list:
#     #print(emp["salary"])
#     if emp["name"] != "krishan":
#         sum+= emp["salary"]

# #print(sum)

team_india = {
    "data": [
        {"name": "Virat",
         "runs": 120},

        {"name": "Dhoni",
         "runs": 100},
        {"name": "Pandya",
         "runs": 70}
    ]
}

for century in team_india["data"]:
   # print(century["name"])
    if century["runs"] >= 100:
        print(century["name"])
