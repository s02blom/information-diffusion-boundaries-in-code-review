#https://python.plainenglish.io/how-to-test-jupyter-notebooks-ae8e8b015d9c
import unittest
import importlib
import os.path
import pandas as pd
import numpy as np
class test_notebook_plot(unittest.TestCase):
    
    @classmethod
    def setUpClass(self) -> None:
        self.flag = True
        if(os.path.isfile('data/minimal_paths/microsoft.pickle.bz2')):
            self.notebook = importlib.import_module("ipynb.fs.full.plot")
        else:
            self.flag = False
            print("no File")

    def setup(self):
        if not self.flag:
            self.fail("File does not exist")
    
    def test_compute_in_notebook(self):
        empy_numpy_array = np.zeroes(4,4)
        empty_dataframe = pd.DataFrame(empy_numpy_array)
        with self.assertRaises(TypeError):
            self.notebook.compute(empty_dataframe)
        
    
    
