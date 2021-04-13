from ..Base import Base
from ..info import Info
from ..ipa import register
import time

TITLE = '代码未混淆风险检测'
LEVEL = 1
INFO = '检测iOS App程序的源代码是否已经经过混淆处理'
blackList = ['Login', 'Helper', 'Manager']


class ObscureCheck(Base):
    def scan(self):
        results = []
        # 不知道为什么，只要不sleep就读不到文件，哪怕文件存在
        time.sleep(0.5)
        with open(self.appPath+'/ClassDump', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                for s in blackList:
                    if s in line and line not in results:
                        results.append(line)
        Info(key=self.__class__, title=TITLE, level=LEVEL, info=INFO, result="\n".join(results)).description()


register(ObscureCheck)