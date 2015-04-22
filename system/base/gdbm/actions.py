#!/usr/bin/python


from pisi.actionsapi import autotools, pisitools


def setup():
    autotools.configure("--disable-static \
                         --enable-libgdbm-compat")


def build():
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
