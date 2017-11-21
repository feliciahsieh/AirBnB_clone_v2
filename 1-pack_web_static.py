#!/usr/bin/python3
import datetime
from fabric.api import local
from fabric.api import *

def do_pack():
    """ do_pack - create a compressed tar file """

    now = datetime.datetime.now()
    fn = "web_static_" + str(now.year) + str(now.month) + \
 str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".tgz"

    dirSrc = "/data/web_static"
    dirDest = "versions"
    result = run("mkdir " + dirDest)
    if result.failed:
        return None

    result = cxn.run('tar -cvzf ' + dirDest + '/' + fn + ' web_static')
    if result.failed:
        return None
    else:
        return(fn)
