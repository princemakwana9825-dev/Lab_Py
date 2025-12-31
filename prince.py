Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 10
print(x)
10

a = 5
print(-a)
-5

p=10
q=5
print(p>q)
True
print(p==q)
False

x = true
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x = true
NameError: name 'true' is not defined. Did you mean: 'True'?
x = chr(true)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = chr(true)
NameError: name 'true' is not defined. Did you mean: 'True'?

x=true
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
 x=5
 
SyntaxError: unexpected indent
y=10
x=5
print(x and y)
10

print(x or y)
5

print(not x)
False


is pass = true
SyntaxError: invalid syntax

Is pass=true
SyntaxError: invalid syntax

is pass=[1,2,3]
SyntaxError: invalid syntax

a=5
b=3
print(a & b)
1

print(a | b)
7

numbers = [1,2,3,4,6]
print(2 in number)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(2 in number)
NameError: name 'number' is not defined. Did you mean: 'numbers'?

numbers = [1,2,3,4,6]
print("2" in numbers)
False

print("5" not in number)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print("5" not in number)
NameError: name 'number' is not defined. Did you mean: 'numbers'?
 print("5 not" in number)
 
SyntaxError: unexpected indent

x=10
y=10
print( x is y)
True

print( x is not y)
False
