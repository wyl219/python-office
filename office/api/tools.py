import wftools

from office.lib.decorator_utils.instruction_url import instruction


# from office.core.ToolsType import wftools
# wftools = wftools()

# @except_dec()
@instruction
def transtools(to_lang: str, content: str, from_lang:str='zh'):
    return wftools.transtools(to_lang=to_lang, content=content, from_lang=from_lang)


# @except_dec()
@instruction
def qrcodetools(url: str, output: str = r'./qrcode_img.png'):
    wftools.qrcodetools(url, output)


# @except_dec()
@instruction
def passwordtools(len=8):
    return wftools.passwordtools(len)


# @except_dec()
@instruction
def weather():
    wftools.weather()


# 通过url，获取ip地址
# # @except_dec()
@instruction
def url2ip(url: str) -> str:
    return wftools.url2ip(url)


# 通过url，获取ip地址
# @except_dec()
@instruction
def lottery8ticket():
    wftools.lottery8ticket()


# @except_dec()
@instruction
def create_article(theme, line_num=200):
    wftools.create_article(theme, line_num)


# @except_dec()
@instruction
def pwd4wifi(len_pwd: int = 8, pwd_list=[]):
    wftools.pwd4wifi(len_pwd, pwd_list)


# 测试网速
@instruction
def net_speed_test():
    wftools.net_speed_test()
