student1 = {
"first_name": "Mehmet Ulas",
"last_name": "Gul",
"index_number": "35422",
"nationality": "Turkish",
"starting_date": " 13-03-2024",
"courses": ["Python", " Object-oriented-programming" , "Algorithms"]
}
student2 = {
"first_name": "Suleyman",
"last_name": "Cakir",
"index_number":"12512"
"nationality": "Turkish",
"starting_date": " 13-03-2024",
"courses": ["Java", "OOP", "Databases"]
}
student3 = {
"first_name": "Polat",
"last_name": "Alemdar",
"index_number": 31931
"nationality": "Turkish",
"starting_date": " 13-03-2024",
"courses":["C++", "Operating systems", "Networking"]
}
students = [student1, student2, student3]
for student in students:
print(f"Name: {student['first_name']} {student{'last_name']}, Index: {student['index_number']}")
