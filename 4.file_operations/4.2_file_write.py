"""    
    "w" mode                    : overwrite the file
    "a" mode                    : append the file
    "x" mode                    : creates a new file but if the file already exists it doesn't overwrite it or append it
    "os.remove()"               : removes the file in the path specified 
    "os.rmdir()"                : removes the directory in the path which are empty 
    os.path.exists(file_name)   : check if the file exists or not 
"""

"""
writer = open("4.file_operations/lecture.txt","w")
writer.write("This is a demo file\n")


appender = open("4.file_operations/lecture_output_append.txt","a")
appender.write("This is a demo file which appends data\n ")
"""

students = ["bhanu","krishna","jatin","lakshay"]

"""
for student in students:
    file_name = f"4.file_operations/{student}.txt"
    file_writer = open(file_name,"w")
    file_writer.write(f"{student} is awesome")
    file_writer.close()

"""
"""
students_characterstics = {
    "bhanu": "reporter",
    "sudheer": "tester",
    "jatin": "etl developer",
    "lakshay": "etl developer",
    "krishna": "tester"}


num =1 
for student, domain in students_characterstics.items():
    file_name = f"4.file_operations/developers.txt"
    message = f"{num}. {student} is a {domain}!\n"
    with open(file_name,"a") as writer: 
        writer.write(message)
    num +=1
"""

"""
creator = open("4.file_operations/dummys.txt","x")
creator.close()
"""
