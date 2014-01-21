# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389653876.408798
_enable_loop = True
_template_filename = 'C:\\Python33\\mystuff\\homepage\\templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>About MyStuff</title>\r\n</head>\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 29
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
        __M_writer("\r\n  <h2>About MyStuff</h2>\r\nWe started as professors at traditional universities. We still are; we teach classes, we serve in our disciplines, we write textbooks, and we conduct research. We understand what it means to be academics.\r\n\r\n<br>\r\n<br>\r\nSince becoming professors, we had watched textbook prices steadily increase even while publishing and distribution costs decreased.\r\n<br>\r\n<br>\r\n\r\nWe also realized the market for educational materials was shifting. Traditional textbooks were being enveloped by digital materials which offered much more convenience, flexibility, and dynamic content. More and more students were bringing laptops and tablets to school.\r\n<br>\r\n<br>\r\n\r\nWe decided to start new type of publishing company in 2010. We strive for textbooks that not only can be used at the world's best institutions, but also that can remain low cost. Further, we embed section-level videos, adaptive problem sets, and other technologies the modern web provides.\r\n\r\n<br>\r\n<br>\r\nCome, and rediscover the textbook. We think you'll be pleased.\r\n<br>\r\nOur offices are located in the heart of the Rocky Mountains in Orem, Utah, USA. Please contact us by email regarding book adoption, textbook authorship, or other general questions.\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


