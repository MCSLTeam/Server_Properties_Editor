from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QIcon
from MCSL2Lib.singleton import Singleton
from PyQt5.QtWidgets import (
    QWidget,
    QSizePolicy,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QSpacerItem,
)
from qfluentwidgets import (
    BodyLabel,
    ComboBox,
    PrimaryPushButton,
    SmoothScrollArea,
    StrongBodyLabel,
    SubtitleLabel,
    TitleLabel,
    ToolButton,
    TransparentToolButton,
    FluentIcon as FIF,
)
from MCSL2Lib.variables import GlobalMCSL2Variables
from .speIcons import *  # noqa: F401
from .speVariables import SPEIconsSetter, SPEVariables

@Singleton
class SPEMainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("SPEMainUI")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.undoBtn = TransparentToolButton(self)
        self.undoBtn.setObjectName("undoBtn")
        self.undoBtn.setIcon(QIcon(SPEIconsSetter.Undo()))

        self.gridLayout.addWidget(self.undoBtn, 4, 3, 1, 1)
        self.StrongBodyLabel = StrongBodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.StrongBodyLabel.sizePolicy().hasHeightForWidth()
        )
        self.StrongBodyLabel.setSizePolicy(sizePolicy)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")

        self.gridLayout.addWidget(self.StrongBodyLabel, 4, 1, 1, 1)
        self.saveBtn = PrimaryPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setObjectName("saveBtn")

        self.gridLayout.addWidget(self.saveBtn, 4, 5, 1, 1)
        self.titleLimitWidget = QWidget(self)
        self.titleLimitWidget.setObjectName("titleLimitWidget")

        self.gridLayout_3 = QGridLayout(self.titleLimitWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.titleLabel = TitleLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")

        self.gridLayout_3.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.titleLimitWidget, 1, 1, 1, 2)
        self.selectServerComboBox = ComboBox(self)
        self.selectServerComboBox.setObjectName("selectServerComboBox")

        self.gridLayout.addWidget(self.selectServerComboBox, 4, 2, 1, 1)
        self.redoBtn = TransparentToolButton(self)
        self.redoBtn.setObjectName("redoBtn")
        self.redoBtn.setIcon(QIcon(SPEIconsSetter.Redo()))

        self.gridLayout.addWidget(self.redoBtn, 4, 4, 1, 1)
        self.propertiesSmoothScrollArea = SmoothScrollArea(self)
        self.propertiesSmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.propertiesSmoothScrollArea.setWidgetResizable(True)
        self.propertiesSmoothScrollArea.setObjectName("propertiesSmoothScrollArea")

        self.propertiesScrollAreaWidgetContents = QWidget()
        self.propertiesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 664, 327))
        self.propertiesScrollAreaWidgetContents.setObjectName(
            "propertiesScrollAreaWidgetContents"
        )

        self.gridLayout_2 = QGridLayout(self.propertiesScrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.propertiesSmoothScrollArea.setWidget(
            self.propertiesScrollAreaWidgetContents
        )
        self.gridLayout.addWidget(self.propertiesSmoothScrollArea, 6, 1, 1, 5)
        spacerItem = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.subtitleWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.subtitleWidget.sizePolicy().hasHeightForWidth()
        )
        self.subtitleWidget.setSizePolicy(sizePolicy)
        self.subtitleWidget.setMinimumSize(QSize(0, 30))
        self.subtitleWidget.setObjectName("subtitleWidget")

        self.horizontalLayout = QHBoxLayout(self.subtitleWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.propertyNameSTitle = SubtitleLabel(self.subtitleWidget)
        self.propertyNameSTitle.setObjectName("propertyNameSTitle")

        self.horizontalLayout.addWidget(self.propertyNameSTitle)
        self.propertyValueSTitle = SubtitleLabel(self.subtitleWidget)
        self.propertyValueSTitle.setObjectName("propertyValueSTitle")

        self.horizontalLayout.addWidget(self.propertyValueSTitle)
        self.tipSTitle = SubtitleLabel(self.subtitleWidget)
        self.tipSTitle.setObjectName("tipSTitle")

        self.horizontalLayout.addWidget(self.tipSTitle)
        self.gridLayout.addWidget(self.subtitleWidget, 5, 1, 1, 5)
        self.updateWidget = QWidget(self)
        self.updateWidget.setObjectName("updateWidget")

        self.gridLayout_4 = QGridLayout(self.updateWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.checkUpdateBtn = ToolButton(FIF.UPDATE, self.updateWidget)
        self.checkUpdateBtn.setObjectName("checkUpdateBtn")

        self.gridLayout_4.addWidget(self.checkUpdateBtn, 0, 1, 1, 1)
        self.widget = QWidget(self.updateWidget)
        self.widget.setObjectName("widget")

        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.currentVersionTitle = StrongBodyLabel(self.widget)
        self.currentVersionTitle.setObjectName("currentVersionTitle")

        self.verticalLayout_2.addWidget(self.currentVersionTitle)
        self.currentVersionValue = BodyLabel(self.widget)
        self.currentVersionValue.setObjectName("currentVersionValue")

        self.verticalLayout_2.addWidget(self.currentVersionValue)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.updateWidget, 1, 3, 1, 3)

        self.StrongBodyLabel.setText("选择服务器：")
        self.saveBtn.setText("保存")
        self.titleLabel.setText("服务器server.properties编辑器")
        self.propertyNameSTitle.setText("配置项")
        self.propertyValueSTitle.setText("值")
        self.tipSTitle.setText("注释")
        self.currentVersionTitle.setText("当前版本：")
        self.currentVersionValue.setText(SPEVariables.speVersion)
        self.propertiesSmoothScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
