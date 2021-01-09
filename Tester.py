import os
import sys
from inspect import currentframe
from io import StringIO

_VERSION: float = 0.1404
_ON_IOS: bool = 'ios' in sys.platform
_ON_WINDOWS: bool = 'win' in sys.platform and 'dar' not in sys.platform
_DEBUG: bool = False

_USED_PIP: bool = False

if _ON_IOS:
    import console


class CT:
    class Colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    @staticmethod
    def p_warning(message: str, end="\n"):
        if _ON_IOS:
            CT.PrintMsg.pythonista_warning(f"{message}", end)
        else:
            CT.PrintMsg.normal_warning(f"{message}", end)

    @staticmethod
    def p_error(message: str, end="\n"):
        if _ON_IOS:
            CT.PrintMsg.pythonista_error(f"{message}", end)
        else:
            CT.PrintMsg.normal_error(f"{message}", end)

    @staticmethod
    def p_success(message: str, end="\n"):
        if _ON_IOS:
            CT.PrintMsg.pythonista_success(f"{message}", end)
        else:
            CT.PrintMsg.normal_success(f"{message}", end)

    class PrintMsg:

        @staticmethod
        def normal_warning(message, end):
            print(f">> {CT.Colors.WARNING}Warning:{CT.Colors.ENDC} {message}", end=end)

        @staticmethod
        def pythonista_warning(message, end):
            console.set_color()
            print(">> ", end="")
            console.set_color(255, 255, 0)
            print("Warning: ", end="")
            console.set_color()
            print(message, end=end)
            console.set_color()

        @staticmethod
        def normal_error(message, end):
            print(f">> {CT.Colors.FAIL}Error:{CT.Colors.ENDC} {message}", end=end)

        @staticmethod
        def pythonista_error(message, end):
            console.set_color()
            print(">> ", end="")
            console.set_color(255, 0, 0)
            print("Error: ", end="")
            console.set_color()
            print(message, end=end)
            console.set_color()

        @staticmethod
        def normal_success(message, end):
            print(f">> {CT.Colors.OKGREEN}Success:{CT.Colors.ENDC} {message}", end=end)

        @staticmethod
        def pythonista_success(message, end):
            console.set_color()
            print(">> ", end="")
            console.set_color(0, 255, 0)
            print("Success: ", end="")
            console.set_color()
            print(message, end=end)
            console.set_color()


def _current_line():
    return currentframe().f_back.f_lineno


if _ON_WINDOWS:
    try:
        from colorama import init as init_colorama

        init_colorama()
    except ModuleNotFoundError:
        print(">> Warning: Tester needs 'colorama' module to work.")
        print(">> Installing 'colorama' module...\n")

        try:
            from pip._internal import main as pip

            pip(['install', '--user', 'colorama'])

            try:
                from colorama import init as init_colorama

                init_colorama()

                CT.p_success("'colorama' module installed successfully")
                _USED_PIP = True
            except ModuleNotFoundError:
                print(f">> Error: Something went wrong while 'colorama' import Tester [Line {_current_line()}]")
        except:
            print(f">> Error: Something went wrong while 'colorama' import Tester [Line {_current_line()}]")

try:
    import requests
except ModuleNotFoundError:
    CT.p_warning("Tester needs 'requests' module to work.")
    print(">> Installing 'requests' module...\n")

    from pip._internal import main as pip

    pip(['install', '--user', 'requests'])

    try:
        import requests

        CT.p_success("'requests' module installed successfully")
        _USED_PIP = True
    except ModuleNotFoundError:
        CT.p_error(f"Something went wrong while 'requests' import Tester [Line {_current_line()}]y")


class _Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class _TstHandler:
    @staticmethod
    def test_function(function, inputs) -> [str]:
        with _Capturing() as output:
            sys.stdin = StringIO(inputs)
            function()
        return output

    @staticmethod
    def print_result(fr: int, tn: int):
        if fr == 0:
            print(f"Test {tn}: Correct")
            return 0
        else:
            print(f"Test {tn}: Incorrect. One or more cases returned a bad/unexpected result")
            return 1


class _Test1:
    _testResult: [str] = [
        "Hi, my name is Daniel from Spain. I'm 27 years old.",
        "Hi, my name is Fernando from Mexico. I'm 19 years old.",
        "Hi, my name is Sprouth from USA. I'm 16 years old."
    ]
    _testInputs: [str] = ["Daniel\n27\nSpain", "Fernando\n19\nMexico", "Sprouth\n16\nUSA"]
    _finalResult: int = 0
    _testNumber: int = 1

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = _TstHandler.test_function(function, self._testInputs[i])
            if self._testResult[i].lower() in [x.lower() for x in output]:
                self._finalResult += 0
            else:
                self._finalResult += 1

        success = _TstHandler.print_result(self._finalResult, self._testNumber)
        if _DEBUG:
            return success

    @staticmethod
    def test_info():
        print(
            "Write a function that has 3 inputs asking for a name (e.g. 'Daniel'), an age (e.g. '27') and a country ("
            "e.g. 'Spain'). The function has to print a message with the exact following structure 'Hi, my name is ["
            "NAME] from [COUNTRY]. I'm [AGE] years old.'")


