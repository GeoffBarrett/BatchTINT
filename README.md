# BatchTINT
A GUI created by the Taub Institute in order to create an end-user friendly batch processing solution to complement Axona's new command line modification of TINT.

# Requirements
Operating System: Windows

This GUI was created with the Windows operating system in mind. Therefore, it is untested on Mac OSX, as well as Linux. It is possible
(though unlikely) that it would work on other operating systems.

Suggested: Use of Python 3.4.4, PyQt4 is most compatible with this version of Python, however there are Python 3.5 versions that may work
Python 3.4.4 can be downloaded here: https://www.python.org/downloads/release/python-344/

# Installation

1) For those that do not have GitHub installed on their desktop, they will need to install the GitHub Desktop Application: 
https://desktop.github.com/
2) The next step would be to open the Command Prompt

3) In the command prompt navigate to the folder where you want to clone the repository (type in: cd folder_path)

4) Then your next step will be to clone the repository by typing in the following to your Command Prompt:
git clone https://github.com/GeoffBarrett/BatchTINT.git

Note: If there is an error produced by the Command Prompt saying the following: 
'git' is not recognized as an internal or external command,operable program or batch file.
ensure that you have added the appropriate git locations to the path system variable. Follow these steps in order to add system variables


  a) First. you are going to need to find the location of git-core and copy the path, it will be similar to the following:
  C:\Users\[Your Username]\AppData\Local\GitHub\[Something Similar to PortableGit_25d850739bc178b2eb13c3e2a9faafea2f9143c0\mingw32\libexec\git-core
  
  b) Second, you will need to find the path of the 'bin' folder within the 'mingw32' folder which will look similar to the following:
  C:\Users\[your name]\AppData\Local\GitHub\PortableGit_25d850739bc178b2eb13c3e2a9faafea2f9143c0\mingw32\bin
  
  c) Go to the following window: Control Panel -> System and Security -> System -> Advanced Systems Settings 
  -> Advanced Tab (if not already on it) and -> Environmental Variables 
  
  d) Under 'System variables' edit the 'Path' variable
  
  e) If the variable is a single line of paths then append the two paths to the end of the variable, 
  you will need to add a semicolon to separate each path (existing path;git-core path;bin path).
  If the window you are looking at has a list of the different paths then you will simply add the two paths.
  
  f) Once you close the existing Command Prompt and open a new one the commands will be available

5) If you are using Python 3.4.4 I have included two wheel (.whl) files in the GitHub repository for PyQt4 that will need
to be installed via the Command Prompt.

If you have not added the Python34 path to the system variable (as done for the GitHub path) then we will have to do the same.

Add the following paths to the 'path' system variable:
C:\Python34\Scripts
C:\Python34

You should also upgrade the 'pip' python script which allows for the downloading of python libraries. To upgrade pip, type the
following into the Command Prompt (remember to restart after adding the system variable): python -m pip install --upgrade pip

Now you can type the following into the command prompt to install PyQt4:
python -m pip install [wheel file path] 

***If you have spaces in your wheel file path make sure to surround the path by quotes***
example: python -m pip install "C:\Users\My Name\Desktop\GitHub\"

The wheel files are the following:
64-bit PC: use the PyQt4-4.11.4-cp34-none-win_amd64.whl files
32-bit PC: use the PyQt4-4.11.4-cp34-none-win32.whl file

Note: if you are using Python 3.5 you can find those .whl files here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4

6) Install a python library repsonsible for some of the images on the GUI

Type in the following into the Command Prompt:

python -m pip install pillow

7) you will also have to add tint to the system variable as we did before with GitHub and Python

Add the following path: C:\Program Files (x86)\Axona\Tint

# Running GUI

Now in your command prompt you can type the following in order to run the GUI:

python BatchSort.py



    
