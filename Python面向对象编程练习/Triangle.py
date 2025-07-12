class Triangle(object):
    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_vaild(a, b, c):
        """检查abc数值是否满足三角形"""
        if  a + b > c and a + c > b and b + c > a:
            pass
        else:
            print("请输入正确的数值")

    @property
    def perimeter(self):
        """计算周长
        :prarm circumference: 三角形周长值
        """
        circumference = self.a + self.b + self.c
        return circumference
    
    @property
    def area(self):
        """计算面积
        :param area: 三角形面积值
        """
        p = 1/2 * self.perimeter
        tri_area = (p * (p - self.a) * (p - self.b) * (p - self.c))
        return tri_area
    
    def __str__(self):
        return f'({self.a}, {self.b}, {self.c})'
    
tri = Triangle(4, 5, 6)
print(f'周长: {tri.perimeter}')
print(f'面积: {tri.area}')
