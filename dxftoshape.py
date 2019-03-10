# -*- coding: utf-8 -*-
"""
/***************************************************************************
 dxftoshp
                                 A QGIS plugin
 extract contour from dxf 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-03-04
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Kim Yonghyun
        email                : queenmedley@gmail.com
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
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from qgis import core, gui
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .dxftoshape_dialog import dxftoshpDialog
import os.path
import ezdxf
import shapefile
import sys


class dxftoshp:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'dxftoshp_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&dxftoshp')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('dxftoshp', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/dxftoshape/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'dxftoshape'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&dxftoshp'),
                action)
            self.iface.removeToolBarIcon(action)

    def file_process(self):
        self.filepath=self.dlg.mQgsFileWidget.filePath()
        print(self.filepath)
        self.dwg=ezdxf.readfile(self.filepath)
        self.msp=self.dwg.modelspace()
        layer_names=[]

        for e in self.msp:
            if e.dxftype() =='LWPOLYLINE' or e.dxftype()=='POLYLINE':
                layer_names.append(e.dxf.layer)
            else :
                pass
        layer_names_2=list(set(layer_names))
        layer_names_2.sort()
        self.dlg.mComboBox.addItems(layer_names_2)
        self.dlg.mComboBox.setSeparator=','

    def layer_process(self):
        self.contour=[]
        self.contour=self.dlg.mComboBox.checkedItems()
        print(self.contour)

    def make_shape(self):
        shp_file=self.filepath[0:len(self.filepath)-4]
        w=shapefile.Writer(shp_file,shapeType=13)
        w.field('Layer','C',size=20)
        w.field('handle','C',size=20)
        w.field('Elevation','N',size=5)
        print("make shape file",shp_file)

        for e in self.msp:
            if e.dxftype()=='LWPOLYLINE' or 'POLYLINE':
                if e.dxf.layer in self.contour:
                    xy=e.get_points()
                    xyz=[]
                    r=[]
#                    print(e.dxf.layer,e.dxf.elevation,e.dxf.count)
                    for x,y,a,b,c in xy:
                        xyz=[x,y,e.dxf.elevation]
                        r.append(xyz)
                    if e.closed : 
                        r.append(r[0])
                    else :
                        pass
                    w.linez([r])
                    w.record(e.dxf.layer,e.dxf.handle,e.dxf.elevation)
                    print(r)
                else :
                    pass
            else :
                pass
        w.close()
        layer=self.iface.addVectorLayer(shp_file+".shp","contour","ogr")
        self.iface.actionExit()

#        if not layer.isValid():
#            print("Layer is not valid")
#        else :
#            print(shp_file+".shp")

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = dxftoshpDialog()

        self.dlg.mComboBox.checkedItemsChanged.connect(self.layer_process)
        self.dlg.mQgsFileWidget.fileChanged.connect(self.file_process)
        self.dlg.button_box.accepted.connect(self.make_shape)

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass