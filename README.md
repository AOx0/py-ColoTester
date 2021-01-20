# py-ColoTester

Python script to give homework/work/tests to anyone learning python, in my case to some friends. Made for `Python 3.X`+



#### Contents:

-   [Installation](https://github.com/AOx0/py-ColoTester#installation)

-   [How it works](https://github.com/AOx0/py-ColoTester#how-it-works)

-   [Tests](https://github.com/AOx0/py-ColoTester#tests)
    -   [Tester.test1](https://github.com/AOx0/py-ColoTester#testertest1)
    -   [Tester.test2](https://github.com/AOx0/py-ColoTester#testertest2)
    -   [Tester.test3](https://github.com/AOx0/py-ColoTester#testertest3)
    -   [Tester.test4](https://github.com/AOx0/py-ColoTester#testertest4)
    -   [Tester.test5](https://github.com/AOx0/py-ColoTester#testertest5)



## Installation



### Requirements

#### pip

Ubuntu:

```
sudo apt intall python3-pip
```



#### curl

Ubuntu:

```
sudo apt install curl
```



#### requests

To intsall `requests` module use `pip`

```shell
python -m pip install requests
```



### Installation

Then run the following code with python:

```python
import requests as r;exec(r.get("https://raw.githubusercontent.com/AOx0/py-ColoTester/SiteImp/Tester.py").content)
```



## How it works

1.  You are given a series of tasks (tests). Each test has a small explanation, the rules and requisites your function must follow, and an example of the inputs and outputs or arguments and return you should get. With this information, you have to write a function (like you want) that fullfills all requisites.
2.  When you think your function is ready it's time to test it. When testing, `Tester` gives various inputs/arguments that are already verified and checks that all outputs/returns are correct, with this method you have to make real code.

*NOTE: Every time you use Tester in your files it's going to try to update itself. If any module is missing for it to work it will also try install the module automatically.*



## How to use



### Importing Tester

1.  Import `Tester` and access to the `test` you want.

```python
from Tester import Tester

Tester.test1.test_info() 
# Prints:
# Write a function that has 3 inputs asking for a name (e.g. 'Daniel'), an age (e.g. '27') and a country
# (e.g. 'Spain'). The function has to print a message with the exact following structure 'Hi, my name is
# [NAME] from [COUNTRY]. I'm [AGE] years old.' 
```



2.  Read the test explanation with `test_info()` and code a function that makes what the explanation is asking. Example:

```python
from Tester import Tester

def testAttempt():
    name = input("Write a name:\n")
    age = input("Write an age:\n")
    country = input("Write a country:\n")

    print(f"Hi, my name is {name} from {country}. I'm {age} years old.")

```



3.  Once you have finished programming a function that fulfills `test_info()` requirements, you need to *"submit"* it for the `Tester` to evaluate it. You can do it like in the following example:

```python
from Tester import Tester

def testAttempt():
    name = input("Write a name:\n")
    age = input("Write an age:\n")
    country = input("Write a country:\n")

    print(f"Hi, my name is {name} from {country}. I'm {age} years old.")
 
Tester.test1.test(testAttempt) # Prints: 'Test 1: Correct'

```

Specifically, to test your functions you need to follow the next formula: `Tester.testX.test(functionName)`



### Using @Test.XXXX decorator

Just add the decorator like `@Test.One`,  `@Test.Two`, `@Test.Three`, etc. to the function you want. The syntax is `@Test.[NUMBER]`

```python
from Tester import Test

@Test.One
def testAttempt():
    name = input("Write a name:\n")
    age = input("Write an age:\n")
    country = input("Write a country:\n")

    print(f"Hi, my name is {name} from {country}. I'm {age} years old.")
 
testAttempt() # Prints: 'Test 1: Correct'
```

The decorator automatically tests the function you add the decorator to. 

## Tests

This section lists all `Tester` tests and their info (requirements, instructions and i/o examples).

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

<br />

## `Tester.test4`

 <br />

#### `Tester.test4.test_info() `

Write a function that takes an undefined number of inputs containing a number (`int`) that represents a price. An input equal to "0" indicates the end of the input process. Sum all the prices and then make the following:

	-	If the total price is less than $ 250, NO discount is applied.
	-	If the total price is greater than or equal to $ 250 and less than $ 500, a 5% discount is applied.
	-	If the total price is greater than or equal to $ 500 and less than $ 1000 a discount of 10% is applied.
	-	If the total price is greater than or equal to $ 1000, a 15% discount is applied.

To finish, print the final price with the format: **"Final price is `FINAL_PRICE`"**




| Input                                               | Output               |
| --------------------------------------------------- | -------------------- |
| 130<br />27<br />34<br />51<br />223<br />48<br />0 | Final price is 461.7 |

As always, to test your function pass it's name as an argument to `Tester.test4.test()`. E.g. `Tester.test4.test(myFunctionName)`



<br />

## `Tester.test5`

 <br />

#### `Tester.test5.test_info() `

"Write a function that has a unique input: a string that contains 'P' and 'F'. 'P' stands for 'Passed' and 'F' stands for 'Failed'. De function must return 'G' (Graduated) if 80% of the characters in the input are 'P's, if not it must return an 'F' (F).\nE.g. Input: 'ARRAAR' - Output: 'F'"




| Input  | Return |
| ------ | ------ |
| ARRAAR | F      |

As always, to test your function pass it's name as an argument to `Tester.test5.test()`. E.g. `Tester.test5.test(myFunctionName)`





