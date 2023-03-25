import math


class People(object):
    # 构造方法
    def __init__(self, name, age, hobby, gender='妹妹'):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age
        self.gender = gender
        self.hobby = hobby
        return

    # 实例方法
    def interest_Inst_var(self):
        print('{}的爱好是{}。'.format(self.name, self.hobby))

    def interest_Passed_parm(self, hobby):
        print('{}的爱好是{}。'.format(self.name, hobby))


class Example_calculation(object):
    # Define class variable
    class_var = 100

    # Initializing method
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        return

    # Define instantiating method
    def add_calculation(self, var):
        return self.var1 + Example_calculation.class_var + var

    # Define class method
    @classmethod
    def class_method_examp(cls, num):  # 类方法不能调用实例变量
        return cls.class_var + num


class Examp_private(object):
    # Define class private variable
    __Class_var = 1000

    # Initializing variable
    def __init__(self, var1, var2):
        self.__var1 = var1  # var1 is a class-private variable
        self.var2 = var2
        return

    # Define private instantiating method
    def __private_examp(self):  # private method: only callable inside the class "Examp_private"
        return (self.var2 + Examp_private.__Class_var) * self.__var1

    def desc(self):
        return self.__private_examp()


class Example_property(object):
    # Initializing: var2 is the private variable
    def __init__(self, var1, var2):
        self.var1 = var1
        self.__var2 = var2
        return

    @property
    def var2(self):  # Substitute `get_Private_var()` method
        return self.__var2

    @var2.setter
    def var2(self, var2):  # Substitute `set_Private_var()` method
        self.__var2 = var2


class Example_parent(object):
    # 初始化类变量
    def __init__(self, var1, var2):
        self.var1 = var1
        self._var2 = var2  # 为使子类能够调用，不能构造为私有变量，而是受保护的变量`_var`
        return

    @property
    def var2(self):
        return self._var2

    def log_parent_func(self, var):
        return math.log((self._var2 + self.var1), var)


class Example_child(Example_parent):
    # 子类中定义有三个变量，其中var1, _var2是通过父类super()函数传入的，所以还需再构造一个var3
    def __init__(self, var3, **kwargs):
        # var2为父类中的受保护变量，在这里直接通过变量名var2调用即可，不用_var2
        super().__init__(**kwargs)
        self.var3 = var3

    def exp_child_func(self, var4):
        # 在子类的实例方法中，由于var2是由父类传递的，所以要声明“受保护变量”
        return ((self.var1 + self._var2) / self.var3) * math.exp(var4)


class Example_Parent_override:
    def say_hello(self):
        print("Hello from Parent")


class Example_Child_override(Example_Parent_override):
    def say_hello(self):
        super().say_hello()   # 调用父类的方法
        print("Hello from Child")


if __name__ == "__main__":
    # class 1: People()
    # 用类的方法来构造对象
    # person_1 = People(name='XiaoZhao', age=24, hobby='跳舞')
    # person_2 = People(name='XiaoLu', age=25, gender='老哥', hobby=None)
    # person_3 = People(name='Anyone', age='爱几岁几岁', gender='爱啥啥', hobby=None)
    # print('{}巨能睡, 虽然才{}岁，是{}的好{}。'.format(person_1.name, person_1.age, person_2.name, person_1.gender))
    # print('{}是她的大{}，他都{}岁了。'.format(person_2.name, person_2.gender, person_2.age))
    # print('{}只是个凑数的例子，他{}，性别{}。'.format(person_3.name, person_3.age, person_3.gender))
    #
    # person_1.interest_Inst_var()  # 调用类中声明的变量self.xxx
    # person_2.interest_Passed_parm('Guitar')  # 从外部传入参数

    # class 2: Example_calculation
    # cal_examp = Example_calculation(var1=1, var2=2)
    # print(cal_examp.add_calculation(1))
    # print(cal_examp.class_method_examp(1))
    #
    # examp = Examp_private(var1=1, var2=2)
    # # print(examp.__private_examp())  # 会抛出一个AttributeError的错误，因为调用了一个类内部方法__private_examp()
    # print(examp.desc())

    # class 4: Example_property
    # Call the methods
    # examp = Example_property(var1=1, var2=2)
    # print(examp.var2)  # Through a decorator with the same name of var2, enable the direct call
    # examp.var2 = 3
    # print(examp.var2)  # Through `@var2.setter` enable the direct modification of a private variable from outside

    # class 5: Inheritance
    # parent = Example_parent(var1=55, var2=45)
    # log_parent_base = 10
    # print('父类中传入的参数为:{}和{}, 父类中对数运算的底为:{}, 对数计算的结果为:\n{}'.format(parent.var1, parent.var2, log_parent_base, parent.log_parent_func(log_parent_base)))
    # child = Example_child(var1=parent.var1, var2=parent.var1, var3=100)
    # exp_child_exponent = 2
    # print(f'子类中传入的参数为:{child.var3}, 子类的运算函数传入指数为:{exp_child_exponent}, 并且继承了父类中的两个参数{parent.var1}和{parent.var2}, 指数计算的结果是:\n{child.exp_child_func(exp_child_exponent)}')
    # print(child.log_parent_func(6))
    # print(parent.log_parent_func(6))

    # class 6: Overriding the method
    greeting = Example_Child_override()  # 子类声明
    greeting.say_hello()
