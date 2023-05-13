<sub>Title: Python 学习日记 - 正则表达<br>Author:<a href="https://github.com/Alpaka1017?tab=repositories" target="_blank">Xueyong Lu  <i class="fa fa-github" aria-hidden="true"></i></a></br><small>First Edition: March - 2023</small></sub>

<div align = "center">
    <h1>Python学习日记 - Part 02</h1>
</div>
<div align = "right">
	<h2>Regular Expression正则表达式</h2>
</div>




📘<<[Part 01](./Python_Part_01-Git入门.md) | [Part 03](./Python_Part_03-Numpy_01.md)]>> 

正则表达的作用是***处理文本、提取期望的信息***，在其他的很多语言中也是类似的表达，而不只是Python。当然也可以用在Python中提供了很多种字符串对象的内置处理方法，如**.split()**、**.find()**、**.index()**等。

## 1.1 一个例子

```
Python3 高级开发工程师 上海互教教育科技有限公司上海 - 浦东新区2万/月 02-18满员
测试开发工程师（C++/python）上海墨鹍数码科技有限公司上海 - 浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海 - 徐汇区1.3万/每月02-18剩余11人
测试开发工程师（Python） 赫利普（上海）信息科技有限公司上海 - 浦东新区1.1万/每月02-18剩余5人
Python 高级开发工程师 上海行动教育科技股份有限公司上海 - 闵行区2.8万/月02-18剩余255人
python 开发工程师 上海优似腾软件开发有限公司上海 - 浦东新区2.5万/每月02-18满员
```

> 期望输出：
>
> ```2
> 2.5
> 1.3
> 1.1
> 2.8
> 2.5

### 1.1.1通过Python内置函数及方法：

```python
### 要求：提取每个职位的薪资 ###
content = ''' '''

# 将文本内容按照行放入列表
lines = content.splitlines()
# 对每一行文本进行分析：按照规律可知，期望薪资的单位是“万/每月”或者“万/月”，那么这两个字符串前的数字即为期望输出
for line in lines:
    # 用匿名函数 lambda x: ... 其中x为形参
    # lambda x: 当if为真时，运行第一个函数，否则则为第二个
    pos2 = (lambda x: line.find(x) if line.find(x) != -1 else None)('万/每月') or (
        lambda x: line.find(x) if line.find(x) != -1 else None)('万/月')

    if isinstance(pos2, int):
        idx = pos2 - 1
        # 只要是数字或者小数点，那么就继续向前查找
        while line[idx].isdigit() or line[idx] == '.':
            idx -= 1
            # 循环完成后，idx指向的下标就是数字前面的字符
            # 那么数字的起始索引值就是 idx+1
        pos1 = idx + 1
        print(line[pos1:pos2])
```

### 1.1.2 通过正则表达式：

```python
import re
p = re.compile(r'([/d.]+万/每{0,1}月)') # r'([/d.]+万/每?月)'
for one in p.findall(content):
    print(one)
