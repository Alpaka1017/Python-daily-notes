<sub>Title: Python 学习日记 - QT项目中的一些问题与总结<br>Author:<a href="https://github.com/Alpaka1017?tab=repositories" target="_blank">Xueyong Lu  <i class="fa fa-github" aria-hidden="true"></i></a></br><small>First Edition: March - 2023</small></sub>

<div align = "center">
    <h1>
        Python 学习日记 - Part 09
    </h1>
</div>
<div align = "right">
    <h2>QT项目中的一些问题与总结 - 01</h2>
</div>



📘<<[Part 08](./Python_Part_08-MagicFunc.md) | [Part 10](./Python_Part_10-QT_02.md)]>> 

# UI设计及杂项

## UI设计

* 使用***QT Designer***创建UI文件

* 利用以下命令行工具将`*.ui`文件转换成`*.py`文件

  ```bash
  python -m PyQt6.uic.pyuic xxx.ui -o xxx.py
  ```

* 或者直接使用：***QT Designer → Form → View code*** 菜单选项将`*.ui`代码转成`*.py`代码
* 在主程序`main.py`中通过`import`的方式将UI代码导入到自己的项目中

* &#x2139;注意：
  * 在利用***QT Designer***进行布局的时候，明白每一个组件对于其父组件的继承关系
  * 比如：对于想设置一个窗口的缩放大小时，要在空白的`MainWindow`对象上首先放置一个`GridLayout`组件，表明当前的网格布局对于整个窗口（父级组件）继承关系，然后再向其中以同样的方法放置`Widgets`
  * 然后利用`hspacer`、`vspacer`等限制在缩放窗口时某些期望组件的相对位置

## 资源文件注册

* 在考虑到之后要将应用程序打包，原先在程序中通过引用项目的<u>相对</u>或者<u>绝对路径</u>可能会造成一定的找不到引用问题。要避免这一问题，就要将原先的资源文件作为一个部分打包进`*.exe`文件

* 另一个解决方案就是通过***QT Designer***生成资源文件***`*.qrc`***，然后通过==命令行工具==将其转换为`*.py`文件，在需要调用该资源的程序中通过`import`导入

  ```bash
  pyrcc5 xxx.qrc -o xxx.py
  ```

  * 在创建***`*.qrc`***文件时，允许用户添加前缀，类似于路径的定义，然后在引用的时候按照`":suffix/example.png"`的方式进行引用
  * 资源文件***`*.qrc`***允许添加的资源类型：
    1. 图像类：`*.png`，`*.jpg`, `*.jepg`, `*.bmp`, `*.tiff`, `*.gif`, `*.ico`, `*.svg`等
    2. 字体类：`*.ttf`
    3. QT样式表: `*.qss`等

# UI初始化

## ***`QMainWindow`***

* 主窗体`QMainWindow`继承自`PyQt6.QtWidgets`

  * 在程序中导入主窗体的UI文件

    ```python
    from RemoteControl_main_UI import Ui_MainWindow
    ```

  * 通过一个继承自`QMainWindow`的类对其进行初始化

    ```python
    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            
            self.ui_main = Ui_MainWindow()
            self.ui_main.setupUi(self)
    ```

    * &#x2139; `super(MainWindow, self).__init__()`表示调用`MainWindow`类的父类`QtWidgets.QMainWindow`的构造方法。通过执行父类的`__init__()`函数实现了对主窗口对象`MainWindow`的初始化

  * 在主程序入口处对其进行实例化并在***主窗体的事件循环 .exec()***中运行

    ```python
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        # 设置窗口标题
        window.setWindowTitle('xxx')
        # 设置窗口Icon
        icon = QtGui.QPixmap('xxx')
        icon_h_32 = icon.scaledToHeight(32, QtCore.Qt.TransformationMode.SmoothTransformation)
        window.setWindowIcon(QtGui.QIcon(icon_h_32))
    
        window.show()
        """创建系统托盘图标"""
        tray_icon = functions.MySysTrayWidget(ui=window.ui_main, app=app, window=window)
    
        sys.exit(app.exec())
    ```

## ***`QDialog`***

* `QDialog`对话框窗体继承自`QtWidgets.QDialog`，是一种可通过某种动作/事件调用打开的子窗体对象

* 与主窗体创建类似的方法：设计布局并生成`*.ui`文件 → 转换为`*.py`文件 → 在主程序中导入

  ```python
  from StepGuide_child_UI import Ui_Dialog_StepDetails
  ```

  * 实例化方法：

    ```python
    class StepGuideChildWindow(QtWidgets.QDialog, Ui_Dialog_StepDetails):
        def __init__(self, parent=None):
            super(StepGuideChildWindow, self).__init__(parent)
            self.parent = parent
            self.setupUi(self)
            # 设置子窗口的模态：当其打开时，其他窗口为不可选中状态
            self.setModal(True)
    
            # 初始化窗口组件
            ...
    ```

  * 要通过主窗体中的某些组件的事件来打开这个子窗口（对话框），那么就要先在***主窗体类中对子窗口进行实例化（构造）:***

    ```python
    # self表示这里的ui_child_step_guide子窗口对象继承自主窗体，self即为MainWindow
    self.ui_child_step_guide = StepGuideChildWindow(self)
    ```

