# py-ColoTester

Repo dedicated to creating a python script to give homework/work/tests to anyone who is learning python. 



## Installation

Availabe for `Linux` /` Windows` / `MacOs` for `Python 3.x +`

 To install the Tester **go to the path where your learning folder is** **and** **write the command** in your Cmd / terminal / shell

```bash
curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o Tester.py
```

*NOTE*: *If you know how imports work then write the command at any path and make sure to import Tester correctly on your python files.*



## How it works

1.  You are given a series of tasks (tests). Each test has a small explanation, the rules and requisites your function must follow, and an example of the inputs and outputs you should get. With this information, you have to write a function (like you want) that follows all requisites.
2.  When you think you're done it's time to test the function. When testing, Tester gives various inputs and parameters that are already verified and checks that all outputs are correct, with this method you have to make real Programmation.

*NOTE: Every time you use Tester in your files it's gonna look and try to update himself. If any module is missing for it to work it will also install that automatically.*



## How to use

1.  Import `Tester` in any python file **inside the folder where you used the installation command** and access to the Tester's `test` you want.

```python
import Tester

Tester.test1.printTest() 
# Prints:
# Una función que por medio de inputs (3) reciba un nombre [Daniel], una edad [27] y un país de origen [España] e imprima el mensaje 'Hola mi nombre es [NOMBRE], tengo [EDAD] años y vengo de [PAIS]' 
```



2.  Read the test rules / explanations and code what the test is asking for. Example:

```python
import Tester

def test1():
  nombre = input("Ingresa un nombre\n")
  edad = input("Ingresa una edad\n")
  pais = input("Donde naciste?\n")
  
  print(f"Hola mi nombre es {nombre}, tengo {edad} años y vengo de {pais}")
```



3.  Once you have finished programming the function the test's instructions asked for it's time to test it. You can do it like in the following example:

```python
import Tester

def testAttepmt():
  nombre = input("Ingresa un nombre\n")
  edad = input("Ingresa una edad\n")
  pais = input("Donde naciste?\n")
  
  print(f"Hola mi nombre es {nombre}, tengo {edad} años y vengo de {pais}")
 
Tester.test1.test(testAttepmt) # Prints: 'Test 1: Correct'
```

Specifically, to test your functions you need to follow the next formula:

```python
Tester.test[number].test([function])
```



