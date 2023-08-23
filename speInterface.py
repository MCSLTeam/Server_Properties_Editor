from PyQt5.QtCore import Qt, QRect, QSize, pyqtSlot
from MCSL2Lib.publicFunctions import openWebUrl
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
    PushButton,
    FluentIcon as FIF,
    InfoBarPosition,
    InfoBar,
    MessageBox,
)
from MCSL2Lib.variables import GlobalMCSL2Variables
from .speCheckUpdate import CheckUpdateThread, FetchUpdateIntroThread
from .speVariables import SPEVariables
from .singlePropertiesWidget import PropertiesWidget


@Singleton
class SPEMainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("SPEMainUI")

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
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
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.propertyNameSTitle = SubtitleLabel(self.subtitleWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.propertyNameSTitle.sizePolicy().hasHeightForWidth()
        )
        self.propertyNameSTitle.setSizePolicy(sizePolicy)
        self.propertyNameSTitle.setMinimumSize(QSize(185, 0))
        self.propertyNameSTitle.setMaximumSize(QSize(185, 16777215))
        self.propertyNameSTitle.setObjectName("propertyNameSTitle")
        self.horizontalLayout.addWidget(self.propertyNameSTitle)
        self.propertyValueSTitle = SubtitleLabel(self.subtitleWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.propertyValueSTitle.sizePolicy().hasHeightForWidth()
        )
        self.propertyValueSTitle.setSizePolicy(sizePolicy)
        self.propertyValueSTitle.setMinimumSize(QSize(185, 0))
        self.propertyValueSTitle.setMaximumSize(QSize(185, 16777215))
        self.propertyValueSTitle.setObjectName("propertyValueSTitle")
        self.horizontalLayout.addWidget(self.propertyValueSTitle)
        self.tipSTitle = SubtitleLabel(self.subtitleWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tipSTitle.sizePolicy().hasHeightForWidth())
        self.tipSTitle.setSizePolicy(sizePolicy)
        self.tipSTitle.setObjectName("tipSTitle")
        self.horizontalLayout.addWidget(self.tipSTitle)
        self.gridLayout.addWidget(self.subtitleWidget, 5, 1, 1, 5)
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
        self.gridLayout.addWidget(self.updateWidget, 1, 4, 1, 2)
        spacerItem2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.saveBtn = PrimaryPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout.addWidget(self.saveBtn, 4, 5, 1, 1)
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
        spacerItem3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.refreshBtn = PushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshBtn.sizePolicy().hasHeightForWidth())
        self.refreshBtn.setSizePolicy(sizePolicy)
        self.refreshBtn.setObjectName("refreshBtn")
        self.gridLayout.addWidget(self.refreshBtn, 4, 4, 1, 1)
        self.selectServerComboBox = ComboBox(self)
        self.selectServerComboBox.setObjectName("selectServerComboBox")
        self.gridLayout.addWidget(self.selectServerComboBox, 4, 2, 1, 2)
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
        self.gridLayout.addWidget(self.titleLimitWidget, 1, 1, 1, 3)

        self.StrongBodyLabel.setText("选择服务器：")
        self.saveBtn.setText("保存")
        self.titleLabel.setText("服务器server.properties编辑器")
        self.propertyNameSTitle.setText("配置项")
        self.propertyValueSTitle.setText("值")
        self.tipSTitle.setText("注释")
        self.currentVersionTitle.setText("当前版本：")
        self.refreshBtn.setText("刷新")
        self.currentVersionValue.setText(SPEVariables.speVersion)
        self.propertiesSmoothScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
        self.selectServerComboBox.setMaxVisibleItems(6)
        self.saveBtn.setEnabled(False)
        self.checkUpdateBtn.clicked.connect(self.checkUpdate)

    def setServerListComboBox(self):
        self.selectServerComboBox.clear()
        self.selectServerComboBox.addItems(SPEVariables.serverList)

    def clearPropertiesWidget(self):
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().deleteLater()

    def addPropertiesWidget(self, name: str, value: str, valueType: str, tip: str):
        propertiesWidget = PropertiesWidget()
        propertiesWidget.propertyName.setText(name)
        propertiesWidget.propertyValue.setPlaceholderText(valueType)
        propertiesWidget.propertyValue.setText(value)
        propertiesWidget.propertyValue.setObjectName(name)
        propertiesWidget.propertyValue.textChanged.connect(self.changeProperties)
        propertiesWidget.tip.setText(tip)
        self.setObjectName(f"{name}Widget")
        SPEVariables.propertiesLineEditDict.update(
            {
                propertiesWidget.propertyValue.objectName(): propertiesWidget.propertyValue
            }
        )
        self.verticalLayout.addWidget(propertiesWidget)

    def addTypedPropertiesWidget(self, name: str, value: str, widgetData: dict):
        propertiesWidget = PropertiesWidget()
        propertiesWidget.propertyName.setText(name)
        # propertiesWidget.propertyValue.setPlaceholderText(widgetData.get("type", ""))
        # propertiesWidget.propertyValue.setText(value)
        # propertiesWidget.propertyValue.setObjectName(name)
        # propertiesWidget.propertyValue.textChanged.connect(self.changeProperties)
        propertiesWidget.tip.setText(widgetData.get("tip", ""))
        pass

    def changeProperties(self):
        SPEVariables.unSavedServerProperties.update(
            {self.sender().objectName(): self.sender().text()}
        )
        if SPEVariables.unSavedServerProperties != SPEVariables.fileServerProperties:
            self.saveBtn.setEnabled(True)
        else:
            self.saveBtn.setEnabled(False)

    def checkUpdate(self):
        """
        检查更新触发器\n
        返回：\n
        1.是否需要更新\n
            1为需要\n
            0为不需要\n
            -1出错\n
        2.新版更新链接\n
        3.新版更新介绍\n
        """
        self.checkUpdateBtn.setEnabled(False)  # 防止爆炸
        InfoBar.info(
            title="开始为SPE检查更新...",
            content="",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_LEFT,
            duration=3000,
            parent=self,
        )
        self.thread_checkUpdate = CheckUpdateThread(self)
        self.thread_checkUpdate.isUpdate.connect(self.showUpdateMsg)
        self.thread_checkUpdate.start()

    @pyqtSlot(list)
    def showUpdateMsg(self, latestVerInfo):
        """如果需要更新，显示弹窗；不需要则弹出提示"""
        if latestVerInfo[0] == "true":  # 需要更新
            title = f"有新版本：{latestVerInfo[4]}"
            w = MessageBox(title, "更新介绍加载中...", parent=self)
            w.contentLabel.setTextFormat(Qt.MarkdownText)
            w.yesButton.setText("更新")
            w.cancelButton.setText("关闭")
            self.thread_fetchUpdateIntro = FetchUpdateIntroThread(self)
            self.thread_fetchUpdateIntro.content.connect(w.contentLabel.setText)
            self.thread_fetchUpdateIntro.start()
            w.yesSignal.connect(
                lambda: openWebUrl(Url="https://github.com/MCSLTeam/Server_Properties_Editor/releases")
            )
            w.exec()

        elif latestVerInfo[0] == "false":  # 已是最新版
            InfoBar.success(
                title="无需更新",
                content="SPE插件已是最新版本",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_LEFT,
                duration=2500,
                parent=self,
            )
        else:
            InfoBar.error(
                title="SPE检查更新失败",
                content="尝试自己检查一下网络？",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_LEFT,
                duration=2500,
                parent=self,
            )

        self.checkUpdateBtn.setEnabled(True)
