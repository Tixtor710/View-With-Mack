class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
        # Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        Student.firstName=firstName
        Student.lastName=lastName
        Student.idNumber=int(idNumber)
        Student.scores=scores
        
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(s):
        s1=sum(scores)
        l1=len(scores)
        aveg=s1/l1
        if 100>=aveg<=90:
            return('O')
        elif 80<=aveg<90:
            return('E')
        elif 70<=aveg<80:
            return('A')
        elif 55<=aveg<80:
            return('P')
        elif 40<=aveg<55:
            return('D')
        elif aveg<40:
            return('T')
        else:
            return('Invalid Score') 

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())