import sys

paths = sys.path
for path in paths:
    print(path)

print("-"*50)

sys.path.append(r"C:\Users\mindf\Desktop\Wipro-IIHT\python-work\scripts\09-user-defined-modules")

paths = sys.path
for path in paths:
    print(path)

import mymodule
print('From mymodule: ', mymodule.checkprime(10))