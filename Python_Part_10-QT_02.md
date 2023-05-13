<sub>Title: Python 学习日记 - QT项目中的一些问题与总结<br>Author:<a href="https://github.com/Alpaka1017?tab=repositories" target="_blank">Xueyong Lu  <i class="fa fa-github" aria-hidden="true"></i></a></br><small>First Edition: March - 2023</small></sub>

<div align = "center">
    <h1>
        Python 学习日记 - Part 10
    </h1>
</div>
<div align = "right">
    <h2>QT项目中的一些问题与总结 - 02</h2>
</div>




📘<<[Part 09](./Python_Part_09-QT_01.md) | [Part 11](./Python_Part_10-QT_02.md)]>> 

# 事件

## 常见事件

* PyQt中的组件事件主要是通过***信号 (Signal)***和***槽 (Slot)*** 机制来实现的，以下是一些常用的组件及其对应的触发事件

  | Widgets      | Action                                                       |
  | :----------- | :----------------------------------------------------------- |
  | QPushButton  | **clicked (一次性操作)**, pressed, released, **toggled (监控状态的变化)** |
  | QRadioButton | clicked, toggled                                             |
  | QCheckBox    | clicked, toggled                                             |
  | QComboBox    | activated, currentIndexChanged, currentTextChanged           |
  | QLineEdit    | editingFinished, returnPressed, textChanged                  |
  | QTextEdit    | textChanged, cursorPositionChanged                           |
  | QSlider      | valueChanged, sliderReleased                                 |
  | QSpinBox     | valueChanged                                                 |
  | QListView    | clicked, doubleClicked                                       |
  | QTreeWidget  | itemClicked, itemDoubleClicked                               |
  | QTableWidget | cellClicked, cellDoubleClicked                               |
  | QProgressBar | valueChanged, rangeChanged, textChanged                      |



## **`lambda`函数**

* 在连接槽函数时，`lambda`匿名函数允许用户临时传递一个变量

* `lambda`函数往往用在触发事件之后，需要在控件中做出修改的事件中

  * 不需要传递参数：

    ```python
    self.ui_main.catalog_display_button.clicked.connect(self.read_send_thread.ser_command_catalog)
    ```

  * 需要传递参数
    ```python
    # 在get_set_address函数中可以调用参数（Mainwindow的实例：self.ui_main）中的组件，并对其做出修改
    self.ui_main.address_button.clicked.connect(lambda: self.read_send_thread.get_set_address(self.ui_main))
    ```



# 自定义槽函数

## 使用步骤

1. 创建一个类，该类继承自需要使用槽函数的组件类（如 `QWidget`、`QMainWindow` 等）或者继承自 `QObject` 类

   ```python
   class CheckSerialThread(QtCore.QThread):
       # 新定义一个QtCore.pyqtSignal信号，该信号传递的数据类型为str
       CONNECTION_STATUS_CHANGED = QtCore.pyqtSignal(str)
       
       def __init__(self, ui, parent):
           super().__init__(parent)
           ...
   ```

2. 在该类中需要发送信号的地方通过`emit()`方法将要处理的信号发送

   ```python
           if ...:
               self.CONNECTION_STATUS_CHANGED.emit(f"Opening port {self.port_param_dict_func['port']}.")
               try:
                   ...
   ```

3. 在其他类中通过该类的实例访问这个信号对象，并对其进行处理

   ```python
   class MainWindow(QtWidgets.QMainWindow):
       def __init__(self):
           super(MainWindow, self).__init__()
           ...
       self.check_serial_thread.CONNECTION_STATUS_CHANGED.connect(
                   lambda status: functions.update_connection_status(self.ui_main, status))
       ...
   ```

4. 将这个信号发送的数据在函数`functions.update_connection_status`中进行处理

   ```python
   """functions.py"""
   @QtCore.pyqtSlot(str)
   def update_connection_status(ui, status: str):
       if any(keyword in status for keyword in ("Successfully", "successfully")):
           ui.status_label.setStyleSheet('QLabel {color:green; font: 57 9pt "Open Sans Medium";}')
           ...
   ```

## 注意事项

* 该信号的发射是机制是：只要`CheckSerialThread`类中的信号通过`emit()`有数据发送，那么就会激活它对应的槽函数