```

其中，`.../每{0,1}月`也可以写为`.../每?月`。

*`re.compile(r'_')`*函数的参数就是正则表达式的字符串。上面的例子指定的搜索子串的特征为 <font color = Blue> `([/d.]+万/每{0,1}月) `</font>，该函数会返回一个*compile*对象，*compile*对象的*`.findall`*方法返回**所有返回的子串**，并放在一个**列表**里。

正则表达式验证工具：[RegEx验证](https://regex101.com)

## 1.2 RegEx语法

正则表达式中包含两种字符，一种是直接进行相同匹配的字符**普通字符**；一种是特殊的字符，也被成为**元字符（metacharacters）**，如:

` . * + ? / [ ] ^ $ {} | () `

### 1.2.1 <a id = "RegEx_dot">任意字符`.`</a>

> 表示要匹配**除了换行符以外的**<mark>任何单个</mark>字符

> ```示例
> 苹果是绿色的
> 香蕉是黄色的
> 橙子是橙色的
> 乌鸦是黑色的
> ```
>
> > 找出上面文本中的所有颜色：
> >
> > ```python
> > import re
> > text = '''
> >         苹果是绿色的
> >         橙子是橙色的
> >         香蕉是黄色的
> >         乌鸦是黑色的'''
> > char_match = re.compile(r'(.色)')
> > for element in char_match.findall(text):
> >     print(element)
> > ```
> >
> > > 运行结果如下：
> > >
> > > ```python
> > > 绿色
> > > 黄色
> > > 橙色
> > > 黑色
> > > 
> > > Process finished with exit code 0
> > > ```

### 1.2.2 任意次` *`

> 表示匹配`*`**前面**的**子表达式**<mark>任意次</mark>，包括0次

> ```示例 
> 苹果，是绿色的
> 橙子，是橙色的
> 香蕉，是黄色的
> 乌鸦，是黑色的
> ```
>
> > 从以上文本中，找出每行“，”之后的内容，包括“，”本身。
> >
> > ```python
> > import re
> >     text = '''
> >         苹果，是绿色的
> >         橙子，是橙色的
> >         香蕉，是黄色的
> >         乌鸦，是黑色的'''
> > str_match = re.compile(r'(，.*)')
> > for element in str_match.findall(text):
> >     print(element)
> > ```
> >
> > `(，.*)`表示：从`“，”`开始，任意次数`“*”`的任意字符`“.”`
> >
> > > 运行结果如下：
> > >
> > > ```python
> > > ，是绿色的
> > > ，是橙色的
> > > ，是黄色的
> > > ，是黑色的
> > > ```

### 1.2.3 任意非零次`+`

> 表示匹配`+`**前面**的**子表达式**<mark>一次或多次</mark>，不包括0次

### 1.2.4 指定次`{}`

> 表示匹配**前面**的**子表达式**<mark>指定次数</mark>：`X{a,b}`要匹配的X元素出现**至少a次，最多b次**。

> ```示例
> text = '''
>             张飒，158 4665 7365，43
>             李嗣，178 6543 6789，26
>             杨武，134 7965 7321，36
>             王陆，165 7865 1354，34
>             刘琦，173 6543 8654，45'''
> ```
>
> > 如从以上文本中提取电话号码信息：
> >
> > ```python
> > info_match = re.compile(r'(/d{3}./d{4}./d{4})')
> > for number in info_match.findall(text):
> >     print(number)
> > ```
> >
> > > 输出为：
> > >
> > > ```python
> > > 158 4665 7365
> > > 178 6543 6789
> > > 134 7965 7321
> > > 165 7865 1354
> > > 173 6543 8654
> > > ```

### 1.2.5 贪婪模式和非贪婪模式

例如要把下面字符串中的所有`html`标签提取出来：

```python
source = '<html><head><title>Title</title>'
```

得到如下列表：

```python
['<html>', '<head>', '<title>', '</title>']
```

利用`<.*>`表示在`<>`中出现的任意次数的任意字符来表示一个`html`标签，理论上是可行的，下面是实际运行的结果：

```python
<html><head><title>Title</title>
```

原因是，在正则表达式中 `'*', '+', '?'`都是“贪婪的”，它们会尽可能多地匹配内容，所以用`<.*>`就表示从第一个`<`一直匹配到了最后一个`>`。要得到期望输出，需采用**非贪婪模式**，在`*`后面加`?`，变成`<.*?>`。（控制“尽可能多”还是“尽可能少”）

```python
source = '<html><head><title>Title</title>'
    tag_match = re.compile(r'(<.*?>)')
    print(tag_match.findall(source))
    for tag in tag_match.findall(source):
    	print(tag)
```

输出变为：

```python
['<html>', '<head>', '<title>', '</title>']
<html>
<head>
<title>
</title>
```

### 1.2.6 元字符的转义

> 对==元字符==本身进行匹配

> ```python
> text = '''
> 		苹果.是绿色的
> 		橙子.是橙色的
> 		香蕉.是黄色的'''
> ```
>
> > 提取上面文本中所有在`.`之前的字符
> >
> > ```python
> > extract_info = re.compile(r'(.*/.)')
> >  for element in extract_info.findall(text):
> >      print(element)
> > ```
> >
> > > 输出如下结果：
> > >
> > > ```python
> > >      苹果.
> > >      橙子.
> > >      香蕉.
> > > ```
> > >
> > > **注意在文本中如果包括tab缩进和空格，在用`.*`也能够被匹配。*(见[`正则表达：.`](#RegEx_dot))

> 匹配==某种类型==的字符

| 转义表示 |    等同表达     | 描述                                 | 补充                                                         |
| :------: | :-------------: | :----------------------------------- | ------------------------------------------------------------ |
|   `/d`   |     `[0-9]`     | 任意==数字字符==                     |                                                              |
|   `/D`   |    `[^0-9]`     | 任意==非数字==字符                   |                                                              |
|   `/s`   | `[/t/n/r/f/v]`  | 任意==空白==字符: 空格、Tab、换行等  |                                                              |
|   `/S`   | `[^/t/n/r/f/v]` | 任意==非空白==字符                   |                                                              |
|   `/w`   |  `[a-zA-Z0-9]`  | 任意==文字字符==：字母、数字、下划线 | `re.compile(r'(/w{2,4})',re.A)` 参数`re.A`表示匹配的是**ASCII**码字符 |
|   `/W`   | `[^a-zA-Z0-9]`  | 任意==非文字==字符                   |                                                              |

转义匹配的不同`re.`方法见下表：

| Flag                       | 含义                                                    |
| -------------------------- | ------------------------------------------------------- |
| ASCII, A                   | 使个别转义匹配`/w, /b, /s, /d`只对**ASCII**字符进行匹配 |
| DOTALL, S                  | 使`.`匹配**任意字符**，包括换行                         |
| IGNOREXCASE, I             | **大小写**不敏感**case-insensitive**匹配                |
| LOCALE, L                  | **local-aware**匹配                                     |
| MULTILINE, M               | **multi-line**匹配，影响`^`和`$`                        |
| VERBOSE, X(for 'extended') | 启用冗长**verbose** REs，便于组织和理解                 |

### 1.2.7 指定字符`[]`

> 匹配几个指定的字符之一

> > ```示例
> > text = '''
> >         张飒，138 4665 7365，43
> >         李嗣，178 6543 6789，26
> >         杨武，114 7965 7321，36
> >         王陆，235 7865 1354，34
> >         刘琦，1b3 6543 8654，45
> >         孙八一， 156 4657 1231,30'''
> > ```
> >
> > 对以上信息提取有效的电话号码：开头为1，并且第二位为3-8
> >
> > > ```python
> > > def RegEx_square_brackets():
> > >     import re
> > >     Number_match = re.compile(r'(1[3-8]/d./d{4}./d{4})')
> > >     for number in Number_match.findall(text):
> > >         print(number)
> > > ```
> > >
> > > > 输出为：
> > > >
> > > > ```python
> > > > 138 4665 7365
> > > > 178 6543 6789
> > > > 156 4657 1231
> > > > ```

> 元字符在`[]`内不再具有特殊含义，而仅仅代表字符本身：
>
> > `r'([a-h][.+*])`

