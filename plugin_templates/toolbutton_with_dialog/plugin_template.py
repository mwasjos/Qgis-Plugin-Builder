# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PluginTemplate
                                 A QGIS plugin
 plugin_template
                              -------------------
        begin                : 2015-03-17
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Pirmin Kalberer
        email                : pka@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from ..plugin_template import PluginTemplate


class ToolbuttonWithDialogPluginTemplate(PluginTemplate):

    def descr(self):
        return "Tool button with dialog"

    def subdir(self):
        return os.path.dirname(__file__)

    def template_map(self, specification, dialog):
        menu_text = dialog.template_subframe.menu_text.text()
        menu = dialog.template_subframe.menu_location.currentText()
        # Munge the plugin menu function based on user choice
        if menu == 'Plugins':
            add_method = 'addPluginToMenu'
            remove_method = 'removePluginMenu'
        else:
            add_method = 'addPluginTo{}Menu'.format(menu)
            remove_method = 'removePlugin{}Menu'.format(menu)
        self.category = menu
        return {
            # Makefile
            'TemplatePyFiles': '%s_dialog.py' % specification.module_name,
            'TemplateUiFiles': '%s_dialog_base.ui' % specification.module_name,
            'TemplateExtraFiles': 'icon.png',
            'TemplateQrcFiles': 'resources.qrc',
            'TemplateRcFiles': "resources_rc.py",
            # Menu
            'TemplateMenuText': menu_text,
            'TemplateMenuAddMethod': add_method,
            'TemplateMenuRemoveMethod': remove_method,
        }

    def template_files(self, specification):
        result = {
            'module_name_dialog.tmpl':
            '%s_dialog.py' % specification.module_name,
            'module_name_dialog_base.ui.tmpl':
            '%s_dialog_base.ui' % specification.module_name,
            'resources.tmpl': 'resources.qrc',
        }
        if specification.gen_tests:
            result.update({
                'test/test_module_name_dialog.templ':
                'test/test_%s_dialog.py' % specification.module_name,
                'test/test_resources.templ': 'test/test_resources.py'
            })
        return result

    def copy_files(self, specification):
        return {
            'icon.png': 'icon.png'
        }
