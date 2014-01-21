# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389373259.029204
_enable_loop = True
_template_filename = 'C:\\Python33\\mystuff\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'top_menu']


# SOURCE LINE 5
from base_app import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def top_menu():
            return render_top_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>My Homepage</title>\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n    <link href="/styles/bootstrap.css" rel="stylesheet">\n')
        # SOURCE LINE 16
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n    <header>\n      <img src="')
        # SOURCE LINE 22
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/images/mystufflogo.png" width="400" height="115" alt="MyStuff Homepage"/>\n      <div id="site_header">MyStuff</div>\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_menu'):
            context['self'].top_menu(**pageargs)
        

        # SOURCE LINE 30
        __M_writer('\n    </header>\n  \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 35
        __M_writer('  \n  \n')
        # SOURCE LINE 38
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer('\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_menu():
            return render_top_menu(context)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer('\n        <a href="/homepage">Home</a>\n        <a href="/homepage/about">About Us</a>\n        <a href="/homepage/contact">Contact</a>\n        <a href="/homepage/terms">Terms</a>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


