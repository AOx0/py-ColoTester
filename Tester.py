import os
import sys
from inspect import currentframe
from io import StringIO

VERSION: float = 0.1361
ON_IOS: bool = 'ios' in sys.platform
ON_WINDOWS: bool = 'win' in sys.platform and 'dar' not in sys.platform

if ON_IOS:
    import console


class _Cmd:
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

    class PrintMsg:
        @staticmethod
        def normal_warning(message):
            print(f">> {_Cmd.Colors.WARNING}Warning:{_Cmd.Colors.ENDC} {message}")

        @staticmethod
        def pythonista_warning(message):
            console.set_color()
            print(">> ", end="")
            console.set_color(255, 255, 0)
            print("Warning: ", end="")
            console.set_color()
            print(message)
            console.set_color()

        @staticmethod
        def normal_error(message):
            print(f">> {_Cmd.Colors.FAIL}Error:{_Cmd.Colors.ENDC} {message}")

        @staticmethod
        def pythonista_error(message):
            console.set_color()
            print(">> ", end="")
            console.set_color(255, 0, 0)
            print("Error: ", end="")
            console.set_color()
            print(message)
            console.set_color()

        @staticmethod
        def normal_success(message):
            print(f">> {_Cmd.Colors.OKGREEN}Success:{_Cmd.Colors.ENDC} {message}")

        @staticmethod
        def pythonista_success(message):
            console.set_color()
            print(">> ", end="")
            console.set_color(0, 255, 0)
            print("Success: ", end="")
            console.set_color()
            print(message)
            console.set_color()


def current_line():
    return currentframe().f_back.f_lineno


if ON_WINDOWS:
    try:
        from colorama import init as init_colorama

        init_colorama()
    except ModuleNotFoundError:
        print(">> Warning: Tester needs 'colorama' module to work.")
        print(">> Installing 'colorama' module...\n")

        try:
            import pip


            def install(package):
                if hasattr(pip, 'main'):
                    pip.main(['install', package])
                else:
                    pip._internal.main(['install', package])


            install('colorama')
            try:
                from colorama import init as init_colorama

                init_colorama()

                _Cmd.PrintMsg.normal_success("'colorama' module installed successfully")
            except ModuleNotFoundError:
                print(f">> Error: Something went wrong while updating Tester [Line {current_line()}]")
        except:
            print(f">> Error: Something went wrong while updating Tester [Line {current_line()}]")

try:
    import requests
except ModuleNotFoundError:

    if ON_IOS:
        _Cmd.PrintMsg.pythonista_warning("Tester needs 'requests' module to work.")
        print(">> Install 'requests' module with StaSh 'https://github.com/ywangd/stash'\n")
    else:
        _Cmd.PrintMsg.normal_warning("Tester needs 'requests' module to work.")
        print(">> Installing 'requests' module...\n")

        try:
            import pip


            def install(package):
                if hasattr(pip, 'main'):
                    pip.main(['install', package])
                else:
                    pip._internal.main(['install', package])


            install('requests')
            try:
                import requests

                _Cmd.PrintMsg.normal_success("'requests' module installed successfully")
            except ModuleNotFoundError:
                _Cmd.PrintMsg.normal_error(f"Something went wrong while updating Tester [Line {current_line()}]")
        except:
            _Cmd.PrintMsg.normal_error(f"Something went wrong while updating Tester [Line {current_line()}]")

print("\n")


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


