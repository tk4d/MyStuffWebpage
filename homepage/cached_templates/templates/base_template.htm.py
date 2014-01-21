# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389654600.423941
_enable_loop = True
_template_filename = 'C:\\Python33\\mystuff\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'leftSide', 'center', 'right_side', 'footer']


# SOURCE LINE 5
from base_app import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def center():
            return render_center(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def right_side():
            return render_right_side(context._locals(__M_locals))
        def leftSide():
            return render_leftSide(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title></title>\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n    <link href="/static/base_app/styles/bootstrap.css" rel="stylesheet">\n    <script src="/static/base_app/scripts/bootstrap.js"></script>\n\n\n')
        # SOURCE LINE 19
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n  \n    <header>\n        <div class ="row">\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 52
        __M_writer('\n\n  </div><!-- /.navbar-collapse -->\n</nav>\n            \n       \n    </header>\n\n\n<div class="row">\n        <div class="col-md-2">\n         ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'leftSide'):
            context['self'].leftSide(**pageargs)
        

        # SOURCE LINE 76
        __M_writer('\n\n        </div>\n        <div class="navbar navbar-fixed-bottom">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 85
        __M_writer(' \n      </div> \n        <div class="col-md-9">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 90
        __M_writer(' \n        </div>\n\n        <div class="col-md-1">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_side'):
            context['self'].right_side(**pageargs)
        

        # SOURCE LINE 96
        __M_writer(' \n      </div>\n</div>\n\n  \n')
        # SOURCE LINE 102
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer('\n            <nav class="navbar navbar-default" role="navigation">\n  <!-- Brand and toggle get grouped for better mobile display -->\n  <div class="navbar-header">\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n      <span class="sr-only">Toggle navigation</span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n    </button>\n    <a class="navbar-brand" href="/homepage">MyStuff</a>\n  </div>\n\n  <!-- Collect the nav links, forms, and other content for toggling -->\n  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n    <ul class="nav navbar-nav">\n      <li><a href="/homepage/about">About Us</a></li>\n      <li><a href="/homepage/terms">Terms</a></li>\n      <li><a href="/homepage/contact">Contact</a></li>\n    </ul>\n    <form class="navbar-form navbar-left" role="search">\n      <div class="form-group">\n        <input type="text" class="form-control" placeholder="Search">\n      </div>\n      <button type="submit" class="btn btn-default">Submit</button>\n    </form>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_leftSide(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def leftSide():
            return render_leftSide(context)
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer('\n        <ul>\n        <a href="/homepage" class="btn btn-primary">Home <span class="badge">42</span></a>\n        <br>\n        <br>\n        <a href="/homepage/about" class="btn btn-success">About Us</a>\n        <br>\n        <br>\n        <a href="/homepage/contact" class="btn btn-warning">Contact</a>\n        <br>\n        <br>\n        <a href="/homepage/terms" class="btn btn-danger">Terms</a>\n        </ul>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        # SOURCE LINE 88
        __M_writer('\n        \n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_side():
            return render_right_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer('\n        <span class="label label-danger">"I\'m a LABEL!"</span>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 80
        __M_writer('\n        <button type="button" class="btn btn-default btn-lg">\n  <span class="glyphicon glyphicon-th-large"></span>\n   Copyright 2014 \n</button>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


