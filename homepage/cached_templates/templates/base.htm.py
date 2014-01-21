# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389653348.904521
_enable_loop = True
_template_filename = 'C:\\Python33\\mystuff\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center_inner', 'center']


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
        def center_inner():
            return render_center_inner(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 12
        __M_writer('  \r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_inner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_inner():
            return render_center_inner(context)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer('\r\n    \r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_inner():
            return render_center_inner(context)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n\r\n')
        # SOURCE LINE 6
        __M_writer('  \t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_inner'):
            context['self'].center_inner(**pageargs)
        

        # SOURCE LINE 8
        __M_writer('  \r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