* 它的槽函数可以使用`@QtCore.pyqtSlot(str)`装饰器来进行装饰，以在连接信号和槽函数时进行编译时检查（可选）

* 自定义的信号可以通过变量组合的方式来一次发送不同类型的变量：
  ```python
  class MyObject(QObject):
      my_signal = pyqtSignal(str, dict, list)
  
      def __init__(self):
          super().__init__()
  
      def do_something(self):
          data_str = "Hello"
          data_dict = {"key": "value"}
          data_list = [1, 2, 3]
          self.my_signal.emit(data_str, data_dict, data_list)
          
  def my_slot(str_data, dict_data, list_data):
      print("Received data:")
      print("String:", str_data)
      print("Dictionary:", dict_data)
      print("List:", list_data)
  
  if __name__ == '__main__':
      obj = MyObject()
      obj.my_signal.connect(my_slot)
  
      obj.do_something()
  ```

## 连接方式 (`PyQt6`)

| 连接方式     | 命名空间 (QtCore.Qt.ConnectionType) | 说明                                                         |
| ------------ | ----------------------------------- | ------------------------------------------------------------ |
| 默认         | AutoConnection                      | 自动选择连接类型。如果信号和槽函数在同一线程，则使用 `QtCore.Qt.DirectConnection`，否则使用 `QtCore.Qt.QueuedConnection` |
| 直接连接     | DirectConnection                    | 直接连接，即信号发射时立即调用槽函数。如果信号和槽函数在同一线程，则直接调用，否则会导致线程跨越。使用此连接类型可以实现信号和槽的 **同步调用**** |
| 队列连接     | QueuedConnection                    | 队列连接，即信号发射时将事件添加到接收对象的事件队列中，稍后在接收对象的事件循环中调用槽函数。使用此连接类型可以实现 **跨线程的信号和槽通信** |
| 阻塞队列连接 | BlockingQueuedConnection            | 阻塞队列连接，与 `QtCore.Qt.QueuedConnection` 类似，但发送信号的线程会等待槽函数执行完毕后再继续执行 |

* 指定方式：`QObject.pyqtSignal_instance.connect(lambda var: handle_signal(var), connection_type)`

# 定时器QTimer

## 基本逻辑

* 在UI程序中，控制延迟任务的执行通常不能再用`time.sleep()`来实现，因为这样会使得主线程也休眠，导致UI假死

* 定时器`QTimer`的运行**依赖于事件循环**
* 事件循环可以是
  * `QtGui.QGuiApplication`, `QtCore.QCoreApplication`, `QtWidgets.QApplication`这些能够直接启动和管理事件循环的实例
  * `QObject`或者`QtCore.QThread`这种本身不具有事件循环，但是依赖于主线程的主事件循环的类
* 当在一个线程中创建并启动 `QTimer`，它会在<u>该线程的事件循环中</u>触发定时器事件。这意味着定时器事件将在该线程的上下文中执行，并且与其他事件和信号的处理是==异步==的
* 在多线程的情况下，Qt 使用了线程间的==事件队列==来传递事件和信号。所以，如果在一个线程中创建并操作 `QTimer`，需要确保在该线程中存在事件循环，以便定时器事件能够被触发和处理。

## 一个例子

