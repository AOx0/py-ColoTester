from io import StringIO 
from time import sleep

try:
    import requests
except ModuleNotFoundError:
    
    def _fkLoading():
        for _ in range(4):
            print("*", end="")
            sleep(0.5)

    _fkLoading()
    print(" 'Tester' needs 'requests' module to work.")
    
    _fkLoading()
    print("Installing 'requests' module...\n")
    
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
            _fkLoading()
            print("'requests' module installed successfully")
        except ModuleNotFoundError:
            print("Something went wrong while updating Tester [Line 35]\n")
        
        
    except:
        print("Something went wrong while updating Tester [Line 39]")

import sys
import os

version : float = 0.12

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
    def testFunction(function, testResult, testInputs) -> [str]:
        with _Capturing() as output:
            sys.stdin = StringIO(testInputs)
            function()
        return output

class test1():
    
    testResult = "Hola mi nombre es Daniel, tengo 27 años y vengo de España"
    testInputs = "Daniel\n27\nEspaña"
    
    @staticmethod
    def test(function, testResult = testResult, testInputs = testInputs):
        output = TstHandler.testFunction(function, testResult, testInputs)
        print(output, testResult.lower())
        if testResult.lower() in [i.lower() for i in output]:
            print("Correcto")
        else:
            print("Incorrecto :D")
    
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
    def _fkLoading():
        for _ in range(4):
            print("*", end="")
            sleep(0.5)

    @staticmethod
    def update():
        
        try:
            gitVersion : float = _UpdateManager._getRepoVersion()
        except:
            print("Failed to get GitHub version [Line 104]")
            return 

        if gitVersion != version and gitVersion > version:
            try:
                for _ in range(4):
                    print("*", end="")
                    sleep(0.5)
                
                _UpdateManager._fkLoading()
                print(f" Actualizando 'Tester' v. {version} -> {gitVersion}...")
                os.system("curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o Tester.py")
                print("Tester actualizado!")
            except:
                print("Something went wrong while updating Tester [Line 118]")
                return


_UpdateManager.update()
