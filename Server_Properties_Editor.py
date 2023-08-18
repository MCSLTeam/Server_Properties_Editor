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
        Window().addSubInterface(speMainUI, FIF.APPLICATION, "示例")
        InfoBar.success(
            title="插件加载提示",
            content="Server_Properties_Editor启用成功！",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
    except Exception as e:
        InfoBar.error(
            title="插件加载提示",
            content=f"Server_Properties_Editor启用失败！\n{e}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )


def disable():
    # Window().
    pass


# 注册加载代码
Server_Properties_Editor.register_loadFunc(load)

# 注册应用代码
Server_Properties_Editor.register_enableFunc(enable)

# 注册应用代码
Server_Properties_Editor.register_disableFunc(disable)
