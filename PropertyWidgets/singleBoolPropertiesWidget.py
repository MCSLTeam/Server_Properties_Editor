from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QSizePolicy, QSpacerItem, QHBoxLayout
from qfluentwidgets import BodyLabel, CardWidget, LineEdit, SwitchButton

from .baseSinglePropertiesWidget import BaseSinglePropertiesWidget


class BoolPropertiesWidget(CardWidget, BaseSinglePropertiesWidget):
    def __init__(self):
        super().__init__()

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(644, 0))
        self.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.propertyName = LineEdit(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propertyName.sizePolicy().hasHeightForWidth())
        self.propertyName.setSizePolicy(sizePolicy)
        self.propertyName.setMinimumSize(QSize(185, 33))
        self.propertyName.setReadOnly(True)
        self.propertyName.setObjectName("propertyName")

        self.horizontalLayout.addWidget(self.propertyName)
        spacerItem1 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.boolSwitcher = SwitchButton(self)
        self.boolSwitcher.setMinimumSize(QSize(185, 22))
        self.boolSwitcher.setLayoutDirection(Qt.LeftToRight)
        self.boolSwitcher.setChecked(False)
        self.boolSwitcher.setObjectName("boolSwitcher")

        self.horizontalLayout.addWidget(self.boolSwitcher)
        spacerItem2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.tip = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tip.sizePolicy().hasHeightForWidth())
        self.tip.setSizePolicy(sizePolicy)
        self.tip.setMinimumSize(QSize(190, 0))
        self.tip.setWordWrap(True)
        self.tip.setObjectName("tip")

        self.horizontalLayout.addWidget(self.tip)
        spacerItem3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        # self.setObjectName("singleBoolPropertiesWidget")
        self.propertyName.setPlaceholderText("配置项")
        # self.tip.setText("[注释]")

        self.boolSwitcher.checkedChanged.connect(self.onValueChanged)

    def onValueChanged(self, value):
        if value:
            self.valueChanged.emit((self.propertyNameText,"true"))
        else:
            self.valueChanged.emit((self.propertyNameText,"false"))

    def setData(self, name: str, value: str, data: dict):
        super().setData(name, value, data)
        self.boolSwitcher.setChecked(value == "true")
