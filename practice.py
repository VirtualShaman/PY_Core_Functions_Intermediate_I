x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] = 15
print(x)

# 2) Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# 3) In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 4) Change the value 20 in z to 30
z[0]['y'] = 30
print(z)



# Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
#     for j in(0,2):
#         print(students.keys[j])

def iterateDictionary():
    for i in range(0,len(students)):
        for j in students[i]:
            print(f"this is j:{j}")
            print(students[i][j])
iterateDictionary()

# should output: (it's okay if each key-value pair ends up on 2 separate lines;

# Get Values From a List of Dictionaries

# def iterateDictionary2(key_name, some_list):

def iterateDictionary2(key,dictName):
    for i in range(0,len(dictName)):
        print(dictName[i][key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dictName):
    for key in dictName:
        print(key,len(dictName[key]))
        for j in range(0,len(dictName[key])):
            print(dictName[key][j])


printInfo(dojo)
