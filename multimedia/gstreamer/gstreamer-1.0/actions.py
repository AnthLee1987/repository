
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib \
                         --with-package-name=\"GStreamer 1.0.6 Evolve OS\" \
                         --with-package-origin=http://www.evolve-os.com")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
