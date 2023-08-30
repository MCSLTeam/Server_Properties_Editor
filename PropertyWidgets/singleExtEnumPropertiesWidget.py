from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QSizePolicy, QSpacerItem, QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import BodyLabel, CardWidget, LineEdit, RadioButton, ComboBox

from .baseSinglePropertiesWidget import BaseSinglePropertiesWidget


class ExtEnumPropertiesWidget(CardWidget, BaseSinglePropertiesWidget):
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
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
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

        self.verticalLayout_2.addWidget(self.propertyName)
        self.placeHolderWidget = QWidget(self)
        self.placeHolderWidget.setMinimumSize(QSize(0, 33))
        self.placeHolderWidget.setObjectName("placeHolderWidget")

        self.verticalLayout_2.addWidget(self.placeHolderWidget)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.extEnumComboxBox = ComboBox(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extEnumComboxBox.sizePolicy().hasHeightForWidth())
        self.extEnumComboxBox.setSizePolicy(sizePolicy)
        self.extEnumComboxBox.setMinimumSize(QSize(180, 0))
        self.extEnumComboxBox.setObjectName("extEnumComboxBox")

        self.verticalLayout.addWidget(self.extEnumComboxBox)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.extEnumToggler = RadioButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extEnumToggler.sizePolicy().hasHeightForWidth())
        self.extEnumToggler.setSizePolicy(sizePolicy)
        self.extEnumToggler.setObjectName("extEnumToggler")

        self.horizontalLayout.addWidget(self.extEnumToggler)
        self.extEnumValue = LineEdit(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extEnumValue.sizePolicy().hasHeightForWidth())
        self.extEnumValue.setSizePolicy(sizePolicy)
        self.extEnumValue.setMinimumSize(QSize(111, 33))
        self.extEnumValue.setMaximumSize(QSize(111, 33))
        self.extEnumValue.setObjectName("extEnumValue")
        
        self.horizontalLayout.addWidget(self.extEnumValue)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
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
        spacerItem7 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)

        # self.extEnumValue.setObjectName("extEnumValue")
        # self.extEnumToggler.setObjectName("extEnumToggler")
        # self.extEnumComboxBox.setObjectName("extEnumComboxBox")
        # self.setObjectName("singleExtEnumPropertiesWidget")
        self.propertyName.setPlaceholderText("配置项")
        self.extEnumToggler.setText("其他")
        # self.tip.setText("[注释]")

        self.extEnumValue.textChanged.connect(self.onWidgetStateChanged)
        self.extEnumToggler.toggled.connect(self.onWidgetStateChanged)
        self.extEnumComboxBox.currentTextChanged.connect(self.onWidgetStateChanged)

    def onWidgetStateChanged(self, value):
        if self.extEnumToggler.isChecked():
            self.extEnumValue.setEnabled(True)
            self.extEnumComboxBox.setEnabled(False)
            self.onValueChanged(self.extEnumValue.text())
        else:
            self.extEnumValue.setEnabled(False)
            self.extEnumComboxBox.setEnabled(True)
            self.onValueChanged(self.extEnumComboxBox.currentText())

    def setData(self, name: str, value: str, data: dict):
        super().setData(name, value, data)
        values = data.get("values", [])
        values = list(map(lambda x: str(x), values))
        self.extEnumComboxBox.addItems(values)
        self.extEnumToggler.setChecked(value not in data.get("values", []))
        if self.extEnumToggler.isChecked():
            self.extEnumValue.setText(value)
            self.extEnumComboxBox.setEnabled(False)
        else:
            self.extEnumComboxBox.setCurrentText(value)
            self.extEnumValue.setText(data.get('ext-type', ''))
            self.extEnumValue.setEnabled(False)
        if extRange := data.get('ext-range', []):
            self.extEnumValue.setValidator(QIntValidator(extRange[0], extRange[1]))
            self.tip.setText(self.tip.text() + f"\n>>>>  [注释] 取值范围: {extRange[0]} ~ {extRange[1]}  <<<<")
