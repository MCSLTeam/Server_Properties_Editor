from PyQt5.QtCore import pyqtSignal


class BaseSinglePropertiesWidget:
    valueChanged = pyqtSignal(tuple)

    def __init__(self):
        self.propertyNameText = None
        self.propertyTip = None

    def onValueChanged(self, value):
        self.valueChanged.emit((self.propertyNameText, value))

    def setData(self, name: str, value: str, data: dict):
        self.propertyNameText = name
        self.propertyTip = data.get("tip", "")
