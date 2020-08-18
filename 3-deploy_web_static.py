#!/usr/bin/python3
"""Script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy.
"""
from datetime import datetime as dt
from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ["104.196.209.226", "34.75.152.150"]


def do_pack():
    """File compressor"""
    try:
        timestamp = dt.now().strftime("%Y%m%d%H%M%S")
        filepath = "./versions/web_static_{}".format(timestamp)
        local('mkdir -p ./versions')
        local('tar -cvzf {}.tgz web_static'.format(filepath))
        archive_path = "{}.tgz".format(filepath)
        if os.path.exists(archive_path):
            return archive_path
    except:
        return None


def do_deploy(archive_path):
    """Deploy the files to the servers"""
    if os.path.exists(archive_path):
        cloudpath = "/data/web_static/releases/" + archive_path[:-4]
        archive = archive_path.split('/')[-1]
        current = "/data/web_static/current"
        put(archive_path, '/tmp')
        run("mkdir -p {}".format(cloudpath))
        run("tar -xzf /tmp/{} -C {}".format(archive, cloudpath))
        run("rm /tmp/{}".format(archive))
        run("mv {}/web_static/* {}".format(cloudpath, cloudpath))
        run("rm -rf {}/web_static".format(cloudpath))
        run("rm -rf {}".format(current))
        run("ln -s {} {}".format(cloudpath, current))
        print('New version deployed!')
        return True
    else:
        return False


def deploy():
    """cript (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers.
    """
    pack = do_pack()
    deploy_all = do_deploy(pack)
    return deploy_all
