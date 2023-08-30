from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy, QSpacerItem, QHBoxLayout
from qfluentwidgets import BodyLabel, CardWidget, LineEdit, SpinBox

from .baseSinglePropertiesWidget import BaseSinglePropertiesWidget


class IntPropertiesWidget(CardWidget, BaseSinglePropertiesWidget):
    def __init__(self):
        super().__init__()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(644, 0))
        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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

        self.horizontalLayout_2.addWidget(self.propertyName)
        spacerItem1 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.intSpinBox = SpinBox(self)
        self.intSpinBox.setMinimumSize(QSize(185, 33))

        self.horizontalLayout_2.addWidget(self.intSpinBox)
        spacerItem2 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.tip = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tip.sizePolicy().hasHeightForWidth())
        self.tip.setSizePolicy(sizePolicy)
        self.tip.setMinimumSize(QSize(190, 0))
        self.tip.setWordWrap(True)
        self.tip.setObjectName("tip")

        self.horizontalLayout_2.addWidget(self.tip)
        spacerItem3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        # self.intSpinBox.setObjectName("intSpinBox")
        # self.setObjectName("singleIntPropertiesWidget")
        self.propertyName.setPlaceholderText("配置项")
        # self.tip.setText("[注释]")

        self.intSpinBox.valueChanged.connect(self.onValueChanged)

    def setData(self, name: str, value: str, data: dict):
        super().setData(name, value, data)
        self.intSpinBox.setRange(-2147483648, 2147483647)
        self.intSpinBox.setValue(int(value))
        if _range := data.get("range", []):
            self.intSpinBox.setRange(*_range)
            self.tip.setText(self.tip.text() + f"\n>>>>  [注释] 取值范围: {_range[0]} ~ {_range[1]}  <<<<")