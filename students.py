students = [{'first_name' :'ali' , 'last_name' :'Sam' ,'index_number' :'3728' , 'nationality' : "polish" , 'starting_date' : "01-04-2025",
           'courses' : ["english" , "programming"]}, {'first_name' :'Joe' , 'last_name' :'kan' ,'index_number' :'3758' , 'nationality' : "british" ,
                                                       'starting_date' : "01-04-2025", 'courses' : ["english" , "math"]}, {'first_name' :'rayan' , 'last_name' :'amen' ,'index_number' :'3798' , 'nationality' : "lebnon" , 'starting_date' : "01-04-2025",
           'courses' : ["english" , "arabic","logic"]}]
for student in students:
    print(f"{student['first_name']},{student['last_name']} - Index: {student['index_number']}")