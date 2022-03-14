import sys
sys.path.append('../../Pass/')
import importlib


class variables:
    def get_variables(input_module):
        global get_variables
        return  importlib.import_module(input_module)
    
    global input_module,pass_py
    input_module = 'pass_test'
    pass_py = get_variables(input_module)
    
    def to_middleware():
        middle_mod =  pass_py.active_crawl
        return middle_mod
        # pass_py = get_variables(input_module)
        # return pass_py.active_crawl