from json import loads

from PyQt5.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition, FluentIcon as FIF, MessageBox

from Adapters.Plugin import Plugin
from MCSL2Lib.publicFunctions import readGlobalServerConfig
from MCSL2Lib.windowInterface import Window
from .speInterface import SPEMainUI
from .speVariables import SPEVariables

Server_Properties_Editor = Plugin()
speMainUI = SPEMainUI()


def load():
    pass


def enable():
    try:
        Window().addSubInterface(speMainUI, FIF.DEVELOPER_TOOLS, "SPE")
        refreshServerList()
        speMainUI.refreshBtn.clicked.connect(refreshServerList)
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


def refreshServerList():
    globalServerConfig = readGlobalServerConfig()
    SPEVariables.serverList.clear()
    for i in globalServerConfig:
        SPEVariables.serverList.append(i["name"])
    SPEVariables.serverList.append("选择一个服务器")
    initSPEComboBox()


def changeWhichServer(serverName):
    if serverName == "选择一个服务器":
        speMainUI.saveBtn.setEnabled(False)
        try:
            speMainUI.saveBtn.clicked.disconnect()
        except Exception:
            pass
        return
    elif SPEVariables.unSavedServerProperties != SPEVariables.fileServerProperties:
        w = MessageBox("警告", "设置未保存！是否要切换到其他服务器的配置文件？", speMainUI)
        w.cancelButton.setText("确定")
        w.yesButton.setText("取消")
        w.cancelSignal.connect(lambda: readServerProperties(serverName))
        w.exec()
    else:
        readServerProperties(serverName)


def readServerProperties(serverName):
    try:
        with open(
            f"./Servers/{serverName}/server.properties", "r", encoding="utf-8"
        ) as serverPropertiesFile:
            lines = serverPropertiesFile.readlines()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    SPEVariables.fileServerProperties[key.strip()] = value.strip()
                    SPEVariables.unSavedServerProperties = (
                        SPEVariables.fileServerProperties.copy()
                    )
        initSPEWidgets()
    except FileNotFoundError:
        InfoBar.error(
            title="提示",
            content="此服务器没有此配置文件。\n尝试先开启一次服务器？",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=speMainUI,
        )
        speMainUI.clearPropertiesWidget()


def initSPEComboBox():
    if not SPEVariables.firstLoad:
        speMainUI.selectServerComboBox.currentIndexChanged.disconnect()
    tmpServerName = speMainUI.selectServerComboBox.text()
    speMainUI.setServerListComboBox()
    if SPEVariables.firstLoad:
        speMainUI.selectServerComboBox.setCurrentIndex(len(SPEVariables.serverList) - 1)
    else:
        try:
            speMainUI.selectServerComboBox.setCurrentIndex(
                SPEVariables.serverList.index(tmpServerName)
            )
        except Exception:
            speMainUI.selectServerComboBox.setCurrentIndex(
                len(SPEVariables.serverList) - 1
            )
            speMainUI.clearPropertiesWidget()
    speMainUI.selectServerComboBox.currentIndexChanged.connect(
        lambda: changeWhichServer(
            SPEVariables.serverList[speMainUI.selectServerComboBox.currentIndex()]
        )
    )
    SPEVariables.firstLoad = False


def loadPropertiesTip():
    with open(
        "./Plugins/Server_Properties_Editor/properties.json", "r", encoding="utf-8"
    ) as propertiesTipFile:
        SPEVariables.tips = loads(propertiesTipFile.read())


def initSPEWidgets():
    try:
        speMainUI.saveBtn.clicked.disconnect()
    except Exception:
        pass
    speMainUI.clearPropertiesWidget()
    loadPropertiesTip()
    for item in SPEVariables.fileServerProperties:
        if item in SPEVariables.tips:
            speMainUI.addPropertiesWidget(
                name=item,
                value=SPEVariables.fileServerProperties[item],
                valueType=SPEVariables.tips[item][0],
                tip=SPEVariables.tips[item][1],
            )
        else:
            speMainUI.addPropertiesWidget(
                name=item,
                value=SPEVariables.fileServerProperties[item],
                valueType="",
                tip="",
            )
    speMainUI.saveBtn.clicked.connect(saveProperties)


def saveProperties():
    try:
        SPEVariables.fileServerProperties = SPEVariables.unSavedServerProperties.copy()
        with open(
            f"./Servers/{SPEVariables.serverList[speMainUI.selectServerComboBox.currentIndex()]}/server.properties",
            "w+",
            encoding="utf-8",
        ) as saveProperties:
            content = "#Minecraft server properties\n#Edited by Server Properties Editor made by LxHTT\n"
            for property in SPEVariables.fileServerProperties:
                fileProperty = (
                    f"{property}={SPEVariables.fileServerProperties[property]}\n"
                )
                content += fileProperty
            saveProperties.write(content)
        InfoBar.success(
            title="提示",
            content="保存成功！",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=speMainUI,
        )
        speMainUI.saveBtn.setEnabled(False)
    except Exception as e:
        InfoBar.error(
            title="提示",
            content=f"保存失败！\n{e}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=speMainUI,
        )


Server_Properties_Editor.register_loadFunc(load)
Server_Properties_Editor.register_enableFunc(enable)
Server_Properties_Editor.register_disableFunc(disable)
