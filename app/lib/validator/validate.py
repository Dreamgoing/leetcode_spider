# coding=utf-8


class IDCardNumberValidator(object):
    ''' dddddd：地区码
        yyyymmdd: 出生年月日
        xxx:顺序类编码，无法确定，奇数为男，偶数为女
        y: 校验码，该位数值可通过前17位计算获得
        18位号码加权因子为(从右到左) Wi = [ 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2,1 ]
        验证位 Y = [ 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2 ]
        校验位计算公式：Y_P = mod( ∑(Ai×Wi),11 )
        i为身份证号码从右往左数的 2...18 位; Y_P为脚丫校验码所在校验码数组位置
    '''

    chmap = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'x': 10,
        'X': 10
    }

    def ch_to_num(self, ch):
        return self.chmap[ch]

    def verify_list(self, l):
        sum_result = 0
        for ii, n in enumerate(l):
            i = 18 - ii
            weight = 2 ** (i - 1) % 11
            sum_result = (sum_result + n * weight) % 11
        return sum_result == 1

    def __call__(self, value):
        if len(value) != 18:
            return False
        char_list = list(value)
        num_list = [self.ch_to_num(ch) for ch in char_list]
        return self.verify_list(num_list)
