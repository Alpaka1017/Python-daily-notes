title: Python 学习日记 -- 对象和类
author: Xueyong Lu
date: 2022-03-24
css: ...\css\my_md_style.css

<div align = "center">
    <h1>
        Python 学习日记 - Day 05
    </h1>
</div>
<div align = "right">
    <h2>对象和类</h2>
</div>



📘<<[Day 04](.\Python_Day04_SerialPort.md) | [Day 06](.\Python_Day06_.md)]>> 

## 1. 面向对象

面向对象：按照真实世界的思维方式进行软件系统的构建。

<img src=".\.msc\pics\class_object_discription.png" style="zoom:65%;" />

### 1.1 定义类

```python
# class <类名>(<父类>)
# 		类体

class Car(object):
	pass

class Car:
    pass
```

* 如果在类的定义中**`<父类>`**缺省，那么将会继承一个**`object`**类。
* 在Python中，**`object`**类是所有类的**根类**，其他所有的类都直接或者间接继承`object`类

### 1.2 创建对象

* 实例化类的过程就是创建对象的过程

* 对象可以看做一群具有类的特征的元素的集合

  ```python
  class Car:
      pass
  
  # 创建对象
  car = Car()
  print(type(car))
  
  >> <class '__main__.Car'>
  ```

### 1.3 类的成员

 <img src=".\.msc\pics\member_class.png" style="text-align : center; zoom:56%;" />

#### 1.3.1 实例变量

* 实例变量是对象个体特有的属性或者数据。

* 通过类的构造函数**`__init__(self, var1, var2, ...)`**进行新对象的构造和初始化

  ```python
  new* # 定义新类，对象时，会自动生成一个new*的非注释类的关键字
  class People(object):
      def __init__(self, name, age):
          self.name = name  # 创建和初始化实例变量name
          self.age = age    # 创建和初始化实例变量age
          return
  
  if __name__ == "__main__":
      # 用类的方法来构造对象
      person = People('XiaoZhao', 24)
      print('{}巨能睡, 虽然才{}岁，但是跟{}岁似的。'.format(person.name, person.age, 3*person.age))
  ```

* **`person`** 是对象，通过类**`People():`**构造

* **`name`**和**`age`**都是对象**`person`**的实例化对象，通过**``object.memberVar``**的方式对其访问

#### 1.3.2 构造方法

* **`__init__`**方法时一个非常特殊的方法，也称**构造方法**

* 作用是创建和初始化实例变量

* **`__init__`**方法本身没有开辟新的内存空间

  ```python
  class People(object):
      def __init__(self, name, age, gender='妹妹'):
          self.name = name  # 创建和初始化实例变量name
          self.age = age  # 创建和初始化实例变量age
          self.gender = gender
          return
  
  
  if __name__ == "__main__":
      # 用类的方法来构造对象
      person_1 = People('XiaoZhao', 24)
      person_2 = People('XiaoLu', 25, '老哥')
      person_3 = People(name='Anyone', gender='爱啥啥', age='爱几岁几岁')
      print('{}巨能睡, 虽然才{}岁，是{}的好{}。'.format(person_1.name, person_1.age, person_2.name, person_1.gender))
      print('{}是她的大{}，他都{}岁了。'.format(person_2.name, person_2.gender, person_2.age))
      print('{}只是个凑数的例子，他{}，性别{}。'.format(person_3.name, person_3.age, person_3.gender))
      
  >> XiaoZhao巨能睡, 虽然才24岁，是XiaoLu的好妹妹。
  >> XiaoLu是她的大老哥，他都25岁了。
  >> Anyone只是个凑数的例子，他爱几岁几岁，性别爱啥啥。
  ```

  <i class="fa fa-exclamation-circle" aria-hidden="true"></i>**注意：**

  * 用类构造新对象时，对象的实例化参数为定义的参数，而与类中初始化的参数无关
  * 定义对象的参数与传入类的参数一一对应，而与顺序无关
  * 默认在类中指定的参数要放在最后**`gender='xxx'`**

#### 1.3.3 实例方法

* 实例方法与构造方法的变量一样，都是某个实例（对象）个体特有的方法

* 注意两种方法：

  * 实例方法中调用类中定义的变量**`self.var`**，这里实例方法的调用就不需要外部参数，可以是**`Func(self)`**
  * 实例方法也可以通过外部传入参数，此时函数定义为**`Func(self, var)`**

  ```python
  class People(object):
      # 构造方法
      def __init__(self, name, age, hobby, gender='妹妹'):
          '''
          '''
          self.hobby = hobby
          return
      # 实例方法
      def interest_Inst_var(self):  # 使用类的参数
          print('{}的爱好是{}。'.format(self.name, self.hobby))
  
      def interest_Passed_parm(self, hobby):  # 使用外部传入参数
          print('{}的爱好是{}。'.format(self.name, hobby))
  if __name__ == "__main__":
      person_1 = People(name='XiaoZhao', age=24, hobby='跳舞')
      person_2 = People(name='XiaoLu', age=25, gender='老哥', hobby=None)
      
      person_1.interest_Inst_var()  # 调用类中声明的变量self.xxx
      person_2.interest_Passed_parm('Guitar')  # 从外部传入参数
      
  >> XiaoZhao的爱好是跳舞。
  >> XiaoLu的爱好是Guitar。
  ```

