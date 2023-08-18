from PyQt5.QtCore import Qt
from Adapters.Plugin import Plugin
from MCSL2Lib.windowInterface import Window
from .speInterface import SPEMainUI
from qfluentwidgets import InfoBar, InfoBarPosition, FluentIcon as FIF

Server_Properties_Editor = Plugin()
speMainUI = SPEMainUI()

def load():
    pass


def enable():
    try:
        Window().addSubInterface(speMainUI, FIF.DEVELOPER_TOOLS, "SPE")
        InfoBar.success(
            title="提示",
            content="Server_Properties_Editor已启用。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
    except Exception as e:
        InfoBar.error(
            title="提示",
            content=f"Server_Properties_Editor启用失败！\n{e}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )


def disable():
    try:
        Window().navigationBar.removeWidget(routeKey=speMainUI.objectName())
        speMainUI.setParent(None)
        InfoBar.success(
            title="提示",
            content="Server_Properties_Editor已禁用。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
    except Exception as e:
        InfoBar.error(
            title="提示",
            content=f"Server_Properties_Editor禁用失败！\n{e}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )


# 注册加载代码
Server_Properties_Editor.register_loadFunc(load)

# 注册应用代码
Server_Properties_Editor.register_enableFunc(enable)

# 注册应用代码
Server_Properties_Editor.register_disableFunc(disable)
