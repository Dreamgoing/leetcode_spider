# coding=utf-8
import os

PATH_BASE = os.path.dirname(os.path.abspath(__file__))

URL_BASE = "https://leetcode.com"

HEADERS_BASE = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'leetcode.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'https://leetcode.com/accounts/login/',
}

LANG_MAPPING = {
    'python': '.py',
    'c++': '.cpp',
    'cpp': '.cpp',
    'golang': '.go',
    'mysql': '.sql',
    'java': 'java'
}