#### 1.3.4 类变量

* 类变量属于类，而不属于某个对象

* 类中的方法（构造方法或者实例方法）要调用类变量时，要通过类变量的父级（类名）来调用

  ```python
  *new
  class Example(object):
      # Define class variable
      var_class = 1000
      
      # Define initializing method
      def __init__(self, var1, var2):
          self.var1 = var1
          self.var2 = var2
          return
      
      # Define Instantiating method
      def Instantiating_method(self, var3):
          return self.var1 + var3
      
  # Call the class variable using a instantiated method:
  if __name__ == '__main__':
      example_obj = Example(var1_real, var2_real)
      example_obj.Instantiating_method(Example.var_class)
      # var1 was defined and initialized in __init__ method
  ```

#### 1.3.5 类方法

* 与类变量一样，类方法也属于类，而不属于某个对象实例

* 声明类方法的方式为装饰器**`@`**，装饰器在后面学习中会继续讨论

* 类方法可以调用类变量（构造/实例方法不行），eg: **`cls.class_var`**

* 但是在**类方法**中无法调用其他的实例变量，eg: **`self.var1`**

  ````python
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
      def class_method_examp(cls, num):  # 类方法不能调用实例变量（self.var1）
          return cls.class_var + num
      
  cal_examp = Example_calculation(var1=1, var2=2)
  print(cal_examp.add_calculation(1))
  print(cal_examp.class_method_examp(1))
  
  >> 102
  >> 101
  ````

#### 1.3.6 私有变量和私有方法

* 私有变量和私有方法都是只有在类里面才能访问的变量和方法

* 在类的外面如**`main()`**函数访问一个类的私有变量或者方法，会抛出**`AttributeError`**

* 私有变量的<u>构造</u>**`__init__`**方法：**`self.__var = var`**

* 私有方法的构造：**`def __func(self):`**

  ```python
  *new
  class Examp_private(object):
      # Define class private varible
      __Class_var = 1000
      
      # Initializing variable
      def __init__(self, var1, var2)
      	self.__var1 = var1    # var1 is a class-private variable
          self.var2 = var2
          return
      
      # Define private instantiating method
      def __private_examp(self):  # private method: only callable inside the class "Examp_private"
          return (self.var2 + Examp_private.__Class_var) * self.__var1
      
      def desc(self):
          return self.__private_examp()
      
  examp = Examp_private(var1 = 1, var2 = 2)
  print(examp.__private_examp())
  print(examp.desc())
  ```

  * 上述调用中：`print(examp.__private_examp())`会抛出一个**`AttributeError`**的错误，因为**`__private_examp()`**为类内部的方法
  * **`print(examp.desc())`**方法能够正常输出，因为`desc()`方法为公共方法，同时`desc()`调用了一个类的内部方法

#### 1.3.7 使用属性

* 为了实现对象的封装，在一个类中==不应该==有公有的成员变量，这些成员变量应该被设计为私有的，然后通过公有的**set**和**get**方法访问。

  ```python
  *new
  class Example_get_set(object):
      # Construction initializing method
      def __init__(self, var1, var2):
          self.var1 = var1
          self.__var2 = var2
          return
      
      # Define `get` method
      def get_Private_var(self):
          return self.__var2
      
      # Defin `set` method
      def set_Private_var(self, var_extern):
          self.__var2 = var_extern
          
  # call the methods
  examp = Example_get_set(var1=1, var=2)
  print(examp.get_Private_var()) # Print the private variable inside the class
  examp.set_Private_var(new_var) # Set new variable to the private variable
  print(examp.get_Private_var()) # Print the private variable after modification
  ```

  * 能够在外部通过调用`get_var2`方法获取class `Example_get_set`的内部变量__var2
  * 通过调用`set_var2`方法从外部更改class `Example_get_set`的内部变量`__var2`

* 可以通过**属性**来替代`get`和`set`方法

  ```python
  *new
  class Example_property(object):
      # Initializing: var2 is the private variable
      def __init__(self, var1, var2):
          self.var1 = var1
          self.__var2 = var2
          return
      
      @property
      def var2(self):            # Substitute `get_Private_var()` method
          return self.__var2
      
      @var2.setter
      def var2(self, var2):      # Substitute `set_Private_var()` method
      	self.__var2 = var2
          
  # Call the methods
  examp = Example_property(var1=1, var2=2)
  print(examp.var2)              # Through a decorator with the same name of var2, enable the directl call
  examp.var2 = new_var
  print(examp.var2)			   # Through `@var2.setter` enable the direct modification of a private variable from outside
  ```

  * 装饰器**`@property`**下定义的方法名就是类里的私有变量名，这样即使在外部也能直接通过访问变量本身来调用变量
  * 装饰器**`var2.setter`**定义的方法名也为类里的私有变量名，但是**`.setter`**提供了能直接赋值的方法

### 1.4 类和对象的性质

