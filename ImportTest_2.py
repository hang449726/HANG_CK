import io
import sys
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import ImportTest_1 as it
from ImportTest_1 import fun4,fun3
it.fun1()
it.fun2()
fun4()
fun3()