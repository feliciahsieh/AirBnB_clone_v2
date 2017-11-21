#!/usr/bin/python3
import os, errno
import tarfile
import datetime
import time
from fabric.api import *


def do_pack():
    """ do_pack - create a compressed tar file """

    now = datetime.datetime.now()
    fn = "web_static_" + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.
second) + ".tgz"
    print(fn)

    tar = tarfile.open(fn, "w")
    for name in ["/data/web_static"]:
        tar.add(name)

    tar.close()

    directory = "./versions"
    result = run("mkdir " + directory)
    if result.failed:
        print("failed mkdir()")
    else:
        print(directory)


do_pack()