> 在方括号`[]`里使用`^`符号，表示**非**
>
> > ```python
> > strin = 's4d3a5sd4+da.546s87@%#Ad%645'
> > ```
> >
> > 对于以上字符串，有以下要求：
> >
> > * 提取字符串中的所有**数字字符**：
> > * 提取字符串中的所有**非数字字符**：
> > * 提取字符串中的所有**字母**：
> > * 提取字符串中的所有**特殊字符**：
> >
> > > ```python
> > > import re
> > >     strin = 's4d3a5sd4+da.546s87@%#Ad%645'
> > >     # 提取上述字符串中的数字
> > >     numbers = re.compile(r'([/d])')
> > >     # 提取上述字符串中的非数字
> > >     non_numbers = re.compile(r'([^/d])')
> > >     # 提取上述字符串中的字母
> > >     char_match = re.compile(r'([a-zA-Z])')
> > >     # 提取上述字符串中的特殊字符
> > >     spec_char = re.compile(r'([^a-zA-Z0-9])')
> > >     print(numbers.findall(strin))
> > >     print(non_numbers.findall(strin))
> > >     print(char_match.findall(strin))
> > >     print(spec_char.findall(strin))
> > > ```
> > >
> > > > 输出为：
> > > >
> > > > ```python
> > > > 字符串中包括的数字为： ['4', '3', '5', '4', '5', '4', '6', '8', '7', '6', '4', '5']
> > > > 字符串中包括的非数字为： ['s', 'd', 'a', 's', 'd', '+', 'd', 'a', '.', 's', '@', '%', '#', 'A', 'd', '%']
> > > > 字符串中包括的字母为： ['s', 'd', 'a', 's', 'd', 'd', 'a', 's', 'A', 'd']
> > > > 字符串中包括的特殊字符为： ['+', '.', '@', '%', '#', '%']
> > > > ```

### 1.2.8 起始位置和单行/多行模式

> `^`除了表示**非**以外，还能用于表示文本的开头

> ```示例
> text = '''001-苹果价格-10
> 002-橙子价格-12
> 003-香蕉价格-16'''
> ```
>
> > 获取每一类水果的标号：
> >
> > ```python
> > start_tags = re.compile(r'(^/d+)')
> >     for tag in start_tags.findall(text):
> >         print(tag)
> > ```
> >
> > 输出为: `001`，也就是只输出了第一行
> >
> > 要分别输出每一行的标签，需要用到多行模式`re.M`
>
> ```示例
> text = '''001-苹果价格-10/n002-橙子价格-12/n003-香蕉价格-16'''
> ```
>
> > 上述方法适用于在前面`def`了新的函数，造成`text`的异常缩进，因为多行模式并不能处理缩进。
> >
> > ```python
> > start_tags = re.compile(r'^/d+', re.M)
> >     for tag in start_tags.findall(text):
> >         print(tag)
> > ```
> >
> > > 输出为：
> > >
> > > ```python
> > > 001
> > > 002
> > > 003
> > > ```

> `$`用来表示单行/多行模式的末尾匹配

