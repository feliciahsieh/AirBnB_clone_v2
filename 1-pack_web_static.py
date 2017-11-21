#!/usr/bin/python3
import tarfile
import datetime
import time


def do_pack():
    """ do_pack - create a compressed tar file """

    now = datetime.datetime.now()
    fn = "web_static_" + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".tgz"
    print(fn)


    #print('{%Y%m%d%H%M%S}'.format(datetime.datetime.now()))

    # web_static_<year><month><day><hour><minute><second>.tgz

    tar = tarfile.open(fn, "w")
    for name in ["."]:
        tar.add(name)
    #tar.add("/data/web_static/releases/test/index.html")
    #tar.add("/data/web_static/shared")

    tar.close()


do_pack()