* 带有按钮组（**OK**和**Cancel**）的`QDialog`

  ```python
  # buttonBox为QDialog对象上按钮的父级控件
  self.buttonBox.accepted.connect(self.handle_operation_accepted)
  
  def handle_operation_accepted(self):
      ...
  ```

## **`QtGui.QApplication`**

* Qt中的应用程序类，==非窗体对象==
* 用于<u>管理应用程序的生命周期</u>和<u>事件循环</u>。它是基于QtWidgets模块的应用程序使用的主要类
* 使用`QApplication`类创建应用程序对象，并启动应用程序的事件循环



## **`QtCore.QApplication`**

* Qt中的应用程序类的另一个变体，==非窗体对象==
* 用于基于Qt核心模块的应用程序
* 适用于<u>没有图形界面</u>或使用<u>其他图形界面库（如Qt Quick）</u>的应用程序



## **`QtWidgets.QApplication`**

* 是`QtGui.QApplication`的子类，==非窗体对象==
* 专门用于基于Qt Widgets模块的应用程序
* 提供了一些特定于窗口部件的功能，并与Qt Widgets模块的其他类密切集成



## `QObject`

* `QObject` 是 Qt 框架中所有对象的基类，它提供了一些基本的功能，如信号和槽机制、对象树结构、属性管理等

* `QObject` 是一个非常通用的类，可以被用作其他 Qt 类的基类

* `QObject` 本身不支持开启事件循环，但是可以通过在`QObject`实例对象之上创建一个**任意**的`QApplication`对象，即可开启事件循环

  ```python
  from PyQt6.QtCore import QTimer, QObject
  
  class MyObject(QObject):
      def __init__(self):
          super().__init__()
          
          self.timer = QTimer()
          self.timer.timeout.connect(self.handle_timeout)
          self.timer.start(1000)  # 每隔1秒触发一次定时器事件
  
      def handle_timeout(self):
          print("Timer timeout!")
  
  # 创建 QApplication 对象并启动事件循环
  app = QApplication([])
  obj = MyObject()
  app.exec()
  ```



# 部分UI组件的初始化及其使用

## `QLabel`

* `QLabel`的常用方法：
  * **`setText(str text)`**: 设置标签的文本内容
  * **`text() -> str`**: 获取标签的文本内容
  * **`setPixmap(QPixmap pixmap)`**: 设置标签显示的图像
  * `setAlignment(Qt.Alignment alignment)`: 设置标签文本的对齐方式
  * `setWordWrap(bool enable)`: 设置是否启用自动换行
  * **`setStyleSheet(str styleSheet)`**: 设置标签的样式表
  * **`setToolTip(str text)`**: 设置标签的工具提示文本
  * **`clear()`**: 清除标签的内容
  * `setScaledContents(bool enable)`: 设置是否自动缩放图像以适应标签的大小
  * `setSizePolicy(QSizePolicy policy)`: 设置标签的尺寸策略
  * `setFont(QFont font)`: 设置标签的字体
  * `setAccessibleName(str name)`: 设置标签的可访问名称

## `QRadioButton`

* 设置`QRadioButton`的单选中模态
  ```python
      ...
      button_group = QtWidgets.QButtonGroup()
      button_group.buttonClicked.connect(self.handleButtonClicked)
  	
      # 局部变量，只在方法内部可见和可访问，只在方法执行期间存在，并且无法在类的其他方法中访问或引用
      button1 = QRadioButton("Button 1")
      button2 = QRadioButton("Button 2")
      button3 = QRadioButton("Button 3")
  
      button_group.addButton(button1, 1)
      button_group.addButton(button2, 2)
      button_group.addButton(button3, 3)
  
  def handleButtonClicked(self, button):
          # 根据选中按钮的ID执行相关操作
          selected_id = button.parent().checkedId()
          print("Selected ID:", selected_id)
  ```

## `QComboBox`

* `QComboBox`常用的方法：
  * `addItem()`：添加一个对象
  * `addItems()`：添加多个对象
* `QComboBox`常用的事件：
  * **`activated`**：选择了下拉列表中的一个项并关闭下拉列表时触发
  * `highlighted`：鼠标悬停在下拉列表中的一个项上时触发
  * `activated(int)`：选择一个选项并关闭，并返回索引
  * **`currentTextChanged`**：当前文本改变触发
  * **`currentIndexChanged`**：当前索引改变触发
  * `currentIndexChanged(int)`：类似上面，返回一个索引值