* 在一个主事件循环中通过不同时间间隔来循环遍历输出一个字典的不同类型的值`values()`:

  ```python
  import sys
  
  from PyQt6.QtCore import QTimer, QCoreApplication
  from PyQt6 import QtGui, QtCore, QtWidgets
  from threading import Timer
  
  # 可以继承自：QtGui.QGuiApplication, QtCore.QCoreApplication, QtWidgets.QApplication
  class DictPrint(QtWidgets.QApplication):
      def __init__(self, run_commands, receive_status, parent=None):
          super().__init__(parent)
          self.run_commands = run_commands
          self.receive_status = receive_status
          self.timer_run = QtCore.QTimer()
          self.count_inner = 0
          self.count_outer = 0
          self.list_dict_items = run_commands
          self.parent = parent
  
      # print(list_dict_items)  # 返回第一个元组的第一个元素：即'a': {'1': 2, '2': 3, '3': 4},的键“a”
      def print_dict_elements(self):
          if self.count_outer < len(self.list_dict_items):
              if isinstance(list(self.list_dict_items[self.count_outer])[1], dict):
                  value_to_list = list(self.list_dict_items[self.count_outer])
                  dict_to_list = list(value_to_list[1].values())
                  if self.count_outer < len(self.list_dict_items):  # 控制外层循环
                      print(f"{dict_to_list[0]} - {dict_to_list[1]}")
                      self.timer_run.singleShot(800, self.print_dict_elements)
                      print('count_outer', self.count_outer)
                      self.count_inner = 0
                      self.count_outer += 1
                      self.print_dict_elements()
                  else:
                      self.timer_run.stop()
              elif isinstance(list(self.list_dict_items[self.count_outer])[1], list):
                  value_to_list = list(self.list_dict_items[self.count_outer])
                  if self.count_outer < len(self.list_dict_items):
                      if self.count_inner < len(value_to_list[1]):
                          print(
                              f"{list(self.list_dict_items[self.count_outer])[0]} - {list(self.list_dict_items[self.count_outer])[1][self.count_inner]}")
                          self.timer_run.singleShot(800, self.print_dict_elements)
                          self.count_inner += 1
                      else:
                          self.count_inner = 0
                          self.count_outer += 1
                          print('count_outer', self.count_outer)
                          self.print_dict_elements()
                  else:
                      self.timer_run.stop()
              elif isinstance(list(self.list_dict_items[self.count_outer])[1], str):
                  value_to_list = list(self.list_dict_items[self.count_outer])
                  if self.count_outer < len(self.list_dict_items):
                      print(f"{value_to_list[0]} - {value_to_list[1]}")
                      self.timer_run.singleShot(500, self.print_dict_elements)
                      self.count_outer += 1
                  else:
                      print('count_outer', self.count_outer)
                      self.timer_run.stop()
                      self.print_dict_elements()
              elif isinstance(list(self.list_dict_items[self.count_outer])[1], bytes):
                  value_to_list = list(self.list_dict_items[self.count_outer])
                  if self.count_outer < len(self.list_dict_items):
                      if self.count_inner < 10:
                          print(f"{value_to_list[0]} - {value_to_list[1]}")
                          self.timer_run.singleShot(100, self.print_dict_elements)
                          self.count_inner += 1
                      else:
                          self.count_inner = 0
                          self.count_outer += 1
                          print('count_outer', self.count_outer)
                          self.print_dict_elements()
                  else:
                      self.timer_run.stop()
          else:
              self.timer_run.stop()
              self.quit()
              self.count_outer = 0
              self.count_inner = 0
  
  
  # timer_1.singleShot(1000, print_dict_elements)
  if __name__ == '__main__':
      dict_timer_test = {'Clear target t:': '@cttime\r\n',
                         'b': [1, 2, 3, 4],
                         'Clear target V:': '@ctvolume\r\n',
                         'Writes to memory: OFF:': '@NVRAM\r\n',
                         'Default force level': '@force 50\r\n',
                         '1': {'prompt': '>>Syringe selected: air, 1 ml, 4.69 mm',
                               'command': '@syrm air, 1 ml, 4.69 mm\r\n'},
                         '2': {'prompt': '>>Infusion rate: 3.2963 ml/min',
                               'command': '@irate 3.2963 ml/min\r\n'},
                         '3': {'prompt': '>>Target Volume: 2 pl',
                               'command': '@tvolume 2 pl\r\n'},
                         '4': {'prompt': '>>Infusion running:',
                               'command': '@irun\r\n'},
                         '5': b'@status\r\n'}
      app = DictPrint(run_commands=list(dict_timer_test.items()), receive_status=None, parent=sys.argv)
      app.print_dict_elements()
      sys.exit(app.exec())
  ```

  



# 多线程

## **界面更新**

* PyQt 的界面组件应该只在**主线程**中进行操作。如果在其他线程中直接操作界面组件，可能会导致线程安全问题和意外行为。如果需要在其他线程中进行一些耗时的操作，可以使用信号和槽机制或者线程通信来将结果传递给主线程，在主线程中更新界面
  * <u>或者通过在线程中创建类变量</u>，然后在主线程中通过一个<u>定时器</u>轮训获取这个变量，来实现在主线程中对主界面组件的操作
  * 

## **线程通信**

* 在多线程应用程序中，线程之间的通信非常重要。如信号和槽、事件和队列。使用适当的线程通信机制可以确保线程之间的安全数据交换
* 

