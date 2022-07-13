import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

class EncodingBash:
    def __init__(self) -> None:
        pass

    def encoding(self):
        print("Waiting... 读取文件")
        with open("clipboard.priv.txt", 'r', encoding='utf') as f:
            text = ''.join( f.readlines() )

        print(text)
        print("Waiting... 获取密钥")
        self.get_stamp()
        print("Waiting... 加密文件")
        print("Waiting... 保存文件")

    
    def decoding(self):
        print("Waiting... 读取密文")
        print("Waiting... 控制台获取密钥")
        print("Waiting... 解码")
        print("Waiting... 输出明文")


    def get_stamp(self):
        print("Waiting... 删除目录下的 stamp_*.priv 文件")
        os.system("del stamp_*.priv")
        print("Waiting... 随机生成6位密钥")
        stamp = str( time.time() )[-6:]
        print(stamp)
        print("Waiting... 保存密钥 stamp_xxxxxx.priv")
        os.system(f"echo > stamp_{stamp}.priv")


class CipherCylinder:
    def __init__(self) -> None:
        pass


    def __enc__(self, text: str, stamp: str) -> str:
        iv = "0102030405060708"  # 偏移量

        aes = AES.new(
            key=stamp.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC
        )  # 创建加密器
        bs = aes.encrypt(pad( text.encode(), 16 )) # 加密
        return str(b64encode(bs), "utf-8") # 转化成字符串返回


    def __dec__(self, enc: str, stamp: str) -> str:
        pass
