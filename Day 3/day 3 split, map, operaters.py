Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = input()
harshath
>>> name
'harshath'
>>> type(name)
<class 'str'>
>>> name = input("enter a name")
enter a name harshath
>>> name
' harshath'
>>> age = input("enter a age: ")
enter a age: 23
>>> age
'23'
>>> age = int(input("enter a age: "))
enter a age: 23
>>> age
23
>>> type(age)
<class 'int'>
>>> price = input("enetr a price:")
enetr a price:99.99
>>> price
'99.99'
>>> type(price)
<class 'str'>
>>> price =  float(input("enetr a price:"))
enetr a price:89.89
>>> price
89.89
>>> type(price)
<class 'float'>
>>> venkata narayana swamy harshath
SyntaxError: invalid syntax
>>> "venkata narayana swamy harshath"
'venkata narayana swamy harshath'
>>> "venkata narayana swamy harshath".split()
['venkata', 'narayana', 'swamy', 'harshath']
>>> "venkata narayana swamy harshath".split(',')
['venkata narayana swamy harshath']
"venkata,narayana,swamy,harshath".split(',')
['venkata', 'narayana', 'swamy', 'harshath']
name = input("enter a name: ")
enter a name: venkata narayana swamy harshath
name
'venkata narayana swamy harshath'
name = input("enetr a name")).split()
SyntaxError: unmatched ')'
name = input("enetr a name").split()
enetr a namevenkata narayan swamy harshath
name
['venkata', 'narayan', 'swamy', 'harshath']
num = input("enter a number :")
enter a number :2
3
3
num = input("enter a number :").split()
enter a number :4 5 5 5 5
num
['4', '5', '5', '5', '5']
num = int(input("enter a num :"))
enter a num :2 3 4 5 
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    num = int(input("enter a num :"))
ValueError: invalid literal for int() with base 10: '2 3 4 5 '
num = int(input("enter a num :").split())
enter a num :2 3 4  5 6
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    num = int(input("enter a num :").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
" to correct this we use map
SyntaxError: unterminated string literal (detected at line 1)
" to correct this we use map "
' to correct this we use map '
num = int(map(input("enter a num :").split()))
enter a num :2 3 4 5 6
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    num = int(map(input("enter a num :").split()))
TypeError: map() must have at least two arguments.
num = list(map(int,input("enter a num :").split()))
enter a num :2 3 4 5
num
[2, 3, 4, 5]
num = list(map(float,input("enter a num :").split()))
enter a num :2 3 4 5
num
[2.0, 3.0, 4.0, 5.0]
num = tuple(map(int,input("enter a num :").split()))
enter a num :2 3 45 5
num
(2, 3, 45, 5)
num = tuple(map(float,input("enter a num :").split()))
enter a num :2 3 4 5 6
num
(2.0, 3.0, 4.0, 5.0, 6.0)
names = tuple(input("enetr a number").split())
enetr a number 23 harshath 45
names
('23', 'harshath', '45')
names = set(input("enetr a number").split())
enetr a number harshath venkat swamy
names
{'harshath', 'venkat', 'swamy'}
names = set(map(int,input("enetr a number").split())

            hs
            
SyntaxError: '(' was never closed
names = set(map(int,input("enetr a number").split()))
            
enetr a number2 3 4 5 6 
names
            
{2, 3, 4, 5, 6}
d = eval(input("enetr the input: "))
            
enetr the input: {1:2, 2:3, 4:5}
d
            
{1: 2, 2: 3, 4: 5}
a,b,c = 1,2,3
            
a
            
1
b
            
2
c
            
3





a=b=c=10
            
a
            
10
b
            
10
c
            
10
a = 10
            
b =5
            
a+b
            
15
a-b
            
5
a-b
            
5
a*b
            
50
a/b
            
2.0
a**b
            
100000
a//b
            
2
"comparision operater"
            
'comparision operater'
a >
            
SyntaxError: invalid syntax
a>b
            
True
a<b
            
False
a>=b
            
True
a<=b
            
False
a!=b
            
True
a == b
            
False
"assignment operator"
            
'assignment operator'
a = 30
            
a = a+10
            
a
            
40
a+= 10
            
a
            
50
a -= 10
            
a
            
40
a *= 10
            
a
            
400
a/b
            
80.0
"logiacl"
            
'logiacl'
" and == two things are true is true"
            
' and == two things are true is true'
" or == any one is true is ture"
            
' or == any one is true is ture'
"membership "
            
'membership '

============================================================== RESTART: C:\Users\CH HARSHATH\OneDrive\Desktop\pfs\Day 2.py =============================================================
-----------------personal_deatils----------------
 StudentName = Cheedella Venkata Narayana Swamy Harshath
 Student_ID = CGH2906
Batch_No   = PFS-HYD-050
Email_ID = cheedellaharshath4891@gmail.com
Date_of_Birth = 2002-02-24
Age = 23
Gender = Male
 Blood_Group = B
 City = Guntur
 State = Andhra pradesh
 Student_Phone_Number = +916302215981
Parent_Phone_Number = +916302082700
Github_Link= https://github.com/Harshath14
---------------Educational_Details---------------
 College_Name = centurion university of technology and management
USN_Number = 201801330014
 Qualification = UG (Bachelor Degrees)
 Department = B.Tech - Computer Science (CSE, Cybersecurity, AI & ML, IoT, Cloud Computing, Data Analytics, Data Science)
 Pass_out_Year = 2024
 Graduation_Percentage = 80%
 Arrears = No
 _10th_Pass Year = 2018
 _10th_Percentage = 93%
 _12th_Pass Year = 2016
 _12th_Percentage = 90%
 skills = ['Python', 'Flask', 'HTML', 'CSS', 'Bootstrap', 'Javascript', 'MySQL', 'Aws', 'Jenkins', 'Github', 'Linux', 'Terraform', 'Docker', 'Git']

============================================================== RESTART: C:\Users\CH HARSHATH\OneDrive\Desktop\pfs\Day 2.py =============================================================
-----------------personal_deatils----------------
StudentName = Cheedella Venkata Narayana Swamy Harshath
Student_ID = CGH2906
Batch_No   = PFS-HYD-050
Email_ID = cheedellaharshath4891@gmail.com
Date_of_Birth = 2002-02-24
Age = 23
Gender = Male
Blood_Group = B
City = Guntur
State = Andhra pradesh
Student_Phone_Number = +916302215981
Parent_Phone_Number = +916302082700
Github_Link= https://github.com/Harshath14
---------------Educational_Details---------------
College_Name = centurion university of technology and management
USN_Number = 201801330014
Qualification = UG (Bachelor Degrees)
Department = B.Tech - Computer Science (CSE, Cybersecurity, AI & ML, IoT, Cloud Computing, Data Analytics, Data Science)
Pass_out_Year = 2024
Graduation_Percentage = 80%
Arrears = No
_10th_Pass Year = 2018
_10th_Percentage = 93%
_12th_Pass Year = 2016
_12th_Percentage = 90%
skills = ['Python', 'Flask', 'HTML', 'CSS', 'Bootstrap', 'Javascript', 'MySQL', 'Aws', 'Jenkins', 'Github', 'Linux', 'Terraform', 'Docker', 'Git']
