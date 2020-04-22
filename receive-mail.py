

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def receive_mail():
    # 输入邮件地址，密码和pop3地址
    email = input('Email:')
    password = input('password is:')
    pop3_server = input('Pop3 server is:')

   # 连接到pop3服务器
    server = poplib.POP3(pop3_server)

    # 可以打开或者关闭调试信息
    server.set_debuglevel(1)

    # 可选：输出pop3服务期的欢迎文字
    print(server.getwelcome().decode('utf-8'))

    #身份认证
    server.user(email)
    server.pass_(password)

    # list（）返回所有邮件的编号
    resp, mails, octets = server.list()

    # 可以查看返回的列表，
    print(mails)

    # 获取最新一封邮件，注意索引号从1开始
    index = len(mails)
    resp, lines, octets = server.retr(index)

    # lines存储了邮件原始文本的每一行
    # 可以获得整个邮件的原始文本
    msg_content = b'\r\n'.join(lines).decode('utf-8')

    # 稍后解析邮件
    msg = Parser().parsestr(msg_content)

'''
这个Message对象可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，
嵌套可能还不止一层,我们要递归地输出Message对象的层次结构
'''
# indent用于缩进显示
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s<%s>' % (name, addr)
            print('%s%s:%s' % (' ' * indent,header,value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s-------------' % (' ' * indent))
            print_info(part,indent + 1)
    else::
    content_tytpe = msg.get_content_type()
    if content_tytpe == 'text/plain' or content_tytpe == 'text/html':
        content = msg.get_payload(decode=True)
        charset = guess_charset(msg)
        if charset:
            content = content.decode(charset)
        print('%sText: %s' % (' ' * indent, content + '...'))
    else:
        print('%sAttachment: %s' % (' ' * indent,content_tytpe))

# 邮件的Subject或Email中包含的名字都是经过编码的str，要正常显示必须进行解码，代码如下：
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

'''
decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以会解析出多个元素。编写上面的代码时偷懒了，只取了第一个元素。
文本邮件的内容也是str，还需要检测编码，否则非UTF-8编码的邮件都无法正常显示，代码如下：
'''
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# 可以根据邮件索引号直接从服务期删除邮件
server.dele(index)

# 关闭连接
server.quit()