> 上例获取价格：
>
> ```python
> end_price = re.compile(r'(/d+$)', re.M)
> for price in end_price.findall(text):
>     print(price)
> ```
>
> > 输出结果
> >
> > ```python
> > 10
> > 12
> > 16
> > ```
> >
> > 注意的是，如果是单行模式，但文本是多行，那么用`$`匹配定位到的是整个文本的最后一行。

### 1.2.9 组选择`()`

> 用以选择==某一类符合特征==的字符串

> ```python
> 苹果，苹果是绿色的
> 橙子，橙子是橙色的
> 香蕉，香蕉是黄色的
> ```
>
> > 从以上文本中提取水果类型，不包括`，`：用组选择方法：`r'(.*)，'`。逗号`，`作为匹配标识符放在`()`外面，在匹配时不被选择。
> >
> > ```python
> > import re
> > text = '''苹果，苹果是绿色的/n橙子，橙子是橙色的/n香蕉，香蕉是黄色的'''
> > fruits_match = re.compile(r'(.*)，')
> > for fruit in fruits_match.findall(text):
> >     print(fruit)
> > ```
> >
> > > 输出结果为：
> > >
> > > ```python
> > > 苹果
> > > 橙子
> > > 香蕉
> > > ```

> 当有多个组时：在上述文本中，分别提取水果==类型==和==颜色==，并输出结果：
>
> > ```python
> > fruits_match_multigroup = re.compile(r'(.*)，.*(.色)')
> > for fruit_multi_group in fruits_match_multigroup.findall(text):
> >     print(fruit_multi_group)
> > ```
> >
> > 结果输出为：
> >
> > > ```python
> > > ('苹果', '绿色')
> > > ('橙子', '橙色')
> > > ('香蕉', '黄色')
> > > ```
> > >
> > > 在多个组选择时，输出的结果为每一行匹配结果的==元组==，而不再是列表。

## 1.3 正则表达式的方法

### 1.3.1 切割字符串

字符串对象提供的`.split()`方法仅适用于简单的字符串分割情形，对于更加复杂、灵活的应用场景，可以用正则表达式中的切割方法`re.split()`。

> 提取下面字符串中的名字：
>
> ```py
> text = '''关羽；张飞，赵云、马超,黄忠，   马岱/n  魏延，严颜'''
> ```
>
> > ```python
> > import re
> >     nameList = re.split(r'[；，、,/s]/s*', text)
> >     print(nameList)
> > ```
> >
> > 输出结果为：
> >
> > ```python
> > ['关羽', '张飞', '赵云', '马超', '黄忠', '马岱', '魏延', '严颜']
> > ```
> >
> > 上面正则表达式`r'[；，、,/s]/s*'`表示：首先对`[...]`中的符号进行匹配切割，然后加上后面的`/s`任意个空白字符（空格、换行、Tab等）。

### 1.3.2 Sub替换

> ```python
> def RegEx_subFunc(match):
>     # Match对象的.group(0)返回的是整个匹配到的字符串
>     src = match.group(0)
> 
>     # Match对象的.group(1)返回的是第一个组的内容
>     number_subfunc = int(match.group(1)) + 6
>     dest = f'av{number_subfunc}' # 字符串连接
> 
>     print(f'{src}替换为{dest}')
>     # 返回的值就是最终替换的字符串
>     return dest
> ```
>
> ```python
> def RegEx_match_replace():
>     links = '''
> 
>     下面是这学期要学习的课程：
> 
>     <a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
>     这节讲的是牛顿第2运动定律
> 
>     <a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
>     这节讲的是毕达哥拉斯公式
> 
>     <a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
>     这节讲的是切割磁力线
>     '''
>     
>     print_str = re.compile(r'av(/d*)/')  # r'/av(/d+?)/'
>     print(print_str.findall(links))
>     
>     newStr = re.sub(r'av(/d*)', RegEx_subFunc, links)
>     print(newStr)
> ```
>
> > 输出结果为：
> >
> > ```python
> > ['66771949', '46349552', '90571967']
> > av66771949替换为av66771955
> > av46349552替换为av46349558
> > av90571967替换为av90571973
> > 
> > 
> >     下面是这学期要学习的课程：
> > 
> >     <a href='https://www.bilibili.com/video/av66771955/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
> >     这节讲的是牛顿第2运动定律
> > 
> >     <a href='https://www.bilibili.com/video/av46349558/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
> >     这节讲的是毕达哥拉斯公式
> > 
> >     <a href='https://www.bilibili.com/video/av90571973/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
> >     这节讲的是切割磁力线
> >     
> > ```



📘<<[Part 01](./Python_Part_01-Git入门.md) | [Part 03](./Python_Part_03-Numpy_01.md)]>> 