class _Test2:
    _testResult: [float] = [
        4.033204557385719,
        6.829905940696578,
        64.44744357483128

    ]
    _testInputs: [str] = [[4, 5], [8, 8], [50, 99]]
    _finalResult: int = 0
    _testNumber: int = 2

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = function(self._testInputs[i][0], self._testInputs[i][1])
            if self._testResult[i] == output:
                self._finalResult += 0
            else:
                self._finalResult += 1

        success = _TstHandler.print_result(self._finalResult, self._testNumber)
        if _DEBUG:
            return success

    @staticmethod
    def test_info():
        print(
            "Write a function that replicates the mathematical function f(x, y) = ∜(x² + y² + (xy/2) * √(x*y³)). 'x' "
            "and 'y' must be arguments of the function, the result must be returned and not printed. Example, "
            "when 'x' is equal to 4 and 'y' is equal to 5, the returned result is '4.033204557385719'")


class _Test3:
    _testResult: [str] = [
        "major",
        "equal",
        "minor"
    ]
    _testInputs: [str] = ["10\n3", "7\n7", "1\n5"]
    _finalResult: int = 0
    _testNumber: int = 3

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = _TstHandler.test_function(function, self._testInputs[i])
            if self._testResult[i].lower() in [x.lower() for x in output]:
                self._finalResult += 0
            else:
                self._finalResult += 1

        success = _TstHandler.print_result(self._finalResult, self._testNumber)
        if _DEBUG:
            return success

    @staticmethod
    def test_info():
        print(
            "Write a function that has two arguments that receive integers. If both values are the same print 'equal' "
            "if the first value is the smallest print 'minor' and if the first value is the highest print 'major'. "
            "E.g: input_1: 10, input_2: 3, prints: 'major'.")


class _Test4:
    _testResult: [str] = [
        "Final price is 461.7",
        "Final price is 21",
        "Final price is 20764.65"
    ]
    _testInputs: [str] = ["130\n27\n34\n51\n223\n48\n0", "7\n7\n7\n0", "100\n450\n320\n324\n23235\n0"]
    _finalResult: int = 0
    _testNumber: int = 4

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = _TstHandler.test_function(function, self._testInputs[i])
            if self._testResult[i].lower() in [x.lower() for x in output]:
                self._finalResult += 0
            else:
                self._finalResult += 1

        success = _TstHandler.print_result(self._finalResult, self._testNumber)
        if _DEBUG:
            return success

    @staticmethod
    def test_info():
        print(
            "Write a function that takes an undefined number of inputs containing a number that represents a price. "
            "An input equal to \"0\" indicates the end of the input process. Sum all the prices and then make the "
            "following:\n\t- If the total price is less than $ 250, NO discount is applied. \n\t- If the total price "
            "is greater than or equal to $ 250 and less than $ 500, a 5% discount is applied.\n\t- If the total price "
            "is greater than or equal to $ 500 and less than $ 1000 a discount of 10% is applied.\n\t- If the total "
            "price is greater than or equal to $ 1000, a 15% discount is applied.\n To finish, print the final price "
            "with the format: \"Final price is [FINAL_PRICE]\"")


class _Test5:
    _testResult: [str] = ["F", "G", "F"]
    _testInputs: [str] = ["PFFPPF", "PFPPPPPPPPPF", "PF"]
    _finalResult: int = 0
    _testNumber: int = 5

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = _TstHandler.test_function(function, self._testInputs[i])
            if self._testResult[i].lower() in [x.lower() for x in output]:
                self._finalResult += 0
            else:
                self._finalResult += 1

        success = _TstHandler.print_result(self._finalResult, self._testNumber)
        if _DEBUG:
            return success

    @staticmethod
    def test_info():
        print(
            "Write a function that has a unique input: a string that contains 'P' and 'F'. 'P' stands for "
            "'Passed' and 'F' stands for 'Failed'. De function must return 'G' (Graduated) if 80% of the "
            "characters in the input are 'P's, if not it must return an 'F' (F). E.g. Input: 'PFFPPF' - Out"
            "put: 'F'"
        )


