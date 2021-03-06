# Compatible since ranger 1.7.0
# This linemode emulates 'ls --classify' in that it adds a "/" at end of
# directories (even links to directories which is more practical than the ls
# switch) and an "@" at the end of links to files.
# By Geir Isene <g@isene.com>

from __future__ import (absolute_import, division, print_function)

import codecs

import ranger.api
from ranger.core.linemode import LinemodeBase


@ranger.api.register_linemode
class MyLinemode(LinemodeBase):
    name = "classify"

    def filetitle(self, fobj, metadata):
        return_value = fobj.relative_path
        if fobj.is_directory:
            return_value += "/"
        elif fobj.is_link:
            return_value += "@"
        elif fobj.is_socket:
            return_value += "="
        elif fobj.is_fifo:
            return_value += "|"
        return return_value

    def infostring(self, fobj, metadata):
        raise NotImplementedError
