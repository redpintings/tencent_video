import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from tencent_weishi_dowload.config import BTN
from tencent_weishi_dowload.config import KEY
import time
from os import system
from random import randint
from tencent_weishi_dowload.PhoneControl import OperateAllPhone


class WeixinOperate():
    """
    实现对所有在线手机进行操作
    """
    busy = 0

    def __init__(self, phone_list):
        self.oap = OperateAllPhone(phone_list)
       
    def home(self):
        """
        :return:通过多次点击BACK按键回到主界面 之所以不直接点击HOME按键 是需要层层返回到主界面
        """
        for i in range(5):
            self.oap.key(KEY['BACK_KEYEVENT'])
            time.sleep(0.3)
        return KEY['BACK_KEYEVENT']

    def home_to_gzh_search(self):
        """
        :return:点击微视频图标
        """
        # 点击微信图标
        self.oap.tap(BTN['EMU_WEIXIN_ICON'])
        time.sleep(1)
        self.oap.tap(BTN['SEARCH'])
        time.sleep(1)
        self.oap.tap(BTN['Focus'])
        time.sleep(1)
        self.oap.tap(BTN['he'])
        time.sleep(2)
        return 0

    def click_det(self, bar):
        """
        点击详情页
        :return:
        """
        self.oap.tap(bar)
        time.sleep(1)

    def share_copy(self):
        """
        share and copy but
        :return:
        """
        self.oap.tap(BTN['share'])
        time.sleep(0.3)
        # 左拉滑动
        self.oap.swap([910, 1748], [351, 1734])
        self.oap.tap(BTN['copy2'])
        time.sleep(0.5)
        # adb shell am broadcast -a clipper.get
        command = r'adb shell am broadcast -a clipper.get >> data.txt'
        system(command)

    def click_choose_one(self, bar):
        self.oap.tap(bar)
        time.sleep(1)
        self.share_copy()
        self.oap.key(KEY['BACK_KEYEVENT'])
        time.sleep(0.3)

    def search_gzh(self):
        """
        上滑刷新
        :return:
        """
        # 输入拼音
        print('准备上拉')
        for i in range(50):
            self.oap.swap([761, 1390], [806, 999])
            time.sleep(0.5)
            self.click_det(BTN['detail'])
            time.sleep(1)
            self.oap.key(KEY['BACK_KEYEVENT'])
            time.sleep(0.3)

        return 0

    def ones_time(self):
        """
        进行上滑
        :return:
        """
        command = r'adb shell am startservice ca.zgrs.clipper/.ClipboardService'
        system(command)
        print('准备上拉')
        self.oap.swap([761, 1390], [806, 999])
        time.sleep(0.5)
        self.oap.swap([761, 1390], [806, 999])
        time.sleep(0.5)
        self.click_det(BTN['bar1'])
        self.share_copy()
        for i in range(1800):
            if i == 300 or i == 600:
                command = r'adb -s 1f29b831 usb'
                system(command)
            self.oap.swap([761, 1390], [806, 999])
            self.share_copy()
            time.sleep(0.5)

    def screen_cap(self):
        """
        截图尝试
        :return:
        """
        command = r'adb pull /screen.png'
        system(command)


if __name__ == '__main__':
    w = WeixinOperate(['xxxxx'])
    # w.home()
    w.home_to_gzh_search()
    # w.search_gzh()
    w.ones_time()
    w.home()
