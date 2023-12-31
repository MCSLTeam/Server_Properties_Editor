from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem, QSizePolicy
from qfluentwidgets import BodyLabel, CardWidget, LineEdit

from .baseSinglePropertiesWidget import BaseSinglePropertiesWidget


class PropertiesWidget(CardWidget, BaseSinglePropertiesWidget):
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
        self.propertyName.setReadOnly(True)
        self.propertyName.setReadOnly(True)
        self.propertyName.setReadOnly(True)
        self.propertyName.setReadOnly(True)
        self.propertyName.setReadOnly(True)
        self.propertyName.setReadOnly(True)
        self.propertyName.setReadOnly(True)
        self.propertyName.setObjectName("propertyName")

        self.horizontalLayout.addWidget(self.propertyName)
        spacerItem1 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.propertyValue = LineEdit(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.propertyValue.sizePolicy().hasHeightForWidth()
        )
        self.propertyValue.setSizePolicy(sizePolicy)
        self.propertyValue.setMinimumSize(QSize(185, 33))
        self.propertyValue.setObjectName("propertyValue")

        self.horizontalLayout.addWidget(self.propertyValue)
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
        self.propertyName.setPlaceholderText("配置项")
        # self.propertyValue.setPlaceholderText("值")
        self.tip.setText("[注释]")

        self.propertyValue.textChanged.connect(self.onValueChanged)

    def setData(self, name: str, value: str, data: dict):
        super().setData(name, value, data)
        self.propertyValue.setText(value)
