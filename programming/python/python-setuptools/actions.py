
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import pythonmodules, pisitools


def install():
    pythonmodules.install()
    pythonmodules.install(pyVer="3")
