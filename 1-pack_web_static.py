#!/usr/bin/python3
import datetime
from fabric.api import local, run, env


def do_pack():
    """ do_pack - create a compressed tar file """
    """ Ref: https://gist.github.com/elliottb/7744008 """

    # remote ssh credentials
    env.hosts = ['142.44.167.237']
    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/holberton_key'

    # specify path to files being deployed
    env.archive_source = '/data/web_static'

    # archive name, arbitrary, and only for transport
    now = datetime.datetime.now()
    env.archive_name = "web_static_" + str(now.year) + str(now.month) + \
 str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".tgz"

    result = run("mkdir versions")
    if result.failed:
        return None

    # specify path to deploy root dir - you need to create this
    env.deploy_project_root = '/data/web_static/'

    # specify name of dir that will hold all deployed code
    env.deploy_release_dir = 'versions/'

    # symlink name. Full path to deployed code is env.deploy_project_root + this
    env.deploy_current_dir = 'current'

    if result.failed:
        return None
    else:
        return(env.archive_name)
