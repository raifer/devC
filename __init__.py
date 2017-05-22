# coding:utf-8

import os
import sys

import sixpad as sp
page = sp.window.curPage
win = sp.window

from . import goto
from . import tracer

## Plugin Path
PLUGIN_PATH = os.path.dirname(__file__)


def get_shortkey(action):
    """get_shortkey(action) -> shorkey, str"""
    
    # shortkeys
    shortkey ={
        'next_function': ['CTRL+R', None],
        'previous_function':['CTRL+SHIFT+R', None],
        'next_struct': ['CTRL+E', None],
        'previous_struct':['CTRL+SHIFT+E', None],
        'list_function':['ALT+R', None],
    } # end shortkey dico
    
    value = shortkey[action]
    # test if user set personal key for this action
    if value[1]:
        # User shortkey found
        key = value[1]
    else:
        # Default shortkey used
        key = value[0]
    # end if
    return key
# end def

def load_dev_c(page):
    """Load dev C module"""
    
    log.h2('Load dev C')
    # Creating devC menu
    log('Create dev C menu')
    menu_dev_c = win.menus.add(label = "Dev C", action = None, index = -2, submenu = True, name = 'dev_c',specific = True, group = 'devc')
    # creat sub menu and global submenus and items
    log('creat sub menu and global submenus and items')
    submenus, items = creat_submenu(menu_dev_c)
    # Accelerator
    log('creat accelerators')
    accelerator_active = creat_accelerator()
    return menu_dev_c, submenus, items
# end def

def creat_submenu(menu_dev_c):
    """Creat sub menu and item for dev C modul
    return submenus dico, items dico"""
    
    submenus = {}
    items = {}
    
    # Sub Menu
    # Goto
    submenus['goto'] = menu_dev_c.add(
        label = sp.msg('Goto'), submenu = True, action = None, name = 'goto', specific = True, group = 'devc')
    # items in Goto sub menu
    # next function
    items['next_function'] = submenus['goto'].add(
        label = sp.msg('Next function'), action = goto.next_function, accelerator = get_shortkey('next_function'), name = "next_function", specific = True, group = 'devc')
    # Previous function
    items['previous_function'] = submenus['goto'].add(
        label = sp.msg('Previous function'), action = goto.previous_function, accelerator = get_shortkey('previous_function'), name = "previous_function", specific = True, group = 'devc')
    # Liste des fonctions
    items['list_function'] = submenus['goto'].add(
        label = sp.msg('LIst of functions'), action = goto.select_function, accelerator = get_shortkey('list_function'), name = "list_function", specific = True, group = 'devc')
    # next struct
    items['next_struct'] = submenus['goto'].add(
        label = sp.msg('Next struct'), 
        action = goto.next_struct, 
        accelerator = get_shortkey('next_struct'), 
        name = "next_struct", 
        specific = True, group = 'devc')
    # Previous struct
    items['previous_struct'] = submenus['goto'].add(
        label = sp.msg('Previous struct'), action = goto.previous_struct, accelerator = get_shortkey('previous_struct'), name = "previous_struct", specific = True, group = 'devc')
    return submenus, items
# end def

def creat_accelerator():
    """ Create accelerators from shorkey dico and return accelerator_active"""
    
    accelerator_active = {}
    # Goto
    # Next level 2 heading.
    #accelerator_active['next_head2'] = win.addAccelerator(
        #get_shortkey('next_head2'), lambda:goto.next_head(HEAD2), True)
    return accelerator_active
# end def

def load_translate_file():
    """Load the lang file to translate markpad"""
    log.h1('Load translate file')
    # Load language
    for lang in(sp.locale, 'english'):
        lang_file = os.path.join(PLUGIN_PATH, lang + '.lng')
        if os.path.isfile(lang_file) :
            # Lang file found
            log('Lang file found : %s' % lang)
            sp.loadTranslation(lang_file)
        # end if
    # end for
# end def

def page_opened(page):
    """Start when new page is openned.
    find file extension and load markPad if a markup language uses this extension""" 
    
    # fetch extension of this new page
    log.h1('Page "%s" opened, search kind of this document' % page.name)
    ext = os.path.splitext(page.file)[1][1:].lower()
    if not ext:
        # This page contains a new file or file without extension.
        log('Page not saved page or file without extension.')
        ext = 'noext'
    # end if
    log('File extension : %s' % ext)
    # Search language for this extension
    if ext in ["c", "h"] :
        # Load module
        menu_dev_c, submenus, items = load_dev_c(page)
    else:
        log('Not C file')
        log('Dev C not loaded for "%s".' % page.name)
    # end else
# end def

## main ##
# Init log systeme
log_file_path = os.path.join(PLUGIN_PATH, 'log_markpad.md')
log = tracer.Tracer(log_file_path)
log.h1('MarkPad trace')
log.print_time()

# Load lng file to translate markpad
load_translate_file()

# Init Markup Manager.

# Add event to load module when new page is open
win.addEvent('pageOpened', page_opened)
# Load module for the initial page
page_opened(win.curPage)
