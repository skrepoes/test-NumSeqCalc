Numeric Sequence Calculator
===========================
Developed with Bootstrap (UI and responsiveness) and JQuery (DOM manipulation, validation and sequence calculation logic).

#####  dev
CSS in this case is very basic, however SASS (scss) files can be found in dev/sass.
Use preferred pre-processor to compile to css/style.css. In dev, simply used Koala GUI App (http://koala-app.com/).

##### py 
Python scripts is used for unit testing. The Selenium (Testing Framework) python library can be found here.

##### tests
The python/selenium unit test scripts are located here. 

##### wwwroot
Contains the web application and web resources. 

Installation
------------
Download the repository ZIP to your local file system.
Extract the contents in the **test-NumSeqCalc-master** directory into **C:\NumSeqCalc** so that your directory structure looks like this:
```sh
C:\NumSeqCalc>dir /B
.gitattributes
dev
py
readme.md
tests
wwwroot
```

Run Manually
------------
Once downloaded, you can manually run the web appication by opening the **C:\NumSeqCalc\wwwroot\index.html** file in your local web browser.
The calculator is used by entering number and pressing **Calculate**.  
Only numeric characters are accepted into the input field. 


Run Unit Tests
--------------
Unit tests have been written using Selenium (http://www.seleniumhq.org/) browser automation testing via Python scripts.
To run these unit tests the following is required:
a)	firefox browser installed
b)	python environment installed
c)	selenium web driver in the python environment

**A. Install Firefox**

https://www.mozilla.org/

**B. Install Python (if required) **

For python I have used Active Python (http://www.activestate.com/activepython)
Download and install this in the default directory.
Add the python install directory to you system path, to allow you to call python.exe from any directory. 

**C. Install selenium web driver for python **

Extract Selenium for python from the repositories location:
C:\NumSeqCalc\py\bin\selenium-2.43.0.tar.gz

From the extracted file, copy the **selenium-2.43.0\py\selenium** folder and it’s contents into your Python environment’s **\lib** folder.
...in my case this was folder was copied into **C:\Python27\Lib** to create **C:\Python27\Lib\selenium** 

The required folder is the one that contains a webdriver folder as well as the selenium.py file.

**Running Unit Tests**

To run unit tests, open a command prompt and change directory to **C:\NumSeqCalc**

Simply run the python command followed by a the name of a script located in the tests directory:

```sh
python tests/<testscript.py>
```

For example:
```sh
C:\NumSeqCalc>python tests/utAllTests.py
```

Execution of a test will open a firefox browser, perform the test and the test results will be outputted in the command window:

For example:
```sh
C:\NumSeqCalc>python tests/utAllTests.py
.
----------------------------------------------------------------------
Ran 1 test in 18.408s

OK
```

Unit Tests
----------
The following tests scripts have bene implemented:
```
                    End-to-end
utAllTests.py       // Run all tests below [with short pauses]

                    Validation checks
utInput_0.py        // User enters number O in calculator
utInput_text.py     // User enters string “text” in calculator
utInput_empty.py    // User enters empty string in calculator

                    Calculations
utInput_1.py        // User enters number 1 in calculator
utInput_10.py       // User enters number 10 in calculator
utInput_100.py      // User enters number 100 in calculator
utInput_1000.py     // User enters number 1000 in calculator

                    Instructions
utOpen_modal.py     // User clicks on instructions button 
```

Notes
-----
* While I used selenium/python for the unit tests, I am very open to adopt and use your preferred unit testing framework, as required. 

* The calculator input field has been implemented only allow entry of numeric characters. Therefore the utInput_text test will actually not "phyically" enter any characters into the input field, but this is still a valid test case.

* During test execution,  if you receive the error
```
ImportError: No module named selenium
```
then this is an indicatation you are missing the selenium folder (containing selenium.py and the webdriver folder) from  python's /lib directory. 
