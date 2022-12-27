import sys
# sys.version_info(major=3, minor=7, micro=0, releaselevel='final', serial=0)
def versPython():
    if sys.version_info.major == 3:
        print('Your python version is Python 3')
    else:
        print('Your python version is Python 2')
versPython()

print(sys.version)
