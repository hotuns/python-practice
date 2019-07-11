import re


s = r'([a-z]+) ([a-z]+)'

pattern = re.compile(s, re.I)  # s.I 表示忽略大小写

m = pattern.match('hello world wide web')

# group(0)表示返回匹配成功的整个子串, 参数1表示第一个
print(m.group(0))

# span(0)返回匹配成功的 整个子串快递, 参数1表示第一个
print(m.span(0))

# 所有的子串
print(m.groups())
