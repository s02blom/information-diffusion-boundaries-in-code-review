#https://python.plainenglish.io/how-to-test-jupyter-notebooks-ae8e8b015d9c
import unittest
import importlib
import os.path

class test_notebook_plot(unittest.TestCase):
    
    @classmethod
    def setUpClass(self) -> None:
        if(os.path.isfile('data/minimal_paths/microsoft.pickle.bz2')):
            self.notebook = importlib.import_module("ipynb.fs.full.plot")
        else:
            print("no File")
    
    def test_one(self):
        self.assertEqual((1+1), 2)
    
    
