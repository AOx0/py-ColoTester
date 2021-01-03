import os
import sys
from inspect import currentframe
from io import StringIO

VERSION: float = 0.1341
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
        "Hola mi nombre es Daniel, tengo 27 años y vengo de España",
        "Hola mi nombre es fernando, tengo 19 años y vengo de méxico",
        "Hola mi nombre es Sprouth, tengo 90 años y vengo de USA"
    ]
    _testInputs: [str] = ["Daniel\n27\nEspaña", "Fernando\n19\nMéxico", "Sprouth\n90\nUSA"]
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
            "Una función que por medio de inputs (3) reciba un nombre [Daniel], una edad [27] y un país de origen ["
            "España] e imprima el mensaje 'Hola mi nombre es [NOMBRE], tengo [EDAD] años y vengo de [PAIS]'.")


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
            "Una función que replique la función matemática f(x, y) = ∜( x² + y² + (xy/2) * √( x * y³ ) ). Ejemplo, "
            "cuando 'x' vale 4 y 'y' vale 5 el resultado que devuelve es '4.033204557385719'")


class _Test3:
    _testResult: [str] = [
        "mayor",
        "iguales",
        "menor"
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
            "Este problema consiste en leer dos valores y escribir si son iguales, si el primero es menor que el "
            "segundo, o si el primero es mayor al segundo. Si son iguales debes imprimir 'iguales', si el primero es "
            "menor debes imprimir 'menor' y si el primero es mayor debes imprimir 'mayor'. Ejemplo: input 1: 10, "
            "input 2: 3, imprime: 'mayor'")


class _UpdateManager:

    @staticmethod
    def get_repo_version():
        git_version: str = requests.get(
            'https://raw.githubusercontent.com/AOx0/py-ColoTester/master/version.txt').content.decode("utf-8")
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

        contents = requests.get("https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py").content.decode(
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
            if ON_IOS:
                _Cmd.PrintMsg.pythonista_warning("A new version of Tester is available.")
            else:
                _Cmd.PrintMsg.normal_warning("A new version of Tester is available.")

            print(f">> Updating Tester v. {VERSION} -> {git_version}...")

            if ON_IOS:
                try:
                    _UpdateManager.update_ios()
                    _Cmd.PrintMsg.pythonista_success("Tester updated successfully!")

                except:
                    _Cmd.PrintMsg.pythonista_error(f"Something went wrong while updating Tester [Line {current_line()}]")
                    return
            else:
                try:
                    os.system(
                        "curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o Tester.py")
                    _Cmd.PrintMsg.normal_success("Tester updated successfully!")
                except:
                    _Cmd.PrintMsg.normal_error(f"Something went wrong while updating Tester [Line {current_line()}]")
                    return


if __name__ == 'Tester':
    _UpdateManager.update()

    test1 = _Test1()
    test2 = _Test2()
    test3 = _Test3()
