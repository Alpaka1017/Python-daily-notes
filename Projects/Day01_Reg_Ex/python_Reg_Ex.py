### 要求：提取每个职位的薪资 ###
import re

content = '''
            Python3 高级开发工程师 上海互教教育科技有限公司上海 - 浦东新区2万/月 02-18满员
            测试开发工程师（C++/python）上海墨鹍数码科技有限公司上海 - 浦东新区2.5万/每月02-18未满员
            Python3 开发工程师 上海德拓信息技术股份有限公司上海 - 徐汇区1.3万/每月02-18剩余11人
            测试开发工程师（Python） 赫利普（上海）信息科技有限公司上海 - 浦东新区1.1万/每月02-18剩余5人
            Python 高级开发工程师 上海行动教育科技股份有限公司上海 - 闵行区2.8万/月02-18剩余255人
            python 开发工程师 上海优似腾软件开发有限公司上海 - 浦东新区2.5万/每月02-18满员
            python 开发工程师 上海优似腾软件开发有限公司上海 - 浦东新区
'''

### 通过Python内置函数及方法 ###
def str_process_salary():
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

### 通过正则表达式的方法 ###
def RegEx_salary():
    import re
    p = re.compile(r'([\d.]+万/每?月)')
    for one in p.findall(content):
        print(one)

### 找出下面文本中所有颜色:正则表达“.”
def RegEx_dot():
    import re
    text = '''
        苹果是绿色的
        香蕉是黄色的
        橙子是橙色的
        乌鸦是黑色的'''
    char_match = re.compile(r'(.色)')
    for element in char_match.findall(text):
        print(element)

### 找出每行“，”之后的内容：正则表达“*”
def RegEx_star():
    import re
    text = '''
        苹果，是绿色的
        橙子，是橙色的
        香蕉，是黄色的
        乌鸦，是黑色的
        猴子，'''
    str_match = re.compile(r'(，.*)')
    for element in str_match.findall(text):
        print(element)

### 找出每组数据中的电话号：正则表达“{}”
def RegEx_curly_brace():
    import re
    number_list = []
    age_list = []
    text = '''
            张飒，158 4665 7365，43
            李嗣，178 6543 6789，26
            杨武，134 7965 7321，36
            王陆，165 7865 1354，34
            刘琦，173 6543 8654，45'''
    info_match = re.compile(r'(\d{3}.\d{4}.\d{4})')
    age_match = re.compile(r'(\d{2}$)')
    for number in info_match.findall(text):
        number_list.append(number)
        print(number)
    for age in age_match.findall(text):
        age_list.append(age)

### 贪婪模式与非贪婪模式
def RegEx_greed_model():
    import re
    source = '<html><head><title>Title</title>'
    tag_match = re.compile(r'(<.*?>)')
    print(tag_match.findall(source))
    for tag in tag_match.findall(source):
        print(tag)
        print(type(tag))

### 对元字符本身进行匹配：转义\
def RegEx_excape ():
    import  re
    text = '''
        苹果.是绿色的
        橙子.是橙色的
        香蕉.是黄色的'''
    extract_info = re.compile(r'(.*\.)')
    for element in extract_info.findall(text):
        print(element)

### 匹配几个指定的字符之一：[]
def RegEx_square_brackets():
    import re
    text = '''
        张飒，138 4665 7365，43
        李嗣，178 6543 6789，26
        杨武，114 7965 7321，36
        王陆，235 7865 1354，34
        刘琦，1b3 6543 8654，45
        孙八一， 156 4657 1231,30'''
    Number_match = re.compile(r'(1[3-8]\d.\d{4}.\d{4})')
    for number in Number_match.findall(text):
        print(number)

### 非'^':
def RegEx_not():
    import re
    strin = 's4d3a5sd4+da.546s87@%#Ad%645'
    # 提取上述字符串中的数字
    numbers = re.compile(r'([\d])')
    # 提取上述字符串中的非数字
    non_numbers = re.compile(r'([^\d])')
    # 提取上述字符串中的字母
    char_match = re.compile(r'([a-zA-Z])')
    # 提取上述字符串中的特殊字符
    spec_char = re.compile(r'([^a-zA-Z0-9])')
    print('字符串中包括的数字为：', numbers.findall(strin))
    print('字符串中包括的非数字为：', non_numbers.findall(strin))
    print('字符串中包括的字母为：', char_match.findall(strin))
    print('字符串中包括的特殊字符为：', spec_char.findall(strin))

### 起始/结尾和多行控制: ^, $和re.M
def RegEx_start_end_multi():
    import re
    text = '''001-苹果价格-10\n002-橙子价格-12\n003-香蕉价格-16'''
    start_tags = re.compile(r'(^\d+)', re.M)
    end_price = re.compile(r'(\d+$)', re.M)
    for tag in start_tags.findall(text):
        print(tag)
    for price in end_price.findall(text):
        print(price)

### 选择符合特定类型的字符串：组匹配()
def RegEx_group_bracket():
    import re
    text = '''苹果，苹果是绿色的\n橙子，橙子是橙色的\n香蕉，香蕉是黄色的'''
    fruits_match = re.compile(r'(.*)，')
    fruits_match_multigroup = re.compile(r'(.*)，.*(.色)')
    for fruit in fruits_match.findall(text):
        print(fruit)
    for fruit_multi_group in fruits_match_multigroup.findall(text):
        print(fruit_multi_group)

### 正则表达式中的字符串切割：re.split()
def RegEx_split ():
    import re
    text = '''关羽；张飞，赵云、马超,黄忠，   马岱\n  魏延，严颜'''
    nameList = re.split(r'[；，、,\s]\s*', text)
    print(nameList)

### 正则表达式中的回掉和替换：
# 替换函数，参数是Match对象
def RegEx_subFunc(match):
    # Match对象的.group(0)返回的是整个匹配到的字符串
    src = match.group(0)

    # Match对象的.group(1)返回的是第一个组的内容
    number_subfunc = int(match.group(1)) + 6
    dest = f'av{number_subfunc}' # 字符串连接

    print(f'{src}替换为{dest}')
    # 返回的值就是最终替换的字符串
    return dest
def RegEx_match_replace():
    links = '''

    下面是这学期要学习的课程：

    <a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
    这节讲的是牛顿第2运动定律

    <a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
    这节讲的是毕达哥拉斯公式

    <a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
    这节讲的是切割磁力线
    '''
    print_str = re.compile(r'/av(\d+?)/')
    print(print_str.findall(links))
    newStr = re.sub(r'av(\d*)', RegEx_subFunc, links)
    print(newStr)


if __name__ == '__main__':
    str_process_salary()
    RegEx_salary()
    RegEx_dot()
    RegEx_star()
    RegEx_curly_brace()
    RegEx_greed_model()
    RegEx_excape()
    RegEx_square_brackets()
    RegEx_not()
    RegEx_start_end_multi()
    RegEx_group_bracket()
    RegEx_split()
    RegEx_match_replace()