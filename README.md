## Software design with Python assignments
**Work by Alexnder Eponeshnikov**

##Assignment 1

How to run:
```
git clone https://github.com/Eponeshnikov/SDwPython.git
cd SDwPython/Assignments/A1
python main.py or python3 main.py
```
**task1.py** contains function decorator which calculates execution time of function and number of calls of function.

**task2.py** contains function decorator  which calculates execution time of function, number of calls of function 
and print function's name, type, signature, type of arguments, docstring, source code and output.

**task3.py** contains class decorator which calculates execution time of function, number of calls of function and print
function's name, type, signature, type of arguments, docstring, source code and output and put all this information to
the .txt file in _txtFiles_ directory. Name of .txt file constructed using next rule: _**func_name + task_3.txt**_.
Also, **task3.py** contains function which rank functions by the time.

**task4.py** contains class and function decorators which calculate execution time of function, number of calls of 
function and print function's name, type, signature, type of arguments, docstring, source code and output and 
(only class decorator) put all this information to the .txt file in _txtFiles_ directory. Name of .txt file constructed 
using next rule: _**func_name + task_4_1.txt**_ for _class decorator_ and _**func_name + task_4_2.txt**_ for _function 
decorator_. If an error occurs while the function is running, the error message is written to the .txt logfile in 
_txtFiles_ directory. Name of .txt logfile constructed using next rule: _**func_name + _err_task_4_1.txt**_ for _class 
decorator_ and _**func_name + _err_task_4_2.txt**_ for _function decorator_.


