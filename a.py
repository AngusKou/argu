import argparse
import datetime


def _warning(verbose, message):
    if verbose >= 0:
        print(datetime.datetime.now().strftime('%d/%m %H:%M:%S') + '|WARNG|', message)


def _info(verbose, message):
    if verbose >= 1:
        print(datetime.datetime.now().strftime('%d/%m %H:%M:%S') + '|INFO |', message)


def _debug(verbose, message):
    if verbose >= 2:
        print(datetime.datetime.now().strftime('%d/%m %H:%M:%S') + '|DEBUG|', message)


parser = argparse.ArgumentParser(description='this is test description')

parser.add_argument('path', help='path to test')
parser.add_argument('--age', type=int, default=10, help='age of the tester')
parser.add_argument('-v', '--verbose', help='show detail of the data: v=INFO,vv=DEBUG', action='count', default=0)


args = parser.parse_args()
v = args.verbose
_info(v, 'args.path='+args.path)
_info(v, 'args.age='+str(args.age))

_info(v, 'this is normal info')
_debug(v, 'this is debug message')

print('this is result')
_warning(v, 'this is a warning')

# summary
# 没有减号的都是必须指定值的参数，无法有默认值
# 可选参数一般都有默认值
# 默认情况下，参数都是字符串，所以要制定type=int来更改数据类型
# action=count很有用，可以指定logging级别 -v,-vv
