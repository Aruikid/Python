class Point:
    """平面上的点"""

    def __init__(self, x = 0, y = 0):
        """初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """计算到另一个点的距离
        :param other: 另一个点
        """
        try:
            delta_x = self.x - other.x
            delta_y = self.y - other.y
        except TypeError:
            print('输入的不是数字噢！！！')
        
        return (delta_x * delta_x + delta_y * delta_y) ** 0.5
    
    def __str__(self):
        """字符串方法
        将Point中的数字用字符串的形式表达
        """
        return f'({self.x}, {self.y})'

p1 = Point(0, 6)
p2 = Point(4, 9)
print(p1)   
print(p2)
print(p1.distance_to(p2))
