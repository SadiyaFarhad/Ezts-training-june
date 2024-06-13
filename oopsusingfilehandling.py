
#Create 5 student object and get data for name usn and marks after that find percentage and grade and store it to th class object.
class Std:
    def __init__(self): 
        self.__USN = None
        self.__Name = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None

    def Std_Input(self):
        self.__Name = input("Enter your Name: ")
        self.__USN = input("Enter Your USN: ")
        for i in range (0,5):
            marks = input(f"Enter Your Marks in Sub{i+1} : ")
            self.__Marks.append(marks)

    def calc_percentage (self):
        sum = 0
        for i in self.__Marks:
            sum = sum + int(i)
        self.__Percentage = (sum/500)*100

    def calc_Grade(self):
        per = float(self.__Percentage)
        if per<=100 and per >=80:
            self.__Grade = "A"
        elif per<80 and per >=60:
            self.__Grade = "B"
        elif per<60 and per >=40:
            self.__Grade = "C"
        elif per<40 and per >=0:
            self.__Grade = "D"
        else: 
            self.__Grade = "Inavlid"

    def print_details(self):
        print("Name: ",self.__Name)
        print("USN : ",self.__USN)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.__Marks[i]}")
        print("Percentage : ", self.__Percentage)
        print("Grade : ", self.__Grade)

    def convert_list(self):
        st_list = [self.__USN,self.__Name,self.__Marks,self.__Percentage,self.__Grade]
        return st_list

    def covert_ob(self,stu_list):
        self.__USN = stu_list[0]
        self.__Name = stu_list[1]
        self.__Marks = stu_list[2]
        self.__Percentage = stu_list[3]
        self.__Grade = stu_list[4]



st1 = Std()

print(type(st1))

st1.Std_Input()

st1.calc_percentage()
st1.calc_Grade()

st1.print_details()

with open("bitm.txt",'wb') as File:
    L=st1.convert_list()
    data = f"{L[0]}|{L[1]}|{L[2][0]},{L[2][1]},{L[2][2]},{L[2][3]},{L[2][4]}|{L[3]}|{L[4]}\n"
    File.write(data.encode())
    File.close()
stu_list=[]

with open("student.txt",'rb') as File:
    data = File.readline().decode('utf-8')
    print(data)
    for i in data.split("|"):
        stu_list.append(i)
    mrks=stu_list[2]
    mrks_list = []
    for i in mrks.split(','):
        mrks_list.append(i)
    stu_list[2]=mrks_list


print(stu_list)
st2=Std()
st2.covert_ob(stu_list)
st2.print_details()
"""
OUTPUT:
<class '__main__.Std'>
Enter your Name: sadiya
Enter Your USN: 3br22cs415
Enter Your Marks in Sub1 : 100
Enter Your Marks in Sub2 : 100
Enter Your Marks in Sub3 : 100
Enter Your Marks in Sub4 : 100
Enter Your Marks in Sub5 : 100
Name:  sadiya
USN :  3br22cs415
Marks in Five Subject are :
Subject 1 = 100
Subject 2 = 100
Subject 3 = 100
Subject 4 = 100
Subject 5 = 100
Percentage :  100.0
Grade :  A
3br22cs415|sadiya|100,100,100,100,100|100.0|A

['3br22cs415', 'sadiya', ['100', '100', '100', '100', '100'], '100.0', 'A\n']
Name:  sadiya
USN :  3br22cs415
Marks in Five Subject are :
Subject 1 = 100
Subject 2 = 100
Subject 3 = 100
Subject 4 = 100
Subject 5 = 100
Percentage :  100.0
Grade :  A
"""