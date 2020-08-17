#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:21:54 2020
@author: Robinson Montes
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    file = local('sudo tar -czvf ./versions/web_static_{}.tgz web_static'
                   .format(now))
    if file.succeeded:
        return file
    else:
        return None
