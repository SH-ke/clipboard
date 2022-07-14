import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

class EncodingBash:
    def __init__(self) -> None:
        pass

    def encoding(self) -> str:
        print("Waiting... 读取文件")
        with open("clipboard.priv.txt", 'r', encoding='utf') as f:
            text = ''.join( f.readlines() )

        print(text)
        print("Waiting... 获取密钥")
        key = self.get_stamp()
        print("Waiting... 加密文件")
        cc = CipherCylinder()
        enc = cc.__enc__(text, key)
        print(enc)
        print("Waiting... 保存文件")
        with open("clipboard", 'w') as f:
            f.write(enc)
        
        return enc

    
    def decoding(self) -> str:
        print("Waiting... 读取密文")
        with open("clipboard", 'r', encoding='utf') as f:
            enc = ''.join( f.readlines() )

        print("Waiting... 控制台获取密钥")
        key = input("请输入密钥 Please input passkey: ")
        print("Waiting... 解码")
        cc = CipherCylinder()
        text = cc.__dec__(enc, key*4)
        print("Waiting... 输出明文")
        print(f"{'='*50}\n\n{text}\n\n{'='*50}")

        return text

    
    def board_update(self) -> None:
        text = self.decoding()
        if text == "Error":
            print("更新失败")
            return
        with open("clipboard.priv.txt", 'w', encoding='utf') as f:
            f.write(text)


    def get_stamp(self) -> str:
        print("Waiting... 删除目录下的 stamp_*.priv 文件")
        os.system("del stamp_*.priv")
        print("Waiting... 随机生成6位密钥")
        stamp = str( time.time() )[-4:]
        print(stamp)
        print("Waiting... 保存密钥 stamp_xxxxxx.priv")
        os.system(f"echo $null > stamp_{stamp}.priv")

        return stamp * 4


class CipherCylinder:
    def __init__(self) -> None:
        pass


    # encode: str -> decode -> byte -> pad - > encrypt
    # -> bs64encode -> str utf
    # decode: enc -> decode -> byte -> bs64decode
    # -> decrypt -> unpad -> decode -> str
    def __enc__(self, text: str, stamp: str) -> str:
        iv = "0102030405060708"  # 偏移量

        aes = AES.new(
            key=stamp.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC
        )  # 创建加密器
        bs = aes.encrypt(pad( text.encode(), 16 )) # 加密
        return str(b64encode(bs), "utf-8") # 转化成字符串返回


    def __dec__(self, enc: str, stamp: str) -> str:
        iv = "0102030405060708"  # 偏移量

        aes = AES.new(
            key=stamp.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC
        )  # 创建加密器
        text_byte = aes.decrypt(b64decode( enc.encode() )) # 解密
        # 异常捕获，解密失败
        try:
            text = unpad(text_byte, AES.block_size).decode()
        except UnicodeDecodeError:
            print("密钥错误，解码失败")
            text = "Error"

        return text