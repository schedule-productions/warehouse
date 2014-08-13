#!/usr/bin/env python

import subprocess
from os import path
from os import chdir
from os import system

command = '"{}" "warehouse_manager_src.py"'.format(
    path.join("..", "warehouse-manager-bin", "ipyw.exe"))

chdir("warehouse-manager-src")

subprocess.call(command)
