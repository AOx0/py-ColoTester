import os
import sys
import subprocess

from inspect import currentframe
from io import StringIO


class Tester:
    class __Test:

        def __init__(self, debug: bool):
            self._debug = debug

        def _test_function(self, function, inputs) -> [str]:
            with self._Capturing() as output:
                sys.stdin = StringIO(inputs)
                function()
            return output

        @staticmethod
        def _print_result(fr: int, tn: int):
            if fr == 0:
                print(f"Test {tn}: Correct")
                return 0
            else:
                print(f"Test {tn}: Incorrect. One or more cases returned a bad/unexpected result")
                return 1

        class _Capturing(list):
            def __enter__(self):
                self._stdout = sys.stdout
                sys.stdout = self._stringio = StringIO()
                return self

            def __exit__(self, *args):
                self.extend(self._stringio.getvalue().splitlines())
                del self._stringio
                sys.stdout = self._stdout

    class __Test1(__Test):
        _testResult: [str] = [
            "Hi, my name is Daniel from Spain. I'm 27 years old.",
            "Hi, my name is Fernando from Mexico. I'm 19 years old.",
            "Hi, my name is Sprout from USA. I'm 16 years old."
        ]
        _testInputs: [str] = ["Daniel\n27\nSpain", "Fernando\n19\nMexico", "Sprout\n16\nUSA"]
        _finalResult: int = 0
        _testNumber: int = 1

        def test(self, function):
            for i in range(len(self._testResult) - 1):
                output = self._test_function(function, self._testInputs[i])
                if self._testResult[i].lower() in [x.lower() for x in output]:
                    self._finalResult += 0
                else:
                    self._finalResult += 1

            success = self._print_result(self._finalResult, self._testNumber)
            if self._debug:
                return success

        @staticmethod
        def test_info():
            print(
                "Write a function that has 3 inputs asking for a name (e.g. 'Daniel'), an age (e.g. '27') and a "
                "country (e.g. 'Spain'). The function has to print a message with the exact following structure 'Hi, "
                "my name is [NAME] from [COUNTRY]. I'm [AGE] years old.'")

    class __Test2(__Test):
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

            success = self._print_result(self._finalResult, self._testNumber)
            if self._debug:
                return success

        @staticmethod
        def test_info():
            print(
                "Write a function that replicates the mathematical function f(x, y) = ∜(x² + y² + (xy/2) * √(x*y³)). "
                "'x' and 'y' must be arguments of the function, the result must be returned and not printed. Example, "
                "when 'x' is equal to 4 and 'y' is equal to 5, the returned result is '4.033204557385719'")

    class __Test3(__Test):
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
                output = self._test_function(function, self._testInputs[i])
                if self._testResult[i].lower() in [x.lower() for x in output]:
                    self._finalResult += 0
                else:
                    self._finalResult += 1

            success = self._print_result(self._finalResult, self._testNumber)
            if self._debug:
                return success

        @staticmethod
        def test_info():
            print(
                "Write a function that has two arguments that receive integers. If both values are the same print "
                "'equal' if the first value is the smallest print 'minor' and if the first value is the highest print "
                "'major'. E.g: input_1: 10, input_2: 3, prints: 'major'.")

    class __Test4(__Test):
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
                output = self._test_function(function, self._testInputs[i])
                if self._testResult[i].lower() in [x.lower() for x in output]:
                    self._finalResult += 0
                else:
                    self._finalResult += 1

            success = self._print_result(self._finalResult, self._testNumber)
            if self._debug:
                return success

        @staticmethod
        def test_info():
            print(
                "Write a function that takes an undefined number of inputs containing a number that represents a "
                "price. An input equal to \"0\" indicates the end of the input process. Sum all the prices and then "
                "make the following:\n\t- If the total price is less than $ 250, NO discount is applied. \n\t- If the "
                "total price is greater than or equal to $ 250 and less than $ 500, a 5% discount is applied.\n\t- If "
                "the total price is greater than or equal to $ 500 and less than $ 1000 a discount of 10% is "
                "applied.\n\t- If the total price is greater than or equal to $ 1000, a 15% discount is applied.\n To "
                "finish, print the final price with the format: \"Final price is [FINAL_PRICE]\"")

    class __Test5(__Test):
        _testResult: [str] = ["F", "G", "F"]
        _testInputs: [str] = ["PFFPPF", "PFPPPPPPPPPF", "PF"]
        _finalResult: int = 0
        _testNumber: int = 5

        def test(self, function):
            for i in range(len(self._testResult) - 1):
                output = self._test_function(function, self._testInputs[i])
                if self._testResult[i].lower() in [x.lower() for x in output]:
                    self._finalResult += 0
                else:
                    self._finalResult += 1

            success = self._print_result(self._finalResult, self._testNumber)
            if self._debug:
                return success

        @staticmethod
        def test_info():
            print(
                "Write a function that has a unique input: a string that contains 'P' and 'F'. 'P' stands for "
                "'Passed' and 'F' stands for 'Failed'. De function must return 'G' (Graduated) if 80% of the "
                "characters in the input are 'P's, if not it must return an 'F' (F). E.g. Input: 'PFFPPF' - Out"
                "put: 'F'"
            )

    class __CLIManager:

        def __init__(self, device: str):
            self.print_ = self.PrintMsg()
            self.device = device

        @staticmethod
        def detectSelfRestartedFlag() -> bool:
            if '_debug' in sys.argv:
                return True

        def p_warning(self, message: str, end="\n"):
            if self.device == "ios":
                self.print_.pythonista_warning(message=f"{message}", end=end)
            else:
                self.print_.normal_warning(message=f"{message}", end=end)

        def p_error(self, message: str, end="\n"):
            error_line = currentframe().f_back.f_lineno
            if self.device == "ios":
                self.print_.pythonista_error(message=f"{message} - Tester.py [Line: {error_line}]", end=end)
            else:
                self.print_.normal_error(message=f"{message} - Tester.py [Line: {error_line}]", end=end)

        def p_success(self, message: str, end="\n"):
            if self.device == "ios":
                self.print_.pythonista_success(message=f"{message}", end=end)
            else:
                self.print_.normal_success(message=f"{message}", end=end)

        class PrintMsg:

            class Colors:
                success = '\033[92m'
                warning = '\033[93m'
                error = '\033[91m'
                ends = '\033[0m'

            def normal_warning(self, message: str, end: str):
                print(f">> {self.Colors.warning}Warning:{self.Colors.ends} {message}", end=end)

            def normal_error(self, message: str, end: str):
                print(f">> {self.Colors.error}Error:{self.Colors.ends} {message}", end=end)

            def normal_success(self, message: str, end: str):
                print(f">> {self.Colors.success}Success:{self.Colors.ends} {message}", end=end)

            @staticmethod
            def pythonista_warning(message: str, end: str):
                console.set_color()
                print(">> ", end="")
                console.set_color(255, 255, 0)
                print("Warning: ", end="")
                console.set_color()
                print(message, end=end)
                console.set_color()

            @staticmethod
            def pythonista_success(message: str, end: str):
                console.set_color()
                print(">> ", end="")
                console.set_color(0, 255, 0)
                print("Success: ", end="")
                console.set_color()
                print(message, end=end)
                console.set_color()

            @staticmethod
            def pythonista_error(message: str, end: str):
                console.set_color()
                print(">> ", end="")
                console.set_color(255, 0, 0)
                print("Error: ", end="")
                console.set_color()
                print(message, end=end)
                console.set_color()

    class __VersionManager:

        def __init__(self, cli, currentVersion, device):
            self.__rawVersionGit = self.__get_versionGithub_usingRequests()
            self.__rawVersionLocal = currentVersion

            self.__intVersionGit = self.__version_to_int(version=self.__rawVersionGit)
            self.__intVersionLocal = self.__version_to_int(version=self.__rawVersionLocal)
            self.__cli = cli
            self.installationPath = self.__get_installation_path()
            self.device = device

        def __get_installation_path(self) -> str:
            import site
            path = site.USER_SITE if self.device != "windows" else self.__get_installation_path()

            return path

        @staticmethod
        def __get_versionGithub_usingRequests():
            version: str = requests.get(
                'https://raw.githubusercontent.com/AOx0/py-ColoTester/SiteImp/version.txt').content.decode("utf-8")

            finalVersion = ""
            for i in version:
                if i == "." or i.isdigit():
                    finalVersion += i

            return finalVersion

        @staticmethod
        def __version_to_int(version: str):
            def makeFinalInt():
                tempValue = ""
                for i in version:
                    if i == ".":
                        versionArray.append(int(tempValue))
                        tempValue = ""
                    else:
                        tempValue += i
                versionArray.append(int(tempValue))

                return (versionArray[0] * 1000000000) + (versionArray[1] * 1) + (versionArray[2] * 0.000000001)

            def fixVersion(v):
                if v.count(".") == 1:
                    v += ".0"
                elif v.count(".") == 0:
                    v += ".0.0"

                return v

            versionArray = []
            version = fixVersion(version)
            return makeFinalInt()

        @staticmethod
        def __get_testerScript_usingRequests():
            return requests.get("https://raw.githubusercontent.com"
                                "/AOx0/py-ColoTester/SiteImp/Tester.py").content.decode("utf-8")

        @staticmethod
        def __ios_update_install():
            contents = requests.get(
                "https://raw.githubusercontent.com/AOx0/py-ColoTester/SiteImp/Tester.py").content.decode(
                "utf-8")

            with open(f"{os.path.expanduser('~/Documents/site-packages-3')}/"
                      "Tester.py", "w+", encoding="utf-8") as f:
                f.seek(0)
                f.write(contents)
                f.truncate()
                f.close()

        @staticmethod
        def __find_sitePackages_windows():
            path = ""
            for path_ in sys.path:
                if 'site-packages' in path_:
                    path = path_.replace('\\', '\\\\')

            return path

        def __pc_update_install(self):
            dirCharacter = "\\" if self.device == "windows" else "/"
            os.system(
                f"curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/SiteImp/Tester.py -o "
                f"{self.installationPath}{dirCharacter}Tester.py")

        def __testerFile_exists(self) -> bool:
            dirCharacter = "\\" if (self.device == "windows") else "/"

            if os.path.exists(f"{self.installationPath}{dirCharacter}Tester.py"):
                exists = True
            else:
                exists = False

            return exists

        def __postUpdateActions(self, isInstalling: bool):
            if isInstalling:
                self.__cli.p_success(f"Tester [v{self.__rawVersionGit}] installed successfully!")
            else:
                self.__cli.p_success(f"Tester [v{self.__rawVersionGit}] updated successfully!")

                # Restarts the script
                if self.device != "ios":
                    os.execv(sys.executable, ['python'] + sys.argv + ['__restartTester'])

        def getTester(self):
            isInstalling = False if self.__testerFile_exists() else True

            if (self.__intVersionLocal < self.__intVersionGit) or isInstalling:
                if not isInstalling:
                    self.__cli.p_warning(f"A new version of Tester is available [v{self.__rawVersionLocal}] -> "
                                         f"[v{self.__rawVersionGit}]")
                else:
                    self.__cli.p_warning(f"Installing Tester.py [v{self.__rawVersionGit}]...")

                if self.device == "ios":
                    self.__ios_update_install()
                    self.__postUpdateActions(isInstalling)
                else:
                    self.__pc_update_install()
                    self.__postUpdateActions(isInstalling)

    @staticmethod
    def __detectDebugFlag() -> bool:
        if '_debug' in sys.argv:
            return True
        else:
            return False

    @staticmethod
    def __detectRestartFlag() -> bool:
        if '__restartTester' in sys.argv:
            return True
        else:
            return False

    @staticmethod
    def __detectDevice() -> str:
        if 'ios' in sys.platform:
            return 'ios'
        elif 'win' in sys.platform and 'dar' not in sys.platform:
            return 'windows'
        else:
            return 'other'

    @staticmethod
    def __pipInstall(module: str, cli: __CLIManager):
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        cli.p_success(f"{module} module installed successfully")
        cli.p_warning("Re-running Tester...")

    def __init__(self):
        self.__version = "0.2.011"

        # Search for run command arguments
        self.__device = self.__detectDevice()
        self.__debug = self.__detectDebugFlag()
        isRestarted = self.__detectRestartFlag()

        if isRestarted:
            # Fix cmd Appearance on Windows.
            print("Re-running Tester...")

        del isRestarted

        # Init CLI
        self.__cli = self.__CLIManager(device=self.__device)

        # Import device-specific modules to color text
        if self.__device == "ios":
            # Import console on ios Pythonista 3
            global console
            import console

            _ = console; del _     # Just to avoid lazy PyCharm warning
        else:
            # Import colorama on Windows/MacOS/etc
            try:
                from colorama import init as init_
                init_()
            except ModuleNotFoundError:
                print(f">> Warning: Tester needs 'colorama' module to work.")
                print(f"Installing 'colorama'...")
                self.__pipInstall('colorama', cli=self.__cli)
                self.__init__()

        # Import requests.
        try:
            global requests
            import requests
        except ModuleNotFoundError:
            self.__cli.p_warning(f">> Warning: Tester needs 'requests' module to work.")
            print(f"Installing 'requests'...")
            self.__pipInstall('requests', cli=self.__cli)
            self.__init__()

        # Init Version Manager
        self.__versionManager = self.__VersionManager(
            cli=self.__cli,
            currentVersion=self.__version,
            device=self.__device
        )

        # Try to update Tester
        self.__versionManager.getTester()

        if "Tester" == __name__:
            self.test1 = self.__Test1(debug=self.__debug)
            self.test2 = self.__Test2(debug=self.__debug)
            self.test3 = self.__Test3(debug=self.__debug)
            self.test4 = self.__Test4(debug=self.__debug)
            self.test5 = self.__Test5(debug=self.__debug)
        else:
            print(f"Welcome to Tester.py [v{self.__version}] by AOx0.\n"
                  "GitHub Repo: https://github.com/AOx0/py-ColoTester")


Tester = Tester()


class Test:

    @staticmethod
    def One(func):
        def wrapper(*_, **__):
            Tester.test1.test(func)
        return wrapper

    @staticmethod
    def Two(func):
        def wrapper(*_, **__):
            Tester.test2.test(func)
        return wrapper

    @staticmethod
    def Three(func):
        def wrapper(*_, **__):
            Tester.test3.test(func)
        return wrapper

    @staticmethod
    def Four(func):
        def wrapper(*_, **__):
            Tester.test4.test(func)
        return wrapper

    @staticmethod
    def Five(func):
        def wrapper(*_, **__):
            Tester.test5.test(func)
        return wrapper


if __name__ == "Tester":
    Test = Test()
