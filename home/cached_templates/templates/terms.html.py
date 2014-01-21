# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389654268.967671
_enable_loop = True
_template_filename = 'C:\\Python33\\mystuff\\homepage\\templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>MyStuff Terms</title>\r\n</head>\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 79
        __M_writer('  \r\n\r\n</body>\r\n</html>')
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
        __M_writer('\r\n <h2> Web Site Terms and Conditions of Use</h2>\r\n<h3>1. Terms</h3>\r\n<br>\r\n<br>\r\n\r\nBy accessing this web site, you are agreeing to be bound by these web site Terms and Conditions of Use, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using or accessing this site. The materials contained in this web site are protected by applicable copyright and trade mark law.\r\n<br>\r\n<br>\r\n<h3>2. Use License</h3>\r\n<br>\r\n<br>\r\nPermission is granted to temporarily download one copy of the materials (information or software) on MyEducator Inc\'s web site for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:\r\nmodify or copy the materials;\r\nuse the materials for any commercial purpose, or for any public display (commercial or non-commercial);\r\nattempt to decompile or reverse engineer any software contained on MyEducator Inc\'s web site;\r\nremove any copyright or other proprietary notations from the materials; or\r\ntransfer the materials to another person or "mirror" the materials on any other server.\r\nThis license shall automatically terminate if you violate any of these restrictions and may be terminated by MyEducator Inc at any time. Upon terminating your viewing of these materials or upon the termination of this license, you must destroy any downloaded materials in your possession whether in electronic or printed format.\r\n<br>\r\n<br>\r\n<h3>3. Disclaimer</h3>\r\n<br>\r\n<br>\r\nThe materials on MyEducator Inc\'s web site are provided "as is". MyEducator Inc makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties, including without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights. Further, MyEducator Inc does not warrant or make any representations concerning the accuracy, likely results, or reliability of the use of the materials on its Internet web site or otherwise relating to such materials or on any sites linked to this site.\r\n<br>\r\n<br>\r\n<h3>4. Limitations</h3>\r\n<br>\r\n<br>\r\nIn no event shall MyEducator Inc or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption,) arising out of the use or inability to use the materials on MyEducator Inc\'s Internet site, even if MyEducator Inc or a MyEducator Inc authorized representative has been notified orally or in writing of the possibility of such damage. Because some jurisdictions do not allow limitations on implied warranties, or limitations of liability for consequential or incidental damages, these limitations may not apply to you.\r\n<br>\r\n<br>\r\n\r\n<h3>5. Revisions and Errata</h3>\r\n<br>\r\n<br>\r\n\r\nThe materials appearing on MyEducator Inc\'s web site could include technical, typographical, or photographic errors. MyEducator Inc does not warrant that any of the materials on its web site are accurate, complete, or current. MyEducator Inc may make changes to the materials contained on its web site at any time without notice. MyEducator Inc does not, however, make any commitment to update the materials.\r\n<br>\r\n<br>\r\n<h3>6. Links</h3>\r\n<br>\r\n<br>\r\nMyEducator Inc has not reviewed all of the sites linked to its Internet web site and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by MyEducator Inc of the site. Use of any such linked web site is at the user\'s own risk.\r\n<br>\r\n<br>\r\n<h3>7. Site Terms of Use Modifications</h3>\r\n<br>\r\n<br>\r\nMyEducator Inc may revise these terms of use for its web site at any time without notice. By using this web site you are agreeing to be bound by the then current version of these Terms and Conditions of Use.\r\n<br>\r\n<br>\r\n<h3>8. Governing Law</h3>\r\n<br>\r\n<br>\r\nAny claim relating to MyEducator Inc\'s web site shall be governed by the laws of the State of Utah without regard to its conflict of law provisions.\r\n\r\nGeneral Terms and Conditions applicable to Use of a Web Site.\r\n\r\nPrivacy Policy\r\nYour privacy is very important to us. Accordingly, we have developed this Policy in order for you to understand how we collect, use, communicate and disclose and make use of personal information. The following outlines our privacy policy.\r\n\r\nBefore or at the time of collecting personal information, we will identify the purposes for which information is being collected.\r\nWe will collect and use of personal information solely with the objective of fulfilling those purposes specified by us and for other compatible purposes, unless we obtain the consent of the individual concerned or as required by law.\r\nWe will only retain personal information as long as necessary for the fulfillment of those purposes.\r\nWe will collect personal information by lawful and fair means and, where appropriate, with the knowledge or consent of the individual concerned.\r\nPersonal data should be relevant to the purposes for which it is to be used, and, to the extent necessary for those purposes, should be accurate, complete, and up-to-date.\r\nWe will protect personal information by reasonable security safeguards against loss or theft, as well as unauthorized access, disclosure, copying, use or modification.\r\nWe will make readily available to customers information about our policies and practices relating to the management of personal information.\r\nWe are committed to conducting our business in accordance with these principles in order to ensure that the confidentiality of personal information is protected and maintained.\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


