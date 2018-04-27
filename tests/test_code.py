import os
import sys
import subprocess

import pytest

thisdir = os.path.dirname(os.path.abspath(__file__))

is_pypy = False
try:
    import __pypy__
    is_pypy = True
except ImportError:
    is_pypy = False

class Test(object):

    # See what Python versions the combined
    # coverage report includes
    def test_show_coverage(self):
        if 'conda' in sys.version: # Anaconda
            if sys.version_info.major == 2:
                print(sys.version_info)
            if sys.version_info.major == 3:
                print(sys.version_info)
        elif not is_pypy:         # CPython
            if sys.version_info.major == 2:
                if sys.version_info.minor == 7:
                    print(sys.version_info)
            elif sys.version_info.major == 3:
                if sys.version_info.minor == 5:
                    print(sys.version_info)
                elif sys.version_info.minor == 6:
                    print(sys.version_info)
        if is_pypy:               # PyPY
            if sys.version_info.major == 2:
                print(sys.version_info)
            if sys.version_info.major == 3:
                print(sys.version_info)

    def test_subprocess(self):
        subprocess.call
        rc = subprocess.call(
            ['python',
             os.path.join(thisdir,'subprocess_example.py')])
        assert rc == 0
