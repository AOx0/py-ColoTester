from io import StringIO 

from inspect import currentframe

def _getCurrentLine():
    cf = currentframe()
    return cf.f_back.f_lineno

try:
    import requests
except ModuleNotFoundError:
    
    print(">> Warning: Tester needs 'requests' module to work.")
    
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
            print(">> Success: 'requests' module installed successfully")
        except ModuleNotFoundError:
            print(f">> Error: Something went wrong while updating Tester [Line {_getCurrentLine()}]\n")
        
        
    except:
        print(f">> Error: Something went wrong while updating Tester [Line {_getCurrentLine()}]")

import sys
import os

version : float = 0.124

class _Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio 
        sys.stdout = self._stdout

class TstHandler:
    
    @staticmethod
    def testFunction(function, testInputs) -> [str]:
        with _Capturing() as output:
            sys.stdin = StringIO(testInputs)
            function()
        return output

class test1():
    
    testResult : [str] = ["Hola mi nombre es Daniel, tengo 27 años y vengo de España"]
    testInputs : [str] = ["Daniel\n27\nEspaña"]
    finalResult : int = 0

    @staticmethod
    def test(function, testResult = testResult, testInputs = testInputs, finalResult = finalResult):
        for i in range(len(testResult)-1):
            output = TstHandler.testFunction(function, testInputs[i])
            if testResult[i].lower() in [x.lower() for x in output]:
                finalResult += 0
            else:
                finalResult += 1
        
        if finalResult == 0:
            print("Test 1: Correct")
        else:
            print("Test 1: Incorrect. One or more cases returned a bad/unexpected result")
    
    def printTest():
        print("Una función que por medio de inputs (3) reciba un nombre [Daniel], una edad [27] y un país de origen [España] e imprima el mensaje 'Hola mi nombre es [NOMBRE], tengo [EDAD] años y vengo de [PAIS]'.")

class _UpdateManager():

    @staticmethod
    def _getRepoVersion():
        githubRepoVersion : str = requests.get('https://raw.githubusercontent.com/AOx0/py-ColoTester/master/version.txt').content.decode("utf-8")
        gitVersion : str = ""
        for i in githubRepoVersion:
            if i.isdigit()  or i == ".":
                gitVersion += i

        return float(gitVersion)
    
    @staticmethod
    def update():
        
        try:
            gitVersion : float = _UpdateManager._getRepoVersion()
        except:
            print(f">> Error: Failed to get GitHub version. Tester [Line _getCurrentLine()]")
            return 

        if gitVersion != version and gitVersion > version:
            try:
                print(">> Warning: A new version of Tester is available.")
                print(f">> Updating Tester v. {version} -> {gitVersion}...")
                os.system("curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o Tester.py")
                print("\n>> Success: Tester updated successfully!")
            except:
                print(f">> Error: Something went wrong while updating Tester [Line {_getCurrentLine()}]")
                return


_UpdateManager.update()