class _TesterManager:

    @staticmethod
    def get_repo_version():
        """Gets Tester's GitHub repo version"""

        git_version: str = requests.get(
            'https://raw.githubusercontent.com/AOx0/py-ColoTester/master/version.txt').content.decode("utf-8")
        version: str = ""
        for i in git_version:
            if i.isdigit() or i == ".":
                version += i

        return float(version)

    @staticmethod
    def get_tester_ios():
        """Support for Pythonista 3"""

        if _DEBUG:
            file_name = "Tester1.py"
        else:
            file_name = "Tester.py"

        contents = requests.get("https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py").content.decode(
            "utf-8")

        with open(file_name, "w", encoding="utf-8") as f:
            f.seek(0)
            f.write(contents)
            f.truncate()
            f.close()

    @staticmethod
    def get_tester() -> int:
        """Installs / Updates Tester.py"""

        try:
            git_version: float = _TesterManager.get_repo_version()
        except:
            CT.p_error(f"Failed to get GitHub version. Tester [Line {_current_line()}]")
            return 1

        if os.path.exists("Tester.py"):
            is_update = True
        else:
            is_update = False

        if (git_version != _VERSION and git_version > _VERSION) or not is_update:
            is_update: bool

            if is_update:
                CT.p_warning("A new version of Tester is available.")

                print(f">> Updating Tester [v.{_VERSION}] -> [v.{git_version}]...")
            else:
                print(f">> Installing Tester [v.{_VERSION}]")

            if _ON_IOS:
                try:
                    _TesterManager.get_tester_ios()
                    CT.p_success(f"Tester [v.{git_version}] installed successfully!")
                except:
                    CT.p_error(f"Something went wrong while updating Tester [Line {_current_line()}]")
                    return 3  # IOS Update Failed
            else:
                try:
                    if _DEBUG:
                        os.system(
                            "curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o "
                            "Tester1.py")
                    else:
                        os.system(
                            "curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o "
                            "Tester.py")

                    if is_update:
                        CT.p_success(f"Tester update to [v.{git_version}] successfully!")
                    else:
                        CT.p_success(f"Tester [v.{git_version}] installed successfully!")
                except:
                    CT.p_error(f"Something went wrong while updating Tester [Line {_current_line()}]")
                    return 2  # Curl Failed
            
            if not _ON_IOS and not _DEBUG:
                CT.p_warning("Re-running Tester.py...\n")
                os.execv(sys.executable, ['python'] + sys.argv)
        return 0  # Success


class _TesterTesting:

    def __init__(self):
        failed = 0
        failed += _TesterTesting.run_update_test()
        failed += _TesterTesting.run_tests_test()

        if failed == 0:
            CT.p_success("All tests were executed successfully")
        else:
            CT.p_error(f"Failed tests with {failed} errors")

    @staticmethod
    def run_tests_test() -> int:
        import tests as t

        global test1, test2, test3, test4, test5

        failed = 0
        functions = [t.test1, t.test2, t.test3, t.test4, t.test5]
        tests = [test1, test2, test3, test4, test5]
        for testNum in range(len(functions)):
            CT.p_warning(f"Testing 'Test {testNum + 1}' ", end="")
            print(f"with function {functions[testNum]}", end=" | ")
            if tests[testNum].test(functions[testNum]) == 0:
                CT.p_success(f"Test {testNum + 1} successful")
            else:
                CT.p_error(f"Test {testNum + 1} failed")
                failed += 1

        if failed == 0:
            CT.p_success("All Tester.testX.test() tests successful")
            print("")

        return failed

    @staticmethod
    def run_update_test() -> int:
        import platform

        global _VERSION
        _VERSION -= 0.0001

        update_result = _TesterManager.get_tester()
        if update_result == 1:
            CT.p_warning("Failed to get GitVersion (requests may be failing)")
            return 1
        elif update_result == 2:
            CT.p_warning("Failed to use 'curl [LINK] -o Tester.py'. Or CT.PrintMsg Fails")
            return 1
        elif update_result == 3:
            CT.p_warning("Failed to update iOS pythonista 3 version. (requests may be failing)")
            return 1
        else:
            print("")
            CT.p_success(f"Update test in {sys.platform} - {platform.machine()} - Python v{platform.python_version()} "
                         "successful")
            print("")
            return 0


test1 = ""
test2 = ""
test3 = ""
test4 = ""
test5 = ""


def main():
    global _DEBUG
    # Try  to update Tester.py
    _TesterManager.get_tester()

    if len(sys.argv) == 2:
        _DEBUG = sys.argv[1] == "1" or sys.argv[1].lower() == "true"

    # Create test instances
    if __name__ == 'Tester' or _DEBUG:
        global test1, test2, test3, test4, test5

        test1 = _Test1()
        test2 = _Test2()
        test3 = _Test3()
        test4 = _Test4()
        test5 = _Test5()

    # Run tests
    if _DEBUG:
        CT.p_warning("Debug mode running")
        _TesterTesting()


if not _USED_PIP:
    main()
else:
    if not _ON_IOS:
        CT.p_warning("Re-running Tester.py...\n")
        os.execv(sys.executable, ['python'] + sys.argv)
