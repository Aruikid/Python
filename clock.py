import time

class Clock:
    def __init__(self, hour = 0, minute = 0, second = 0):
        """初始化方法"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def time(self):
        """时间计时"""
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 59:
                self.hour += 1
                self.minute = 0
                self.second = 0
                if self.hour > 24:
                    print("今天就到此为止啦！明天见啦！")
                    self.hour = 0
                    self.minute = 0
                    self.second = 0
            
    def show(self):
        """显示时间"""
        return print(f'北京时间：{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}')
    
clock = Clock(0, 0, 0)
while True:
    """代码运行"""
    clock.time()
    clock.show()
    time.sleep(1)
