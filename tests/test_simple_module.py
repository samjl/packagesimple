import sys
sys.path.append(sys.path[0] + "/..")
from simple_module import funcC

def test_funcC():
    assert funcC("works!") == "packagesimple:simple_module:funcC: works!"
