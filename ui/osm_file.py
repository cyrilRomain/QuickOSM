from builtins import object
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/osm_file.ui'
#
# Created: Wed Jul  8 21:09:07 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ui_osm_file(object):
    def setupUi(self, ui_osm_file):
        ui_osm_file.setObjectName(_fromUtf8("ui_osm_file"))
        ui_osm_file.resize(589, 408)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ui_osm_file)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(ui_osm_file)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 581, 400))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_osmFile = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_osmFile.setObjectName(_fromUtf8("lineEdit_osmFile"))
        self.horizontalLayout.addWidget(self.lineEdit_osmFile)
        self.pushButton_browseOsmFile = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_browseOsmFile.setObjectName(_fromUtf8("pushButton_browseOsmFile"))
        self.horizontalLayout.addWidget(self.pushButton_browseOsmFile)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setText(_fromUtf8("Points"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.checkBox_points = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_points.setText(_fromUtf8(""))
        self.checkBox_points.setChecked(True)
        self.checkBox_points.setObjectName(_fromUtf8("checkBox_points"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBox_points)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setText(_fromUtf8("Lines"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.checkBox_lines = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_lines.setText(_fromUtf8(""))
        self.checkBox_lines.setChecked(True)
        self.checkBox_lines.setObjectName(_fromUtf8("checkBox_lines"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox_lines)
        self.checkBox_multilinestrings = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_multilinestrings.setText(_fromUtf8(""))
        self.checkBox_multilinestrings.setChecked(True)
        self.checkBox_multilinestrings.setObjectName(_fromUtf8("checkBox_multilinestrings"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_multilinestrings)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setText(_fromUtf8("Multipolygons"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.checkBox_multipolygons = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_multipolygons.setText(_fromUtf8(""))
        self.checkBox_multipolygons.setChecked(True)
        self.checkBox_multipolygons.setObjectName(_fromUtf8("checkBox_multipolygons"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_multipolygons)
        self.radioButton_allTags = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_allTags.setChecked(True)
        self.radioButton_allTags.setObjectName(_fromUtf8("radioButton_allTags"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.radioButton_allTags)
        self.groupBox_file = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_file.setTitle(_fromUtf8(""))
        self.groupBox_file.setObjectName(_fromUtf8("groupBox_file"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_file)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_file)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_browseDir = QtGui.QLineEdit(self.groupBox_file)
        self.lineEdit_browseDir.setObjectName(_fromUtf8("lineEdit_browseDir"))
        self.horizontalLayout_3.addWidget(self.lineEdit_browseDir)
        self.pushButton_browse_output_file = QtGui.QPushButton(self.groupBox_file)
        self.pushButton_browse_output_file.setObjectName(_fromUtf8("pushButton_browse_output_file"))
        self.horizontalLayout_3.addWidget(self.pushButton_browse_output_file)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_7 = QtGui.QLabel(self.groupBox_file)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_filePrefix = QtGui.QLineEdit(self.groupBox_file)
        self.lineEdit_filePrefix.setObjectName(_fromUtf8("lineEdit_filePrefix"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_filePrefix)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.groupBox_file)
        self.radioButton_osmConf = QtGui.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_osmConf.setChecked(False)
        self.radioButton_osmConf.setObjectName(_fromUtf8("radioButton_osmConf"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.radioButton_osmConf)
        self.horizontalLayout_osmConf = QtGui.QHBoxLayout()
        self.horizontalLayout_osmConf.setObjectName(_fromUtf8("horizontalLayout_osmConf"))
        self.lineEdit_osmConf = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_osmConf.setObjectName(_fromUtf8("lineEdit_osmConf"))
        self.horizontalLayout_osmConf.addWidget(self.lineEdit_osmConf)
        self.pushButton_browseOsmConf = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_browseOsmConf.setObjectName(_fromUtf8("pushButton_browseOsmConf"))
        self.horizontalLayout_osmConf.addWidget(self.pushButton_browseOsmConf)
        self.pushButton_resetIni = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_resetIni.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_resetIni.setIcon(icon)
        self.pushButton_resetIni.setObjectName(_fromUtf8("pushButton_resetIni"))
        self.horizontalLayout_osmConf.addWidget(self.pushButton_resetIni)
        self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.horizontalLayout_osmConf)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setText(_fromUtf8("Multilinestrings"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton_runQuery = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_runQuery.setObjectName(_fromUtf8("pushButton_runQuery"))
        self.verticalLayout.addWidget(self.pushButton_runQuery)
        self.label_progress = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_progress.setText(_fromUtf8("text progress"))
        self.label_progress.setObjectName(_fromUtf8("label_progress"))
        self.verticalLayout.addWidget(self.label_progress)
        self.progressBar_execution = QtGui.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_execution.setProperty("value", 0)
        self.progressBar_execution.setObjectName(_fromUtf8("progressBar_execution"))
        self.verticalLayout.addWidget(self.progressBar_execution)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(ui_osm_file)
        QtCore.QObject.connect(self.radioButton_allTags, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_file.setEnabled)
        QtCore.QObject.connect(self.radioButton_osmConf, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_osmConf.setEnabled)
        QtCore.QObject.connect(self.radioButton_osmConf, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.pushButton_browseOsmConf.setEnabled)
        QtCore.QObject.connect(self.radioButton_osmConf, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.pushButton_resetIni.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ui_osm_file)

    def retranslateUi(self, ui_osm_file):
        ui_osm_file.setWindowTitle(_translate("ui_osm_file", "QuickOSM - OSM File", None))
        self.label.setText(_translate("ui_osm_file", "OSM File", None))
        self.pushButton_browseOsmFile.setText(_translate("ui_osm_file", "Browse", None))
        self.radioButton_allTags.setText(_translate("ui_osm_file", "All tags", None))
        self.label_2.setText(_translate("ui_osm_file", "Directory", None))
        self.lineEdit_browseDir.setPlaceholderText(_translate("ui_osm_file", "Save to temporary file", None))
        self.pushButton_browse_output_file.setText(_translate("ui_osm_file", "Browse", None))
        self.label_7.setText(_translate("ui_osm_file", "File prefix", None))
        self.radioButton_osmConf.setText(_translate("ui_osm_file", "OSMConf", None))
        self.pushButton_browseOsmConf.setText(_translate("ui_osm_file", "Browse", None))
        self.pushButton_runQuery.setText(_translate("ui_osm_file", "Open", None))

from QuickOSM import resources_rc
