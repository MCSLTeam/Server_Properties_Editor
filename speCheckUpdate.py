from PyQt5.QtCore import QThread, pyqtSignal

from MCSL2Lib.ProgramControllers.networkController import Session
from .speVariables import SPEVariables


class CheckUpdateThread(QThread):
    """
    检查更新的网络连接线程\n
    使用多线程防止假死
    """

    isUpdate = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("CheckUpdateThread")

    def run(self):
        try:
            latestVerInfo = Session.get(
                f"http://api.2018k.cn/checkVersion?id=A37A88233EB145A594E89DFA888984CC&version={SPEVariables.speVersion}"
            ).text.split("|")
            self.isUpdate.emit(latestVerInfo)
        except Exception as e:
            self.isUpdate.emit(["Failed"])


class FetchUpdateIntroThread(QThread):
    """
    获取更新介绍的网络连接线程\n
    使用多线程防止假死
    """

    content = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("FetchUpdateIntroThread")

    def run(self):
        try:
            intro = f"""{Session.get("http://api.2018k.cn/getExample?id=A37A88233EB145A594E89DFA888984CC&data=remark").text}"""
            self.content.emit(intro)
        except Exception as e:
            self.content.emit(["奇怪，怎么获取信息失败了？\n检查一下网络，或者反馈给开发者？"])
