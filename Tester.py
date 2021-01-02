from io import StringIO 

import requests
import sys
import os

version : float = 0.1

class _Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio 
        sys.stdout = self._stdout

class _TestClass:
    
    @staticmethod
    def testFunction(function, testResult) -> [str]:
        with _Capturing() as output:
            function()
        return output

class test1():
    
    testResult = "Hola mi nombre es Daniel, tengo 27 años y vengo de España"
    
    @staticmethod
    def test(function, testResult = testResult):
        output = _TestClass.testFunction(function, testResult)
        
        if testResult.lower() in [i.lower() for i in output]:
            print("Correcto")
    
    def printTest():
        print("Una función que por medio de inputs reciba un nombre [Daniel], una edad [27] y un país de origen [España] e imprima el mensaje 'Hola mi nombre es [NOMBRE], tengo [EDAD] años y vengo de [PAIS]'.")

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
            print("Failed to get GitHub version")
            return 

        if gitVersion != version and gitVersion > version:
            try:
                print(f"Actualizando 'Tester' v. {version} -> {gitVersion}...")
                os.system("curl -sS https://raw.githubusercontent.com/AOx0/py-ColoTester/master/Tester.py -o Tester2.py")
                print("Tester actualizado!")
            except:
                print("Something went wrong while updating Tester")
                return

_UpdateManager.update()

