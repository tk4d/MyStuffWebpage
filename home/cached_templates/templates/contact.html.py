# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389653976.327676
_enable_loop = True
_template_filename = 'C:\\Python33\\mystuff\\homepage\\templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>Contact MyStuff</title>\r\n</head>\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 30
        __M_writer('  \r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer('\r\n  <h2>Contact Us</h2>\r\n   We love to hear from you!\r\n   <br>\r\n<br>\r\n<h3>Feedback</h3>\r\nIf you have any questions, comments, or ideas, let us know at info@myeducator.com.\r\n<br>\r\n<br>\r\n\r\n<h3>Technical Support</h3>\r\nIf you are experiencing technical errors, please email support@myeducator.com.\r\n<br>\r\n<br>\r\n\r\n<h3>Media</h3>\r\nFor any media or press enquiries, please contact us at press@myeducator.com.\r\n<br>\r\n<br>\r\n<h4>MyEducator, Inc.\r\n1475 W. Center Street\r\nOrem, UT 84057</h4>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


