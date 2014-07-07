__author__ = 'chandrasekar.g'

import os
import site


# ------------------------------------------------- #

# Examples to use OS package
# OS environ package allows user to access declared environmental variables


filename    =   os.environ.get('PYTHONSTARTUP')
javahome    =   os.environ.get('JAVA_HOME')           # I already declared this var in my .bashrc file


print("JAVA_HOM  : ",javahome,'\n')

# ------------------------------------------------- #






# ------------------------------------------------- #

# Example to use site package

userBase    =   site.getuserbase()
absPath     =   site.abs_paths()

print("USER BASE   : ",userBase,'\n')

print("ABSOLUTE PATHS   : ",absPath,'\n')

# ------------------------------------------------- #






# ------------------------------------------------- #
# Example to use for loop

sitePacks   =   site.getsitepackages()

for j in sitePacks:
    print("SITE PACKAGE :",j)


print('\n')
# ------------------------------------------------- #




# ------------------------------------------------- #
# Example to use range

for j in range(8):
    print('Printing J :',j)

print('\n')

print('Printing with in specified range : -  ')
for j in range(2, 8):
    print('Printing J :',j)

# ------------------------------------------------- #