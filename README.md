# py-ColoTester

Python script to give homework/work/tests to anyone learning python, in my case to some friends. 



#### Contents:

1.  [Installation](https://github.com/AOx0/py-ColoTester#installation)
2.  [How it works](https://github.com/AOx0/py-ColoTester#how-it-works)
3.  [Tests](https://github.com/AOx0/py-ColoTester#tests)
     1.  [Tester.test1](https://github.com/AOx0/py-ColoTester#testertest1)
     2.  [Tester.test2](https://github.com/AOx0/py-ColoTester#testertest2)
     3.  [Tester.test3](https://github.com/AOx0/py-ColoTester#testertest3)



## Installation

Availabe for `Linux` /` Windows` / `MacOs` for `Python 3.x +`



#### Linux 

To install the Tester `curl` is necessary. In `Linux` you can install it with:

```
sudo apt install curl
```



#### Installation

 To install the Tester **go to the path where your learning folder with all your .py files is and write the command** in your cmd / terminal / shell

```bash
curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o Tester.py
```

*NOTE*: *If you know how imports work then write the command at any path and make sure to import Tester correctly on your python files.*



## How it works

1.  You are given a series of tasks (tests). Each test has a small explanation, the rules and requisites your function must follow, and an example of the inputs and outputs or arguments and return you should get. With this information, you have to write a function (like you want) that fullfills all requisites.
2.  When you think your function is ready it's time to test it. When testing, `Tester` gives various inputs/arguments that are already verified and checks that all outputs/returns are correct, with this method you have to make real code.

*NOTE: Every time you use Tester in your files it's going to try to update itself. If any module is missing for it to work it will also install the module automatically.*



## How to use

1.  Import `Tester` in any python file **inside the folder where you used the installation command** and access to the Tester's `test` you want.

```python
import Tester

Tester.test1.test_info() 
# Prints:
# Una función que por medio de inputs (3) reciba un nombre [Daniel], una edad [27] y un país de origen [España] e imprima el mensaje 'Hola mi nombre es [NOMBRE], tengo [EDAD] años y vengo de [PAIS]' 
```



2.  Read the test explanation with `test_info()` and code a function that makes what the explanation is asking. Example:

```python
import Tester

def testAttempt():
    name = input("Write a name:\n")
    age = input("Write an age:\n")
    country = input("Write a country:\n")

    print(f"Hi, my name is {name} from {country}. I'm {age} years old.")

```



3.  Once you have finished programming a function that fulfills `test_info()` requirements, you need to *"submit"* it for the `Tester` to evaluate it. You can do it like in the following example:

```python
import Tester

def testAttempt():
    name = input("Write a name:\n")
    age = input("Write an age:\n")
    country = input("Write a country:\n")

    print(f"Hi, my name is {name} from {country}. I'm {age} years old.")
 
Tester.test1.test(testAttempt) # Prints: 'Test 1: Correct'

```

Specifically, to test your functions you need to follow the next formula: `Tester.testX.test(functionName)`





## Tests

This section contains all tests, it's requirements, instructions and examples from  `Tester`.

Remember:

-   `Tester.testX.test_info()` : Prints the `testX` instructions. Replace the `X` in`testX`  with a number to acces to an actual test.
-   `Tester.testX.test(function)` : `Tester` makes tests on the `function` you *"submit"* by passing the name of the fuction as an argument to the `testX.test()` method.



 <br />

##  `Tester.test1`

 <br />

#### `Tester.test1.test_info()`

 Write a function that has 3 inputs asking for a `name` (e.g. 'Daniel'), an `age` (e.g. '27') and a `country` (e.g. 'Spain'). The function has to print a message with the exact following structure **'Hi, my name is `name` from `country`. I'm `age` years old.'**



| Input                     | Output                                              |
| ------------------------- | --------------------------------------------------- |
| Daniel<br />27<br />Spain | Hi, my name is Daniel from Spain. I'm 27 years old. |

As always, to test your function pass it's name as an argument to `Tester.test1.test()`. E.g. `Tester.test1.test(myFunctionName)`

 <br />

##  `Tester.test2`

 <br />

#### `Tester.test2.test_info() `

Write a function that replicates the mathematical function `f(x, y) = ∜(x² + y² + (xy/2) * √(x*y³))`. 

*x* and *y* must be arguments of the function, the result must be returned and not printed. E.g. when *x* is equal to 4 and *y*  is equal to 5, the returned result is *4.033204557385719*




| Arguments         | Returns           |
| ----------------- | ----------------- |
| x = 4,<br />y = 5 | 4.033204557385719 |

As always, to test your function pass it's name as an argument to `Tester.test2.test()`. E.g. `Tester.test2.test(myFunctionName)`

 <br />

## `Tester.test3`

 <br />

#### `Tester.test3.test_info() `

Write a function that has two inputs that are supposed to receive `int`. If both of the stored input values are the same print *"equal"*, if the first value is the smallest print *"minor"* or if the first value is the highest print *"major"*. E.g: input_1 = "10", input_2 = "3", prints: *"major"*.




| Input     | Output |
| --------- | ------ |
| 10<br />3 | major  |

As always, to test your function pass it's name as an argument to `Tester.test3.test()`. E.g. `Tester.test3.test(myFunctionName)`