class _Test1:
    _testResult: [str] = [
        "Hi, my name is Daniel from Spain. I'm 27 years old.",
        "Hi, my name is Fernando from Mexico. I'm 19 years old.",
        "Hi, my name is Sprouth from USA. I'm 16 years old."
    ]
    _testInputs: [str] = ["Daniel\n27\nSpain", "Fernando\n19\nMexico", "Sprouth\n16\nUSA"]
    _finalResult: int = 0

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = _TstHandler.test_function(function, self._testInputs[i])
            if self._testResult[i].lower() in [x.lower() for x in output]:
                self._finalResult += 0
            else:
                self._finalResult += 1

        if self._finalResult == 0:
            print("Test 1: Correct")
        else:
            print("Test 1: Incorrect. One or more cases returned a bad/unexpected result")

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

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = function(self._testInputs[i][0], self._testInputs[i][1])
            if self._testResult[i] == output:
                self._finalResult += 0
            else:
                self._finalResult += 1

        if self._finalResult == 0:
            print("Test 2: Correct")
        else:
            print("Test 2: Incorrect. One or more cases returned a bad/unexpected result")

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

    def test(self, function):
        for i in range(len(self._testResult) - 1):
            output = _TstHandler.test_function(function, self._testInputs[i])
            if self._testResult[i].lower() in [x.lower() for x in output]:
                self._finalResult += 0
            else:
                self._finalResult += 1

        if self._finalResult == 0:
            print("Test 3: Correct")
        else:
            print("Test 3: Incorrect. One or more cases returned a bad/unexpected result")

    @staticmethod
    def test_info():
        print(
            "Write a function that has two arguments that receive integers. If both values are the same print 'equal' "
            "if the first value is the smallest print 'minor' and if the first value is the highest print 'major'. "
            "E.g: input_1: 10, input_2: 3, prints: 'major'.")


class _UpdateManager:

    @staticmethod
    def get_repo_version():
        git_version: str = requests.get(
            'https://git.io/JLb6c').content.decode("utf-8")
        version: str = ""
        for i in git_version:
            if i.isdigit() or i == ".":
                version += i

        return float(version)

    @staticmethod
    def update_ios():
        """
        Support for Pythonista 3
        """

        contents = requests.get("https://git.io/JLb6G").content.decode(
            "utf-8")
        with open("Tester.py", "w", encoding="utf-8") as f:
            f.seek(0)
            f.write(contents)
            f.truncate()
            f.close()

    @staticmethod
    def update():
        try:
            git_version: float = _UpdateManager.get_repo_version()
        except:
            if ON_IOS:
                _Cmd.PrintMsg.pythonista_error(f"Failed to get GitHub version. Tester [Line {current_line()}]")
            else:
                _Cmd.PrintMsg.normal_error(f"Failed to get GitHub version. Tester [Line {current_line()}]")
            return

        if git_version != VERSION and git_version > VERSION:
            is_update: bool

            if os.path.exists("Tester.py"):
                if ON_IOS:
                    _Cmd.PrintMsg.pythonista_warning("A new version of Tester is available.")
                else:
                    _Cmd.PrintMsg.normal_warning("A new version of Tester is available.")

                print(f">> Updating Tester [v.{VERSION}] -> [v.{git_version}]...")
                is_update = True
            else:
                print(f">> Installing Tester [v.{VERSION}]")
                is_update = False

            if ON_IOS:
                try:
                    _UpdateManager.update_ios()
                    if is_update:
                        _Cmd.PrintMsg.pythonista_success("Tester updated successfully!")
                    else:
                        _Cmd.PrintMsg.pythonista_success("Tester installed successfully!")

                except:
                    _Cmd.PrintMsg.pythonista_error(
                        f"Something went wrong while updating Tester [Line {current_line()}]")
                    return
            else:
                try:
                    os.system(
                        "curl -sS https://git.io/JLb6G -o Tester.py")

                    if is_update:
                        _Cmd.PrintMsg.normal_success("Tester updated successfully!")
                    else:
                        _Cmd.PrintMsg.normal_success("Tester installed successfully!")
                except:
                    _Cmd.PrintMsg.normal_error(f"Something went wrong while updating Tester [Line {current_line()}]")
                    return

            print("\n")


availableTests: [str] = ["test1", "test2", "test3"]

_UpdateManager.update()

if __name__ == 'Tester':
    test1 = _Test1()
    test2 = _Test2()
    test3 = _Test3()