## `QLineEdit`

* `QLineEdit`的方法：
  * **`text()`**: 获取当前文本框中的文本内容
  * **`setText(text)`**: 设置文本框中的文本内容为`text`
  * **`clear()`**: 清空文本框中的内容
  * `setPlaceholderText(text)`: 设置文本框中的占位文本，当文本框为空时显示
  * `setReadOnly(enabled)`: 设置文本框是否为只读模式
  * `setMaxLength(length)`: 设置文本框的最大长度
  * `selectAll()`: 选中文本框中的全部文本
  * `setCursorPosition(position)`: 设置文本框中的光标位置
  * `setEchoMode(mode)`: 设置文本框的回显模式，例如密码模式
  * **`setValidator(validator)`**: 设置文本框的输入验证器，限制输入的格式
  * **`textChanged.connect(slot)`**: 连接一个槽函数，在文本内容发生变化时触发
  * `editingFinished.connect(slot)`: 连接一个槽函数，在文本编辑完成时触发（接收到`Carrige Return`或者文本框失焦时触发）

* **`QLineEdit`**组件的`setValidator()`方法：

  * 整型验证器`QtGui.QIntValidator()`

    ```python
    self.int_validator = QtGui.QIntValidator()
    self.int_validator.setBottom(0)
    self.int_validator.setTop(99)
    ...
    self.ui_main.lineEdit.setValidator(self.int_validator)
    ```

  * 浮点数验证器：`QtGui.QDoubleValidator()`

    ```python
    self.double_validator = QtGui.QDoubleValidator()
    self.double_validator.setBottom(0)
    self.double_validator.setDecimals(5)
    ...
    self.ui_main.lineEdit.setValidator(self.double_validator)
    ```

## `QPushButton`

* `QPushButton`的常用方法：
  - **`setText(text)`**: 设置按钮显示的文本
  - **`text()`**: 获取按钮当前显示的文本
  - **`setIcon(icon)`**: 设置按钮显示的图标
  - `icon()`: 获取按钮当前显示的图标
  - `setEnabled(enabled)`: 设置按钮是否可用
  - `isEnabled()`: 检查按钮是否可用
  - **`setChecked(checked)`**: 设置按钮是否被选中（用于`QPushButton`的子类`QRadioButton`和`QCheckBox`）
  - **`isChecked()`**: 检查按钮是否被选中（用于`QPushButton`的子类`QRadioButton`和`QCheckBox`）
  - **`setToolTip(toolTip)`**: 设置按钮的工具提示文本
  - `toolTip()`: 获取按钮的工具提示文本
  - ***`clicked`***: 一个信号，当按钮被点击时触发

## `QTextEdit`

* `QTextEdit`组件常用方法：
  * ***`append(text)`***：`text`文本将会被追加到`QTextEdit`的当前内容的末尾，并自动滚动到新追加的文本位置
  * `setText(text)`: 设置编辑框的文本内容
  * `toPlainText()`: 获取编辑框中的纯文本内容
  * **`setHtml(html)`**: 设置编辑框的HTML内容
  * `toHtml()`: 获取编辑框的HTML内容
  * **`setReadOnly(readOnly)`**: 设置编辑框是否只读
  * `isReadOnly()`: 检查编辑框是否为只读模式
  * `setPlaceholderText(text)`: 设置编辑框的占位文本
  * `placeholderText()`: 获取编辑框的占位文本
  * **`setStyleSheet(styleSheet)`**: 设置编辑框的样式表
  * `undo()`: 执行撤销操作
  * `redo()`: 执行重做操作
  * `cut()`: 执行剪切操作
  * `copy()`: 执行复制操作
  * `paste()`: 执行粘贴操作
  * `selectAll()`: 选中编辑框中的所有文本
  * `clear()`: 清空编辑框中的内容
  * `textChanged`: 一个信号，当编辑框中的文本内容发生变化时触发

## `QTextBrowser`

* 与`QTextEdit`和`QPlainTextEdit`的主要区别：

  |            |      QTextEdit       |              QTextBrowser              |                      QPlainTextEdit                       |
  | :--------: | :------------------: | :------------------------------------: | :-------------------------------------------------------: |
  |  显示模式  |    纯文本/ 富文本    | 主要显示富文本（支持`HTML`超文本显示） |                          纯文本                           |
  |  编辑模式  |        可编辑        |                  只读                  |                          可编辑                           |
  | 功能复杂性 |   支持高级编辑操作   |    不支持（表格、图片、字体样式等）    |                          不支持                           |
  | 外观/布局  | 简单的多行文本编辑框 | 类似浏览器的外观，带有滚动条和页面布局 |                      更加轻量和简单                       |
  |    备注    |          -           |                   -                    | 不支持`append`方法<br />而是用`insertPlainText(text)`方法 |

