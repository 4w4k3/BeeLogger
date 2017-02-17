#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 BeeLogger
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/BeeLogger
# Licensed under the BSD-3-Clause
import subprocess
import urllib2


def update_client_version(version):
    with open("version.txt", "r") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False


def main():
    version = urllib2.urlopen("https://raw.githubusercontent.com/4w4k3/BeeLogger/master/version.txt").read()
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return "[*] Updated to latest version: v{}..".format(version)
    else:
        return "[*] You are already up to date with git origin master."


if __name__ == '__main__':
    print("[*] Checking version information..")
    print(main())
