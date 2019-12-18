Python 3.5.2 (default, Oct  8 2019, 13:06:37) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> type(0x10)
<class 'int'>
>>> type(10)
<class 'int'>
>>> type("안녕");
<class 'str'>
>>> "33"
'33'
>>> '33'
'33'
>>> type('3')
<class 'str'>
>>> type("3")
<class 'str'>
>>> sample = "12345"
>>> sample[3]
'4'
>>> sample[-2:]
'45'
>>> type(sample)
<class 'str'>
>>> sample.encode('utf-8')
b'12345'
>>> sample2 = sample.encode('utf-8')
>>> type(sample2)
<class 'bytes'>
>>> colors = [1, 2, 3]
>>> colors.append(4)
>>> type(colors)
<class 'list'>
>>> colors.append("hi")
>>> type(colors)
<class 'list'>
>>> type(colors[2])
<class 'int'>
>>> type(colors[4])
<class 'str'>
>>> colors
[1, 2, 3, 4, 'hi']
>>> colors.index('1)
	     
SyntaxError: EOL while scanning string literal
>>> colors.index('1')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    colors.index('1')
ValueError: '1' is not in list
>>> colors.index(1)
0
>>> colors.append(1)
>>> colors
[1, 2, 3, 4, 'hi', 1]
>>> colors(1, 2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    colors(1, 2)
TypeError: 'list' object is not callable
>>> colors.count(1)
2
>>> colors.index(1, 2)
5
>>> colors.index(1)
0
>>> for (int i =0 ; i < colors.count(1); ++i)
SyntaxError: invalid syntax
>>> sample3  = {1,2,3,"44"}
>>> sample.union(sample)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sample.union(sample)
AttributeError: 'str' object has no attribute 'union'
>>> type(sample3)
<class 'set'>
>>> (a, b) = 1, 2
>>> print(a, b)
1 2
>>> print(b, a)
2 1
>>> a, b = b,a
>>> print(a,b)
2 1
>>> d
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d = dict('a':1, 'b':2, 'c':3)
SyntaxError: invalid syntax
>>> d {'a':1}
SyntaxError: invalid syntax
>>> d = {'a':1}
>>> type(d)
<class 'dict'>
>>> d['b'] = 2
>>> d
{'a': 1, 'b': 2}
>>> for k, v in d.items()
SyntaxError: invalid syntax
>>> for k, v in d.items()	print(k,v)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> for k, v in d.items()
SyntaxError: invalid syntax
>>> for k, v in d.items():
	print(k,v)
	k, v = v,k
	print(k,v)

a 1
1 a
b 2
2 b
>>> d
{'a': 1, 'b': 2}
>>> del d['c']
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    del d['c']
KeyError: 'c'
>>> del d['b']
>>> d
{'a': 1}
>>> d.clear()
>>> d
{}
>>> sampel
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sampel
NameError: name 'sampel' is not defined
>>> sample
'12345'
>>> type(sample)
<class 'str'>
>>> type(sample2)
<class 'bytes'>
>>> type(sample3)
<class 'set'>
>>> sample3
{'44', 2, 3, 1}
>>> colors
[1, 2, 3, 4, 'hi', 1]
>>> for i in colors.count(1) :
	if
	
SyntaxError: invalid syntax
>>> colros
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    colros
NameError: name 'colros' is not defined
>>> colors
[1, 2, 3, 4, 'hi', 1]
>>> type(colors)
<class 'list'>
>>> colors[:]
[1, 2, 3, 4, 'hi', 1]
>>> colors
[1, 2, 3, 4, 'hi', 1]
>>> cp_colors_1 = colors[:]
>>> cp_colors_2 = colors
>>> colors[0] = 2
>>> colors
[2, 2, 3, 4, 'hi', 1]
>>> cp_colors_2
[2, 2, 3, 4, 'hi', 1]
>>> cp_colors_1
[1, 2, 3, 4, 'hi', 1]
>>> id(colors)	id(colors)
SyntaxError: invalid syntax
>>> id(colors)
140632568163016
>>> id(cp_colors_2
   )
140632568163016
>>> id(cp_colors_1)
140632568256328
>>> 
>>> def func_a
SyntaxError: invalid syntax
>>> def func_a :
	
SyntaxError: invalid syntax
>>> def func()
SyntaxError: invalid syntax
>>> def func_a() :
	print("func a is here")
	:
		
SyntaxError: invalid syntax
>>> def func_a():
	print("func_a is here)
	      
SyntaxError: EOL while scanning string literal
>>> def func_a():
	print("func_a is here")
:
	
SyntaxError: invalid syntax
>>> def func_a():
	print("func_a is here")

>>> func_a
<function func_a at 0x7fe7924528c8>
>>> func_a()
func_a is here
>>> func_b = func_a
>>> func_b
<function func_a at 0x7fe7924528c8>
>>> func_b()
func_a is here
>>> type(sample)
<class 'str'>
>>> type(sample1)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    type(sample1)
NameError: name 'sample1' is not defined
>>> type(sample2)
<class 'bytes'>
>>> type(sample3)
<class 'set'>
>>> sample.encode
<built-in method encode of str object at 0x7fe7924518b8>
>>> sample.encode('utf-8')
b'12345'
>>> type(colors)
<class 'list'>
>>> type(cp_colors_1)
<class 'list'>
>>> colors
[2, 2, 3, 4, 'hi', 1]
>>> def change(x) :
	x[0]= 'h'

>>> def change_ins(x)
SyntaxError: invalid syntax
>>> def change_ins(x):
	x = x[:]
	x[0] = 'h'
	return x

>>> colors
[2, 2, 3, 4, 'hi', 1]
>>> change_ins(colors)
['h', 2, 3, 4, 'hi', 1]
>>> colors
[2, 2, 3, 4, 'hi', 1]
>>> change(colors)
>>> colors
['h', 2, 3, 4, 'hi', 1]
>>> 2**3
8
>>> 2*3
6
>>> def f_a(a= 10, b, c = 20) :
	return a + b + c)
SyntaxError: invalid syntax
>>> def sum_a( a= 10, b, c =20):
	return a + b + c
SyntaxError: non-default argument follows default argument
>>> def sum_a(a=10, b=10, c) :
	return a + b + c
SyntaxError: non-default argument follows default argument
>>> def sum_a(a=10, b=20, c=10):
	return (a+b+c)

>>> sum_a(,,,)
SyntaxError: invalid syntax
>>> sum_a(null, null, null)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    sum_a(null, null, null)
NameError: name 'null' is not defined
>>> type(null)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    type(null)
NameError: name 'null' is not defined
>>> type(NULL)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    type(NULL)
NameError: name 'NULL' is not defined
>>> sum_a()
40
>>> sum_a(2)
32
>>> def sum_a(a=10, b=10, c) :
	return (a + b + c)
SyntaxError: non-default argument follows default argument
>>> def sum_a(a, b=10, c) :
	return a + b + c
SyntaxError: non-default argument follows default argument
>>> def sum_a(a, b, c=10) :
	return a + b + c

>>> def sum_a(a, b=30, c=10) :
	return a + b + c

>>> def sum_a(a=10, b, c) :
	return a + b + c
SyntaxError: non-default argument follows default argument
>>> d= {1:10}
>>> d.items()
dict_items([(1, 10)])
>>> d[1]
10
>>> def judge_a(a):
	if a <= 10:
		return print("low")
	elif a == 10:
		return print("same")
	else
	
SyntaxError: invalid syntax
>>> def judge_a(a):
	if a <= 10:
		return print("low")
	elif a == 10:
		return print("same")
	else :
		return print("high")

	
>>> judge_a(20)
high
>>> judge_a("ff")
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    judge_a("ff")
  File "<pyshell#168>", line 2, in judge_a
    if a <= 10:
TypeError: unorderable types: str() <= int()
>>> def judge_a(a):
	if  type(a) == "<class 'str'>" :
		return print("string is in")
	if a <= 10:
		return print("low")
	elif a == 10:
		return print("same")
	else :
		return print("high")

>>> judge_a("hi")
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    judge_a("hi")
  File "<pyshell#171>", line 4, in judge_a
    if a <= 10:
TypeError: unorderable types: str() <= int()
>>> type("hi")
<class 'str'>
>>> def judge_a(a):
	if  type(a) == '<class 'str'>' :
		return print("string is in")
	if a <= 10:
		return print("low")
	elif a == 10:
		return print("same")
	else :
		return print("high")

SyntaxError: invalid syntax
>>> def judge_a(a):
	if  str(type(a))== "<class 'str'>" :
		return print("string is in")
	if a <= 10:
		return print("low")
	elif a == 10:
		return print("same")
	else :
		return print("high")

>>> judge_a("hi")
string is in
>>> type(str(1))
<class 'str'>
>>> type(int("1"))
<class 'int'>
>>> sample = "1000"
>>> sample2 = 234
>>> sample + sample2
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    sample + sample2
TypeError: Can't convert 'int' object to str implicitly
>>> int(sample) + sample2
1234
>>> type(sample)
<class 'str'>
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> help(judge_a)
Help on function judge_a in module __main__:

judge_a(a)

>>> judge_a.__doc__ ="return the range of a"
>>> help(judge_a)
Help on function judge_a in module __main__:

judge_a(a)
    return the range of a

>>> colors
['h', 2, 3, 4, 'hi', 1]
>>> it = iter(colors)
>>> while it :
	print(it.__next___)

Traceback (most recent call last):
  File "<pyshell#195>", line 2, in <module>
    print(it.__next___)
AttributeError: 'list_iterator' object has no attribute '__next___'
>>> pass
>>> 
[DEBUG ON]
>>> judge_a(300)
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> bool(1)
True
b
>>> bool(12)
True
>>> bool(0)
False
>>> bool(0.00000000000000)
False
>>> type(0)
<class 'int'>
>>> type(0.0)
<class 'float'>
>>> type(2/2)
<class 'float'>
>>> type(10 & 10)
<class 'int'>
>>> bool(10& 10)
True
>>> a = 0
>>> if a and 10/a:
	print("ha")
else:
	print("ho")

ho
>>> if a | 10/a:
	print("ha")
else:
	print("ho")

Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    if a | 10/a:
ZeroDivisionError: division by zero
>>> for str in colors :
	print(str)

h
2
3
4
hi
1
>>> for str in colors:
	a, b = str, type(str)
	print a,b
	
SyntaxError: Missing parentheses in call to 'print'
>>> for str in colors:
	a, b = str, type(str)
	print(a,b)

h <class 'str'>
2 <class 'int'>
3 <class 'int'>
4 <class 'int'>
hi <class 'str'>
1 <class 'int'>
# format 함수 사용
>>> def func_format(a, b):
	print("{0} is {1}".format(a,b) )
>>> func_format(1,2)
1 is 2
                 
# (에러) for 문내 타입 체크 부분
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    if str(type(colors[0])) == "<class 'str'>" :
TypeError: 'int' object is not callable
>>> colors
['h', 2, 3, 4, 'hi', 1]
>>> type(colors)
<class 'list'>
>>> def checker_a() :
	for m in colors:
		print(m, type(m))
		if str(type(m)) == "<class 'str'>" :
			print("string in here")
		else :
			continue

>>> checker_a()
>>> 
