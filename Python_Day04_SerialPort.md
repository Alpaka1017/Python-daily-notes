<sub>Title: Python 学习日记 - 串口通信<br>Author:<a href="https://github.com/Alpaka1017?tab=repositories" target="_blank">Xueyong Lu  <i class="fa fa-github" aria-hidden="true"></i></a></br><small>First Edition: March - 2023</small></sub>

<div align = "center">
    <h1>
        Python 学习日记 - Day 04
    </h1>
</div>
<div align = "right">
    <h2>串口通信</h2>
</div>


📘<<[Day 03](./Python_Day03_Numpy_lib_Part2.md) | [Day 05](./Python_Day05_MagicFunc.md)]>> 

## 1.串口通信基础

### 1.1 基本概念

* **波特率（Baudrate）：**波特率表示==单位时间内传送的[码元](https://baike.baidu.com/item/码元/10525003?fromModule=lemma_inlink)符号的个数==。由于异步串口通信没有时钟，波特率旨在为其指定一个调制载波的频率

* **起始位/停止位：**数据包从起始位开始，到停止位结束。起始信号用==逻辑0==的数据位表示，停止信号由==0.5、1、1.5或2个逻辑1==的数据位表示。串口通信的两个对象之间要约定一致起停位。

* **有效数据：**起始位和结束位之间的数据长度，一般被约定为5、6、7或8位长

* **数据校验：**在有效数据之后加上校验位，以解决因干扰出现的数据通信偏差

  * 奇校验（odd）：要求有效数据和校验位中“1”的个数为奇数。最后传输的是8位有效数据加1位校验位，共9位。
  * 偶校验（even）：要求有效数据和校验位的“1”数量为偶数。同9位
  * 0校验（space）：校验位总是为“0”
  * 1校验（mark）：校验位总是为“1”

  <img src="./.msc/image/serial_communication.png" style="zoom:67%;" />

* **波特率的计算**

  * R232：同步传输

    `波特率 = 时钟频率 / (分频器值 × (分频器倍增值 + 1))`

  * USB：异步传输

    `波特率 = 时钟频率 / (分频器值 × 分频器倍增值 × 数据包长度)`

* **通信速率的计算**

  * **R232 (bps)：**9600bps的波特率、8位数据位、1个校验位和1位停止位

    $传信率 = /dfrac{9600bps}{8+1+1} = 960 bits/s$

  * **USB：**取决于USB版本（最大传输速率）、数据包长度、数据重传次数、总线带宽等



----

## 2. **`PySerial`**

**`PySerial`**模块封装了Python对于串口访问的方法及函数。

* **安装`PySerial`库**

  ```python
  pip install PySerial
  
  >> import serial
  ```

### 2.1 打开串口

```python
import serial

ser = serial.Serial('COM3', 115200, 8, 'N', 2, timeout=1)

ser = serial.Serial(port,                 # 串行口端口（地址）：'COM3' for windows; '/dev/ttyUSB0' for linux
                    baudrate=9600, 		  # 波特率，用于指定通信速率，例如 9600、115200 等。默认值是 9600
                    bytesize=8, 		  # 每个字节的位数，取值范围为 5 到 8 位。默认值是 8
                    parity='N', 		  # 校验位，可以是 'N = 无校验'、'E = 偶校验'、'O = 奇校验'、'M = 标记校验'、'S = 空格校验'
                    stopbits=1, 		  # 停止位，可以是 1 或者 2。默认值是 1
                    timeout=None, 		  # 超时时间(s)，无数据读取，超时自动退出。默认值是 None，表示永远等待
                    xonxoff=False, 		  # 软件流控制。默认值是 False，表示关闭软件数据流控制
                    rtscts=False, 		  # 硬件流控制。默认值是 False，表示关闭硬件数据流控制
                    dsrdtr=False，		 # 硬件流控制，取值为True或False。默认为False
                   	write_timeout= ,	  # 写操作的超时时间，以秒为单位。默认为None，即无超时
                   	inter_byte_timeout= , # 两个连续字节之间的超时时间，以秒为单位。默认为None，即没有超时
                   	exclusive=False,)	  # 独占模式。如果为True，则在打开串口时锁定它，防止其他应用程序访问该串口。win32只能为True。
```

### 2.2 设置串口状态

```python
# ValueError：参数错误
# SerialException：找不到设备或不能配置

ser.baudrate＝9600						 #设置波特率

ser.bytesize＝8							 #字节大小

ser.bytesize＝serial.EiGHTBITS			 #8位数据位

ser.parity=serial.PARITY_EVEN			  #偶校验

ser.parity=serial.PARITY_NONE			  #无校验

ser.parity=serial.PARITY_ODD			  #奇校验
```

### 2.3 向串口发送数据

* `ser.write()`用以上位机向串口设备发送指令

  ```python
  command = b'add. 6/r/n'
  ser.write(command_add)
  
  # 如果发送的指令为一字符串，则要注意在发送时的编码问题，因为串口只能接收`bytes`类型的字符
  command = 'add. 6/r/n'
  ser.write(command.encode())
  # 编码的方式有`utf-8`、`ascii`、`unicode`等
  ```

  * ==**字节串**==：**`b''`**在Python中表示一个字节串对象(**Bytes object**)，其中的每一个字符都用一个字节表示

    通常字节串用来表示==**二进制**==数据，例如串口通信中的发送和接收数据

### 2.4 从串口接收数据

* **`ser.read()`**: 提供了从串口每次接收**一个字符**的方法

  ```python
  data = ser.read(size=1)
  # 返回size字节数组，长度为size
  # 注意：用read()方法时，可能会引起串口缓冲区的数据积累
  ```

* **`ser.readline()`**: 提供了从串口每次接收**一行数据**的方法

  ```python
  # 这个方法可以读取一行数据，即遇到 换行符/n 或者 回车符/r 就停止读取，并返回读取到的数据
  # 返回值是一个字节数组
  # 打开串口时应该指定超时，否则如果串口没有收到新行，则会一直等待。如果没有超时，readline会报异常
  # 读取多行返回数据时：
  response = ser.readline()
  while response.endswith(b'/r/n'):
      response += ser.readline()3
      
  print(response.decode('utf-8'))
  ```

* **`ser.readlines()`**: 提供了从串口一次接收**多行数据**的方法

  ```python
  # 返回的是一个包含多行数据的列表
  # 列表的每一个元素都为字节组成的数组
  ```

* 如果发送的数据采取了特殊的**编码方式**，那么在接收数据到上位机进行解析的时候同样需要以相同的解码方式进行解码

  ```python
  response = ser.readline().decode('utf-8').strip()
  # Python本身的.strip()方法可以去掉字符串中的特定字符
  ```

  * 常用的编码方式：
    * **`ascii`**：ASCII
    * **`utf-8`**：Unicode
    * 默认为**`utf-8`**的字节串

* 除此之外，要想获得串口返回数据中的有效部分，还需要对返回的字符数组进行处理，比如切片、提取数值数据等

* **PHD-Ultra series**返回的响应格式为：

  ```python
  b'/n09:Command error: /r/n'
  # 即末尾以'/r/n‘结尾
  ```

### 3. PHD-Ultra Series

#### 3.1 自定义New method

*  选择**Syringe**，如果在新建方法的时候未指定Syringe，那么默认的为当前Quick mode中使用的Syringe

* 新建**Step**，并为**Step**创建一个**Profile**

  | 样式                                                         | 参数                                                         |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | <img src="./.msc/image/ultra_const_rate.png" alt="ultra_const_rate" style="zoom:67%;" /> | **$·$** 方向<br />**$·$**  速率                              |
  | <img src="./.msc/image/ultra_ramp.png" alt="ultra_ramp" style="zoom:67%;" /> | **$·$** 方向<br />**$·$**  开始和结束的速率<br />**$·$**  目标时长 |
  | <img src="./.msc/image/ultra_stepped.png" alt="ultra_stepped" style="zoom:67%;" /> | **$·$**  方向<br />**$·$**  开始和结束的速率<br />**$·$**  时长和步长 |
  | <img src="./.msc/image/ultra_pulse.png" alt="ultra_pulse" style="zoom:67%;" /> | **$·$**  方向<br />**$·$**  速率R1和R2<br />**$·$**  Volumen V1和V2/ 时长T1和T2<br />**$·$**  脉冲个数 |
  | <img src="./.msc/image/ultra_bolus.png" alt="ultra_bolus" style="zoom:67%;" /> | **$·$**  目标体积<br />**$·$**  目标时间                     |
  | <img src="./.msc/image/ultra_concentration.png" alt="ultra_concentration" style="zoom:67%;" /> | **$·$**  体重<br />**$·$**  注射速率和Concentration [mg/ml或%]<br />**$·$**  剂量[mg/kg]或者时长<br />**$·$**  Doses + time lag |
  | <img src="./.msc/image/ultra_gradient.png" alt="ultra_gradient" style="zoom:67%;" /> |                                                              |
  | <img src="./.msc/image/ultra_autofill.png" alt="ultra_autofill" style="zoom:67%;" /> |                                                              |
  | <img src="./.msc/image/ultra_advanced_opts.png" alt="ultra_advanced_opts" style="zoom:67%;" /> |                                                              |
  
  
