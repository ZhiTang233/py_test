"""
方法级别
在每个测试方法(测试代码)执行前后都会自动调用的结构

    # 在方法执行之前
    def setup(self):
        每个测试方法执行之前都会执行
        pass

    # 方法执行之后
    def teardown(self):
        每个测试方法执行之后都会执行
        pass

类级别
在每个测试类中所以方法执行前后 都会自动调用的结构
# 类级别Fixture的方法 是一个 类方法
# 类中所以方法之前
    @classmethod
    def setupClass(cls):
        pass

    # 类中所以方法之后
    @classmethod
    def teardownClass(cls):
        pass

模块级别(了解)
模块：代码文件
在每个代码文件执行前后执行的代码结构
模块级别需要写在类的外边直接定义函数
# 代码文件之前
    def setupModule():
        pass
    # 在代码文件之后
    def teardownModule():
        pass


方法级别和类级别的方法 不需要同时出现 自行选择

"""