## `QListWidget`

* `QListWidget`组件是用于显示列表的Qt组件，它提供了以下方法：

  * **`addItem(QListWidgetItem item)`**: 向列表中添加一个项
  * **`addItems(List[str] items)`**: 向列表中添加多个项
  * **`item(row: int) -> QListWidgetItem`**: 获取指定行索引处的项
  * **`takeItem(row: int) -> QListWidgetItem`**: 移除并返回指定行索引处的项
  * **`currentItem() -> QListWidgetItem`**: 获取当前选中的项
  * **`currentRow() -> int`**: 获取当前选中项的行索引
  * **`selectedItems() -> List[QListWidgetItem]`**: 获取所有选中的项
  * `selectedIndexes() -> List[QModelIndex]`: 获取所有选中项的索引
  * `clear()`: 清空列表中的所有项
  * **`count() -> int`**: 获取列表中的项数
  * **`itemClicked.connect(slot)`**: 连接点击项的信号与槽函数
  * **`itemDoubleClicked.connect(slot)`**: 连接双击项的信号与槽函数
  * `itemSelectionChanged.connect(slot)`: 连接选中项变化的信号与槽函数

* 利用`addItem()`方法向`QListWidget`添加`icon + text`组合的item:
  ```python
  list_widget = QListWidget()
  
  item = QListWidgetItem("Item Text")
  icon = QIcon("path_to_icon.png")
  item.setIcon(icon)
  
  list_widget.addItem(item)
  ```

## `QSlider`

* `QSlider`对象的常用方法：
  * **`setMinimum(int minimum)`**: 设置滑动条的最小值
  * **`setMaximum(int maximum)`**: 设置滑动条的最大值
  * **`setValue(int value)`**: 设置滑动条的当前值
  * `setTickInterval(int interval)`: 设置刻度线的间隔
  * `setSingleStep(int step)`: 设置单步的大小，即按下箭头或点击滑动条的空白区域时滑动的值的增量
  * `setPageStep(int step)`: 设置页面步长，即按下滑块或点击滑动条背景时滑动的值的增量
  * **`value() -> int`**: 获取滑动条的当前值
  * `minimum() -> int`: 获取滑动条的最小值
  * `maximum() -> int`: 获取滑动条的最大值
  * **`sliderMoved[int value]`**: 滑动条的值发生变化时发出的信号，可以连接到槽函数进行处理
  * **`valueChanged[int value]`**: 滑动条的值发生变化时发出的信号，可以连接到槽函数进行处理

## `QProgressBar`

* `QProgressBar`的常用方法：
  * **`setMinimum(int minimum)`**: 设置进度条的最小值
  * **`setMaximum(int maximum)`**: 设置进度条的最大值
  * **`setValue(int value)`**: 设置进度条的当前值
  * `setTextVisible(bool visible)`: 设置是否显示进度条上的文本
  * `setFormat(str format)`: 设置进度条上显示的文本格式
  * **`reset()`**: 重置进度条，将当前值设置为最小值
  * **`value() -> int`**: 获取进度条的当前值
  * `minimum() -> int`: 获取进度条的最小值
  * `maximum() -> int`: 获取进度条的最大值



## `QAction`

* `QAction`对象继承自`QtGui`，为菜单栏对象的选中状态

* `QAction`对象的动作为`triggered`

* 设置单选的`QAction`状态：通过`QActionGroup`实现：

  ```python
  # self对象为MainWindow类
  self.actionGroup = QtGui.QActionGroup(self)
  self.actionGroup.addAction(self.ui_main.actionNo_line_feed) 	 # No line feed after end identifier
  self.actionGroup.addAction(self.ui_main.action_carrige_return)   # <cr>
  self.actionGroup.addAction(self.ui_main.action_line_feed) 		 # <lf>
  self.actionGroup.addAction(self.ui_main.action_CR_LF)  			 # <cr&lf>
  
  ...
  # 然后通过槽函数的调用以及 self.sender()对象来实现不同的动作
  self.ui_main.actionNo_line_feed.triggered.connect(
      lambda: self.read_send_thread.set_line_feed_style(self.ui_main, self.sender()))
  self.ui_main.action_carrige_return.triggered.connect(
      lambda: self.read_send_thread.set_line_feed_style(self.ui_main, self.sender()))
  self.ui_main.action_line_feed.triggered.connect(
      lambda: self.read_send_thread.set_line_feed_style(self.ui_main, self.sender()))
  self.ui_main.action_CR_LF.triggered.connect(
      lambda: self.read_send_thread.set_line_feed_style(self.ui_main, self.sender()))
  ```

  

📘<<[Part 08](./Python_Part_08-MagicFunc.md) | [Part 10](./Python_Part_10-QT_02.md)]>> 

