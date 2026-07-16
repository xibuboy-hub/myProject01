import json

from django.conf import settings
import hashlib
import base64
from Crypto.Cipher import AES

secret_key = 'aswycbdjddjdueekejhb'


def md5(data_string):
    obj = hashlib.md5(secret_key.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


class aes_decrypt:

    def unpad(self, data):
        """
        移除数据末尾的填充字符
            1. 获取数据的最后一个字符。
            2. 判断该字符是否为整数类型，如果是整数则直接使用，否则将其转换为 ASCII 值。
            3. 根据该值从数据末尾向前截取相应长度的数据并返回。
        :param data:
        :return:
        """
        return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]

    def bytes_to_key(self, data, salt, output=48):
        """
        将字节数据和盐值转换为指定长度的密钥。
        参数:
        data (str): 输入的数据，将被转换为字节。
        salt (bytes): 8字节的盐值，用于增加安全性。
        output (int): 输出密钥的期望长度，默认为48字节。

        返回:
        bytes: 生成的密钥，长度为output参数指定的长度。
        """
        # 将输入数据编码为UTF-8字节序列
        data = data.encode(encoding='utf-8')
        # 确保盐值长度为8字节，否则抛出异常
        assert len(salt) == 8, len(salt)
        # 将盐值追加到数据后面
        data += salt
        # 使用MD5算法生成初始密钥
        key = hashlib.md5(data).digest()
        final_key = key
        # 如果当前密钥长度小于所需输出长度，则进行循环以扩展密钥长度
        while len(final_key) < output:
            # 使用上一次的密钥和原始数据生成新的密钥
            key = hashlib.md5(key + data).digest()
            final_key += key
        # 返回指定长度的密钥
        return final_key[:output]

    def decrypt(self, encrypted, key):
        """
        使用给定的密钥短语解密加密数据。

        加密数据首先从Base64编码解码为二进制数据。然后验证其格式是否以'Salted__'开头，
        这是为了确认数据是按照OpenSSL标准加密的。接着，从加密数据中提取盐值，并使用该盐值
        和密钥短语派生出加密密钥和初始化向量（IV）。使用派生的密钥和IV，通过AES加密器
        解密剩余的加密数据，并在最后移除填充以恢复原始的未加密数据。

        :param encrypted: Base64编码的加密数据字符串。
        :param passphrase: 用于解密数据的密钥短语字符串。
        :return: 解密后的原始数据。
        """
        # 将Base64编码的加密数据转换为二进制数据
        encrypted = base64.b64decode(encrypted)
        # 验证加密数据的格式是否正确（以'Salted__'开头）
        assert encrypted[0:8] == b"Salted__"
        # 从加密数据中提取盐值
        salt = encrypted[8:16]
        # print(f"salt hex(): {salt.hex()}")
        # 使用密钥短语和盐值派生加密密钥和初始化向量（IV）
        key_iv = self.bytes_to_key(key, salt, 32 + 16)
        # print(f"key_iv hex(): {key_iv.hex()}")

        # 从派生的密钥和IV中分离出加密密钥
        key = key_iv[:32]
        # print(f"key hex(): {key.hex()}")

        # 从派生的密钥和IV中分离出初始化向量（IV）
        iv = key_iv[32:]
        # 使用十六进制编码将 bytes 数组转换为字符串
        # print(f"iv hex(): {iv.hex()}")
        # 使用派生的密钥和IV创建AES加密器
        aes = AES.new(key, AES.MODE_CBC, iv)
        # 使用AES加密器解密数据，并移除填充以恢复原始数据
        return self.unpad(aes.decrypt(encrypted[16:]))


if __name__ == '__main__':
    aes1 = aes_decrypt()
    key = 'qazwsxedcrfvtgby'
    encrypt_str='U2FsdGVkX19uLibTFEUUrBSMGI216QqtSnaeVbGD8CE+Xll4w2DSJfCaI2ceGDRhrtWbr8XGvjuDB/n+f46bJg=='
    obj = json.loads(aes1.decrypt(encrypted=encrypt_str, key=key).decode())
    print(obj)
