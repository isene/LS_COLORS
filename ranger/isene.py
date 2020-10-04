# Copyright (C) 2009-2013  Roman Zimbelmann <hut@lavabit.com>
# This software is distributed under the terms of the GNU GPL version 3.
# Geir Isene's ranger colorscheme - corresponding with the LS_COLORS:
# <https://github.com/isene/LS_COLORS>

# FIRST DEFINE THE FILE TYPES
# See: https://github.com/ranger/ranger/blob/master/doc/colorschemes.md
import ranger.gui.widgets.browsercolumn
import ranger.gui.context

# Add your key names
ranger.gui.context.CONTEXT_KEYS.append('textfiles')
ranger.gui.context.CONTEXT_KEYS.append('pdffiles')
ranger.gui.context.CONTEXT_KEYS.append('officefiles')
ranger.gui.context.CONTEXT_KEYS.append('htmlfiles')
ranger.gui.context.CONTEXT_KEYS.append('pgmfiles')
ranger.gui.context.CONTEXT_KEYS.append('binaries')
ranger.gui.context.CONTEXT_KEYS.append('hyperlist')
ranger.gui.context.CONTEXT_KEYS.append('npcfiles')

# Set to False (the default value)
ranger.gui.context.Context.textfiles = False
ranger.gui.context.Context.pdffiles = False
ranger.gui.context.Context.officefiles = False
ranger.gui.context.Context.htmlfiles = False
ranger.gui.context.Context.pgmfiles = False
ranger.gui.context.Context.binaries = False
ranger.gui.context.Context.hyperlist = False
ranger.gui.context.Context.npcfiles = False

OLD_HOOK_BEFORE_DRAWING = ranger.gui.widgets.browsercolumn.hook_before_drawing

def new_hook_before_drawing(fsobject, color_list):
    if fsobject.extension in ['txt', 'md', 'markdown', 'tex', 'book', 'rss', 'log', 'ini', 'conf', 'cfg', 'cf' ]:
        color_list.append('textfiles')
    if fsobject.extension in ['pdf', 'PDF', 'ps', 'djvu', 'mobi', 'epub']:
        color_list.append('pdffiles')
    if fsobject.extension in ['odt', 'odb', 'rtf', 'doc', 'docx', 'dotx', 'odp', 'ppt', 'pptx', 'pps', 'csv', 'ods', 'xls', 'xlsx', 'pages', 'numers', 'key', 'pez']:
        color_list.append('officefiles')
    if fsobject.extension in ['htm', 'html', 'css', 'sass', 'scss', 'jhtm', 'eml']:
        color_list.append('htmlfiles')
    if fsobject.extension in ['rb', 'py', 'php', 'java', 'jsp', 'js', 'vb', 'vba', 'pl', 'hs', 'fs', 'sh', '41', 'rpn']:
        color_list.append('pgmfiles')
    if fsobject.extension in ['7z', 'a', 'bz2', 'gz', 'lz', 'rar', 'tar', 'tgz', 'z', 'zip', 'apk', 'deb', 'rpm', 'jar', 'jar', 'cab', 'pak', 'dmg', 'asc', 'gpg', 'pgp', 'enc', 'pem', 'sig']:
        color_list.append('binaries')
    if fsobject.extension in ['hl', 'woim']:
        color_list.append('hyperlist')
    if fsobject.extension == 'npc':
        color_list.append('npcfiles')

    return OLD_HOOK_BEFORE_DRAWING(fsobject, color_list)

ranger.gui.widgets.browsercolumn.hook_before_drawing = new_hook_before_drawing

# THEN DEFINE THE COLOR SCHEME
from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Default(ColorScheme):
    progress_bar_color = black

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                bg = red
            if context.border:
                fg = default
            if context.media:
                if context.image:
                    fg = 207
                else:
                    fg = 135
            # Specific file types as defined above...
            if context.textfiles:
                fg = 228
            if context.pdffiles:
                fg = 218
            if context.officefiles:
                fg = 211
            if context.htmlfiles:
                fg = 173
            if context.pgmfiles:
                fg = 75
            if context.binaries:
                fg = 116
            if context.hyperlist:
                fg = 208
            if context.npcfiles:
                fg = 166
            #... to here
            if context.container:
                fg = red
            if context.directory:
                attr |= bold
                fg = 111
            elif context.executable and not \
                    any((context.media, context.container,
                        context.fifo, context.socket)):
                fg = 46
            if context.socket:
                fg = 196
            if context.fifo or context.device:
                fg = 124
                if context.device:
                    attr |= bold
            if context.link:
                attr |= bold
                fg = context.good and 248 or 212
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
            if not context.selected and (context.cut or context.copied):
                fg = black
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = yellow
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

        elif context.in_titlebar:
            if context.hostname:
                fg = context.bad and red or green
            elif context.directory:
                attr |= bold
                fg = 111
            elif context.tab:
                if context.good:
                    bg = cyan
            elif context.link:
                attr |= bold
                fg = 246

        elif context.in_statusbar:
            attr |= bold
            if context.permissions:
                if context.good:
                    fg = white
                elif context.bad:
                    attr |= bold
                    fg = red
            if context.marked:
                attr |= bold | reverse
                fg = white
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = red
            if context.loaded:
                bg = self.progress_bar_color

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = blue

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        return fg, bg, attr
