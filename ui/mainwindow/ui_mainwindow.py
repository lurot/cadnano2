# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 792)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStatusTip("")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(7)
        self.splitter.setObjectName("splitter")
        self.sliceGraphicsView = CustomQGraphicsView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliceGraphicsView.sizePolicy().hasHeightForWidth())
        self.sliceGraphicsView.setSizePolicy(sizePolicy)
        self.sliceGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.sliceGraphicsView.setBaseSize(QtCore.QSize(480, 0))
        self.sliceGraphicsView.setMouseTracking(True)
        self.sliceGraphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.sliceGraphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sliceGraphicsView.setLineWidth(0)
        self.sliceGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sliceGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sliceGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.sliceGraphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.sliceGraphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.sliceGraphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.sliceGraphicsView.setObjectName("sliceGraphicsView")
        self.pathGraphicsView = CustomQGraphicsView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathGraphicsView.sizePolicy().hasHeightForWidth())
        self.pathGraphicsView.setSizePolicy(sizePolicy)
        self.pathGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.pathGraphicsView.setMouseTracking(True)
        self.pathGraphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pathGraphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pathGraphicsView.setLineWidth(0)
        self.pathGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.pathGraphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.pathGraphicsView.setObjectName("pathGraphicsView")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.topToolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topToolBar.sizePolicy().hasHeightForWidth())
        self.topToolBar.setSizePolicy(sizePolicy)
        self.topToolBar.setBaseSize(QtCore.QSize(550, 0))
        self.topToolBar.setIconSize(QtCore.QSize(24, 24))
        self.topToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.topToolBar.setObjectName("topToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.topToolBar)
        self.rightToolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightToolBar.sizePolicy().hasHeightForWidth())
        self.rightToolBar.setSizePolicy(sizePolicy)
        self.rightToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.rightToolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rightToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.rightToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.rightToolBar.setObjectName("rightToolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.rightToolBar)
        self.leftToolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftToolBar.sizePolicy().hasHeightForWidth())
        self.leftToolBar.setSizePolicy(sizePolicy)
        self.leftToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.leftToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.leftToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.leftToolBar.setObjectName("leftToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.leftToolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPlugins = QtWidgets.QMenu(self.menubar)
        self.menuPlugins.setObjectName("menuPlugins")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/filetools/new"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/filetools/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filetools/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setIcon(icon2)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_a_Copy = QtWidgets.QAction(MainWindow)
        self.actionSave_a_Copy.setObjectName("actionSave_a_Copy")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionSVG = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/filetools/svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSVG.setIcon(icon3)
        self.actionSVG.setObjectName("actionSVG")
        self.actionX3D = QtWidgets.QAction(MainWindow)
        self.actionX3D.setObjectName("actionX3D")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionNewHoneycombPart = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/parttools/new-honeycomb"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewHoneycombPart.setIcon(icon4)
        self.actionNewHoneycombPart.setObjectName("actionNewHoneycombPart")
        self.actionPathBreak = QtWidgets.QAction(MainWindow)
        self.actionPathBreak.setCheckable(True)
        self.actionPathBreak.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pathtools/break"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathBreak.setIcon(icon5)
        self.actionPathBreak.setObjectName("actionPathBreak")
        self.actionPathSelect = QtWidgets.QAction(MainWindow)
        self.actionPathSelect.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pathtools/select"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathSelect.setIcon(icon6)
        self.actionPathSelect.setObjectName("actionPathSelect")
        self.actionSliceFirst = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/slicetools/go-first"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSliceFirst.setIcon(icon7)
        self.actionSliceFirst.setObjectName("actionSliceFirst")
        self.actionSliceLast = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/slicetools/go-last"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSliceLast.setIcon(icon8)
        self.actionSliceLast.setObjectName("actionSliceLast")
        self.actionPathErase = QtWidgets.QAction(MainWindow)
        self.actionPathErase.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/pathtools/erase"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathErase.setIcon(icon9)
        self.actionPathErase.setObjectName("actionPathErase")
        self.actionPathPencil = QtWidgets.QAction(MainWindow)
        self.actionPathPencil.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/pathtools/force"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathPencil.setIcon(icon10)
        self.actionPathPencil.setObjectName("actionPathPencil")
        self.actionPathInsertion = QtWidgets.QAction(MainWindow)
        self.actionPathInsertion.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/pathtools/insert"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathInsertion.setIcon(icon11)
        self.actionPathInsertion.setObjectName("actionPathInsertion")
        self.actionNewSquarePart = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/parttools/new-square"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewSquarePart.setIcon(icon12)
        self.actionNewSquarePart.setObjectName("actionNewSquarePart")
        self.actionPathSkip = QtWidgets.QAction(MainWindow)
        self.actionPathSkip.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/pathtools/skip"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathSkip.setIcon(icon13)
        self.actionPathSkip.setObjectName("actionPathSkip")
        self.actionRenumber = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/slicetools/renumber"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRenumber.setIcon(icon14)
        self.actionRenumber.setObjectName("actionRenumber")
        self.actionPathPaint = QtWidgets.QAction(MainWindow)
        self.actionPathPaint.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/pathtools/paint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathPaint.setIcon(icon15)
        self.actionPathPaint.setObjectName("actionPathPaint")
        self.actionPathAddSeq = QtWidgets.QAction(MainWindow)
        self.actionPathAddSeq.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/pathtools/addseq"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathAddSeq.setIcon(icon16)
        self.actionPathAddSeq.setObjectName("actionPathAddSeq")
        self.actionExportStaples = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/filetools/csv"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportStaples.setIcon(icon17)
        self.actionExportStaples.setObjectName("actionExportStaples")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/pathtools/modify"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModify.setIcon(icon18)
        self.actionModify.setObjectName("actionModify")
        self.actionCadnanoWebsite = QtWidgets.QAction(MainWindow)
        self.actionCadnanoWebsite.setObjectName("actionCadnanoWebsite")
        self.actionFeedback = QtWidgets.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionFilterPart = QtWidgets.QAction(MainWindow)
        self.actionFilterPart.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/parttools/filter-part"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterPart.setIcon(icon19)
        self.actionFilterPart.setObjectName("actionFilterPart")
        self.actionFilterEndpoint = QtWidgets.QAction(MainWindow)
        self.actionFilterEndpoint.setCheckable(True)
        self.actionFilterEndpoint.setChecked(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/parttools/filter-endpoint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterEndpoint.setIcon(icon20)
        self.actionFilterEndpoint.setObjectName("actionFilterEndpoint")
        self.actionFilterXover = QtWidgets.QAction(MainWindow)
        self.actionFilterXover.setCheckable(True)
        self.actionFilterXover.setChecked(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/parttools/filter-xover"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterXover.setIcon(icon21)
        self.actionFilterXover.setText("")
        self.actionFilterXover.setObjectName("actionFilterXover")
        self.actionFiltersLabel = QtWidgets.QAction(MainWindow)
        self.actionFiltersLabel.setEnabled(False)
        self.actionFiltersLabel.setObjectName("actionFiltersLabel")
        self.actionFilterStrand = QtWidgets.QAction(MainWindow)
        self.actionFilterStrand.setCheckable(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/parttools/filter-strand"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterStrand.setIcon(icon22)
        self.actionFilterStrand.setObjectName("actionFilterStrand")
        self.actionFilterHandle = QtWidgets.QAction(MainWindow)
        self.actionFilterHandle.setCheckable(True)
        self.actionFilterHandle.setChecked(False)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/parttools/filter-handle"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterHandle.setIcon(icon23)
        self.actionFilterHandle.setObjectName("actionFilterHandle")
        self.actionFilterScaf = QtWidgets.QAction(MainWindow)
        self.actionFilterScaf.setCheckable(True)
        self.actionFilterScaf.setChecked(True)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/parttools/filter-scaf"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterScaf.setIcon(icon24)
        self.actionFilterScaf.setObjectName("actionFilterScaf")
        self.actionFilterStap = QtWidgets.QAction(MainWindow)
        self.actionFilterStap.setCheckable(True)
        self.actionFilterStap.setChecked(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/parttools/filter-stap"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterStap.setIcon(icon25)
        self.actionFilterStap.setObjectName("actionFilterStap")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAutoStaple = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/pathtools/autostaple"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAutoStaple.setIcon(icon26)
        self.actionAutoStaple.setObjectName("actionAutoStaple")
        self.topToolBar.addAction(self.actionNew)
        self.topToolBar.addAction(self.actionOpen)
        self.topToolBar.addAction(self.actionSave)
        self.topToolBar.addAction(self.actionSVG)
        self.topToolBar.addAction(self.actionExportStaples)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.actionNewHoneycombPart)
        self.topToolBar.addAction(self.actionNewSquarePart)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.actionAutoStaple)
        self.topToolBar.addAction(self.actionFiltersLabel)
        self.topToolBar.addAction(self.actionFilterScaf)
        self.topToolBar.addAction(self.actionFilterStap)
        self.topToolBar.addAction(self.actionFilterHandle)
        self.topToolBar.addAction(self.actionFilterEndpoint)
        self.topToolBar.addAction(self.actionFilterXover)
        self.topToolBar.addAction(self.actionFilterStrand)
        self.rightToolBar.addAction(self.actionPathSelect)
        self.rightToolBar.addAction(self.actionPathPencil)
        self.rightToolBar.addAction(self.actionPathBreak)
        self.rightToolBar.addAction(self.actionPathInsertion)
        self.rightToolBar.addAction(self.actionPathSkip)
        self.rightToolBar.addAction(self.actionPathPaint)
        self.rightToolBar.addAction(self.actionPathAddSeq)
        self.leftToolBar.addAction(self.actionSliceFirst)
        self.leftToolBar.addAction(self.actionSliceLast)
        self.leftToolBar.addAction(self.actionRenumber)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionModify)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cadnano"))
        self.topToolBar.setWindowTitle(_translate("MainWindow", "Main Toolbar"))
        self.rightToolBar.setWindowTitle(_translate("MainWindow", "Path Tools"))
        self.leftToolBar.setWindowTitle(_translate("MainWindow", "Slice Tools"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuPlugins.setTitle(_translate("MainWindow", "Plugins"))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionSave_a_Copy.setText(_translate("MainWindow", "Save a Copy..."))
        self.actionPrint.setText(_translate("MainWindow", "Print..."))
        self.actionSVG.setText(_translate("MainWindow", "SVG"))
        self.actionX3D.setText(_translate("MainWindow", "X3D"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionNewHoneycombPart.setText(_translate("MainWindow", "Honeycomb"))
        self.actionNewHoneycombPart.setToolTip(_translate("MainWindow", "Click to add new part with honeycomb lattice"))
        self.actionPathBreak.setText(_translate("MainWindow", "Break Tool"))
        self.actionPathBreak.setIconText(_translate("MainWindow", "Break"))
        self.actionPathBreak.setToolTip(_translate("MainWindow", "(B)reak Tool"))
        self.actionPathBreak.setShortcut(_translate("MainWindow", "B"))
        self.actionPathSelect.setText(_translate("MainWindow", "Select"))
        self.actionPathSelect.setIconText(_translate("MainWindow", "Select"))
        self.actionPathSelect.setToolTip(_translate("MainWindow", "Select Tool (v)"))
        self.actionPathSelect.setShortcut(_translate("MainWindow", "V"))
        self.actionSliceFirst.setText(_translate("MainWindow", "First"))
        self.actionSliceFirst.setToolTip(_translate("MainWindow", "Move the slice bar to the first position."))
        self.actionSliceLast.setText(_translate("MainWindow", "Last"))
        self.actionSliceLast.setToolTip(_translate("MainWindow", "Move the slice bar to the last position."))
        self.actionPathErase.setText(_translate("MainWindow", "Erase"))
        self.actionPathErase.setToolTip(_translate("MainWindow", "(E)rase Tool"))
        self.actionPathPencil.setText(_translate("MainWindow", "Pencil"))
        self.actionPathPencil.setToolTip(_translate("MainWindow", "Pe(n)cil Tool"))
        self.actionPathPencil.setShortcut(_translate("MainWindow", "N"))
        self.actionPathInsertion.setText(_translate("MainWindow", "Insert"))
        self.actionPathInsertion.setToolTip(_translate("MainWindow", "(I)nsert Tool"))
        self.actionPathInsertion.setShortcut(_translate("MainWindow", "I"))
        self.actionNewSquarePart.setText(_translate("MainWindow", "Square"))
        self.actionNewSquarePart.setToolTip(_translate("MainWindow", "Click to add new part with square lattice"))
        self.actionPathSkip.setText(_translate("MainWindow", "Skip"))
        self.actionPathSkip.setToolTip(_translate("MainWindow", "(S)kip Tool"))
        self.actionPathSkip.setShortcut(_translate("MainWindow", "S"))
        self.actionRenumber.setText(_translate("MainWindow", "Rnum"))
        self.actionRenumber.setToolTip(_translate("MainWindow", "Renumber Slice helices according to helix ordering in Path panel."))
        self.actionPathPaint.setText(_translate("MainWindow", "Paint"))
        self.actionPathPaint.setToolTip(_translate("MainWindow", "(P)aint Tool"))
        self.actionPathPaint.setShortcut(_translate("MainWindow", "P"))
        self.actionPathAddSeq.setText(_translate("MainWindow", "Seq"))
        self.actionPathAddSeq.setToolTip(_translate("MainWindow", "(A)dd Sequence Tool"))
        self.actionPathAddSeq.setShortcut(_translate("MainWindow", "A"))
        self.actionExportStaples.setText(_translate("MainWindow", "Export"))
        self.actionExportStaples.setToolTip(_translate("MainWindow", "export oligos as *.CSV"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionModify.setText(_translate("MainWindow", "Modify mode"))
        self.actionModify.setToolTip(_translate("MainWindow", "Modify mode"))
        self.actionCadnanoWebsite.setText(_translate("MainWindow", "cadnano Website"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionFilterPart.setText(_translate("MainWindow", "Parts"))
        self.actionFilterPart.setToolTip(_translate("MainWindow", "Part-selection mode"))
        self.actionFilterEndpoint.setToolTip(_translate("MainWindow", "(E)ndpoints"))
        self.actionFilterEndpoint.setShortcut(_translate("MainWindow", "E"))
        self.actionFilterXover.setToolTip(_translate("MainWindow", "(X)overs"))
        self.actionFilterXover.setShortcut(_translate("MainWindow", "X"))
        self.actionFiltersLabel.setText(_translate("MainWindow", "Selectable:"))
        self.actionFiltersLabel.setToolTip(_translate("MainWindow", "Selection Filters"))
        self.actionFilterStrand.setToolTip(_translate("MainWindow", "stran(D)s"))
        self.actionFilterStrand.setShortcut(_translate("MainWindow", "D"))
        self.actionFilterHandle.setToolTip(_translate("MainWindow", "(H)andles"))
        self.actionFilterHandle.setShortcut(_translate("MainWindow", "H"))
        self.actionFilterScaf.setToolTip(_translate("MainWindow", "s(C)affold"))
        self.actionFilterScaf.setShortcut(_translate("MainWindow", "C"))
        self.actionFilterStap.setToolTip(_translate("MainWindow", "s(T)aple"))
        self.actionFilterStap.setShortcut(_translate("MainWindow", "T"))
        self.actionAbout.setText(_translate("MainWindow", "About cadnano"))
        self.actionAutoStaple.setText(_translate("MainWindow", "AutoStaple"))
        self.actionAutoStaple.setToolTip(_translate("MainWindow", "Create staple strands complementary to existing scaffold."))

from views.customqgraphicsview import CustomQGraphicsView
import ui.mainwindow.icons_rc
