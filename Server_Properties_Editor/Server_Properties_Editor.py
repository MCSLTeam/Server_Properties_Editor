#     Copyright 2023, LxHTT, mailto:lxhtz.dl@qq.com
#
#     Part of "MCSL2", a simple and multifunctional Minecraft server launcher.
#
#     Licensed under the GNU General Public License, Version 3.0, with our
#     additional agreements. (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        https://github.com/MCSLTeam/MCSL2/raw/master/LICENSE
#
################################################################################

from PyQt5.QtCore import Qt
from Adapters.Plugin import Plugin
from MCSL2Lib.windowInterface import Window
from qfluentwidgets import InfoBar, InfoBarPosition

Server_Properties_Editor = Plugin()


def load():
    pass


def enable():
    InfoBar.success(
        title="插件加载提示",
        content="Server_Properties_Editor启用成功！",
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.BOTTOM_LEFT,
        duration=2500,
        parent=Window().pluginsInterface,
    )


def disable():
    Window


# 注册加载代码
Server_Properties_Editor.register_loadFunc(load)

# 注册应用代码
Server_Properties_Editor.register_enableFunc(enable)

# 注册应用代码
Server_Properties_Editor.register_disableFunc(disable)
