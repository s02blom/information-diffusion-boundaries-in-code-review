#https://python.plainenglish.io/how-to-test-jupyter-notebooks-ae8e8b015d9c
import unittest
import importlib

class test_notebook_plot(unittest.TestCase):
    
    @classmethod
    def setUpClass(self) -> None:
        self.notebook = importlib.import_module("ipynb.fs.full.plot")
    
    