## **线程同步**

* 当多个线程访问共享数据时，需要注意线程同步。使用适当的同步机制（如互斥锁、信号量等）可以避免多个线程同时修改共享数据而导致的数据竞争和不一致性

  ```python
  self.mutex = QtCore.QMutex()
  ...
  self.mutex.lock() 		# 获取锁。如果当前锁空闲，那么在加锁之后继续运行当前线程，如果该锁当前被其他线程持有，那么当前线程会被阻塞，知道获取锁成						   功为止
  """
  一系列操作
  """
  self.mutex.unlock()  	# 完成后释放锁，避免阻塞其他线程的执行
  ```

* 长时间运行的任务：如果有长时间运行的任务，例如计算密集型的操作或网络请求等，建议将这些任务放在单独的线程中执行，以避免阻塞主线程导致界面失去响应

  

## **线程终止**

* 在线程终止时需要注意合理的线程退出方式。确保线程能够安全地退出并释放资源，以避免内存泄漏和其他潜在问题

  * 设置线程运行标志：
    ```python
    class ReadSendPort(QtCore.QThread):
        def __init__(self, check_serial_thread=None, ser=None, ui_main=None, parent=None):
            super().__init__(parent)
            self.running = True
            ...
        def run(self):
            if self.ser is None:
                self.quit()
                return
            else:
                pass
    		# 按照运行标识来确定线程是否要启动
            while self.ser and self.running:
                ...
        def stop(self):
            self.running = False
    ```

    在其他线程中通过调用`self.read_send_thread.stop()`的方法就可以使`ReadSendPort`线程停止

  * 通过`terminate()`方法：可能会造成资源无法释放，线程无法安全退出的风险

    ```python
    """CheckSerialThread()类中"""
        def stop_read_send_thread(self):
            if self.read_send_thread:
                self.read_send_thread.terminate()
    ```

## **线程休眠**：

* `self.wait_condition = QtCore.QWaitCondition()`和`self.wait_condition.wakeAll()`

  ```python
  class CheckSerialThread(QtCore.QThread):
      def __init__(self, ui, parent):
          super().__init__(parent)
          self.auto_reconnect = True						# 自动重启线程的标志
          self._pause_thread = False  					# 暂停串口检测线程的标志
          self.mutex = QtCore.QMutex()					# 主线程休眠锁
          self.wait_condition = QtCore.QWaitCondition()   # 线程休眠
      def run(self):
      	self.mutex.lock()
      	try:
      		if self._pause_thread and not self.auto_reconnect:
      			self.wait_condition.wait(self.mutex)	# 在线程休眠时要避免其他线程访问和修改其资源
      		else:
                  ...
                  
     	# 唤醒线程的方法：self.wait_condition.wakeAll()
  	def resume_thread(self):
          self.auto_reconnect = True
          self._pause_thread = False
          self.wait_condition.wakeAll()
  ```

  

# Logging

* 需要导入：`import logging.config`模块
* 按照记录的严重程度分为：
  - `debug`
  - `info`
  - `warning`
  - `error`
  - `critical`
* 导入字典配置文件：`*from* settings *import* settings_log`
  * 日志记录的**格式、等级、传递、日期** 等都可以在配置文件中修改
  * [settings_log.py](https://drive.google.com/file/d/19H4I18ID0DHaCX8yM2LFBUQG1JBNSYMc/view?usp=share_link)

* 配置日志记录器：

  ```python
  # Configuration logging functionality
  logging.config.dictConfig(settings_log.LOGGING_DIC)
  logger_debug_console = logging.getLogger('logger1')  		# Console print
  logger_info_console_file = logging.getLogger('logger2')  	# Console & file recording
  logger_info_file = logging.getLogger('logger3')				# File writing
  ```

* 使用：
  ````python
  # 输出到控制台
  logger_debug_console.info(f"错误信息：{str(e)")
  # 输出到控制台& 记录到日志文件
  logger_info_console_file.debug(f"错误信息：{str(e)")
  # 只记录到文件
  logger_info_file.info(f"错误信息：{str(e)")
  ````

  

📘<<[Part 09](./Python_Part_09-QT_01.md) | [Part 11](./Python_Part_10-QT_02.md)]>> 

