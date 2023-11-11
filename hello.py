print("Hello World!")
print("Bananas are great!")
print("I am an integer ", 6)
print("I am a string, ", "Hello Me")
print("I am a float ", 5.5)
print("I am a list of fruits: ['apple', 'orange'] ")
print("""I am a dictionary meaning object,
       for example a dictionary of fruits
       {'orange': 2, 'apple' : 1}""")
print("I am a boolean i.e. 1 or 0 or true or false")

name= "Alice"
age= 30.5
color= ['pink','blue']
years= 2
isStudent= True
def process_personal_info (name,age,color,years,isStudent):
    # i am a dictionary 
    person = {'name': name, 'age': age, 'color': color, 'years': years, 'isStudent': isStudent}
    return person # i am a comment, and i want to say return marks the end of a function

# process_personal_info() --this will error out
print(process_personal_info(name,age,color,years,isStudent))