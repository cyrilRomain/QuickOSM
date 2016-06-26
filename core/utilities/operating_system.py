# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickOSM
 A QGIS plugin
 OSM Overpass API frontend
                             -------------------
        begin                : 2014-06-11
        copyright            : (C) 2014 by 3Liz
        email                : info at 3liz dot com
        contributor          : Etienne Trimaille
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import platform
import sys
from shutil import copytree, copy2
from os import listdir, makedirs, stat
from os.path import join, isdir, exists

from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtNetwork import QNetworkProxy


def get_proxy():
    """
    Get a proxy according to QSettings
    @return: proxy
    @rtype: QNetworkProxy
    """
    s = QSettings()
    if s.value('proxy/proxyEnabled', '') == 'true':

        proxy_type = s.value('proxy/proxyType', '')
        proxy_host = s.value('proxy/proxyHost', '')
        proxy_port = s.value('proxy/proxyPort', '')
        proxy_user = s.value('proxy/proxyUser', '')
        proxy_password = s.value('proxy/proxyPassword', '')

        proxy = QNetworkProxy()

        if proxy_type == 'DefaultProxy':
            proxy.setType(QNetworkProxy.DefaultProxy)
        elif proxy_type == 'Socks5Proxy':
            proxy.setType(QNetworkProxy.Socks5Proxy)
        elif proxy_type == 'HttpProxy':
            proxy.setType(QNetworkProxy.HttpProxy)
        elif proxy_type == 'HttpCachingProxy':
            proxy.setType(QNetworkProxy.HttpCachingProxy)
        elif proxy_type == 'FtpCachingProxy':
            proxy.setType(QNetworkProxy.FtpCachingProxy)

        proxy.setHostName(proxy_host)
        proxy.setPort(int(proxy_port))
        proxy.setUser(proxy_user)
        proxy.setPassword(proxy_password)
        return proxy
    else:
        return None


def copy_tree(src, dst, symlinks=False, ignore=None):
    if not exists(dst):
        makedirs(dst)
    for item in listdir(src):
        s = join(src, item)
        d = join(dst, item)
        if isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not exists(d) or stat(s).st_mtime - stat(d).st_mtime > 1:
                copy2(s, d)


def is_windows():
    return True if platform.system() == 'Windows' else False


def get_default_encoding():
    if is_windows():
        return sys.getdefaultencoding()
    else:
        return 'UTF-8'
