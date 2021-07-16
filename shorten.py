# 1.长链接转换为短链接核心就是进制转换
# 2.十进制数转为62进制( 0~9 + A~Z + a~z )共62个字符
# 3.假如允许转换的10进制数范围为 10 000 000~ 99 999 999 （唯一，相当于数据库主键）每一个数字对应一个长链接，再转为62进制数
# 4.浏览器解析时，现将短链接（62进制数）转换成 10进制数 --- > 再找到对应的长链接，最后解析


# 数字转62进制
def convert(num):
    global all_chars
    all_chars = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz~!@#$%&_-'
    mod = len(all_chars)
    digits = []
    while num > 0:
        # 拿到对应的下标取得mod进制数，并插入列表0号位
        digits.insert(0, all_chars[num % mod])
        num//= mod
    return ''.join(digits)

# 例：12 000 000 转为mod进制数为 oLkO
print(convert(12000000))
