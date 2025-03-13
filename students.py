students = [{'first_name' :'ali' , 'last_name' :'Sam' ,'index_number' :'3728' , 'nationality' : "polish" , 'starting_date' : "01-04-2025",
           'courses' : ["english" , "programming"]}, {'first_name' :'Joe' , 'last_name' :'kan' ,'index_number' :'3758' , 'nationality' : "british" ,
                                                       'starting_date' : "01-04-2025", 'courses' : ["english" , "math"]}, {'first_name' :'rayan' , 'last_name' :'amen' ,'index_number' :'3798' , 'nationality' : "lebnon" , 'starting_date' : "01-04-2025",
           'courses' : ["english" , "arabic","logic"]}]
for student in students:
    print(f"{student['first_name']},{student['last_name']} - Index: {student['index_number']}")

def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
    new_student ={'first_name': first_name , 'last_name' : last_name, 'index_number' : index_number, 'nationality' : nationality, 'starting_date' : starting_date,
           'courses' : courses}
    students.append(new_student)
    #print(f"student {first_name} {last_name}")
add_student('amal', 'kop', '32145', 'american','01-04-2025', ['physics'])
for student in students:
    print(f"{student['first_name']},{student['last_name']} - Index: {student['index_number']}")