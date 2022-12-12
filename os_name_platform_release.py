import os, sys, platform, sysconfig
print('Your operating system is :', os.name, 'Name of the OS system :', platform.system(), 'Version of the operating system :', platform.release(), 'Your sysconfig.get_platform() is :', sysconfig.get_platform(), 'Your platform.machine() :', platform.machine(), 'Your platform.architecture() :', platform.architecture())
