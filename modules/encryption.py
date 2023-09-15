import hashlib
import hmac


def encrypt_string(string, secret_key):
    # 将字符串转换为字节类型
    string = string.encode('utf-8')

    # 使用HMAC算法进行加密
    hashed = hmac.new(secret_key.encode('utf-8'), string, hashlib.sha256)

    # 返回加密后的结果
    return hashed.hexdigest()


def decrypt_string(encrypted_string, secret_key):
    # 将加密字符串转换为字节类型
    encrypted_string = encrypted_string.encode('utf-8')

    # 使用HMAC算法进行解密
    decrypted = hmac.new(secret_key.encode('utf-8'), encrypted_string, hashlib.sha256)

    # 比较解密结果与原始字符串
    if decrypted.hexdigest() == encrypted_string.decode('utf-8'):
        # 返回解密后的字符串
        return decrypted.hexdigest()
    else:
        # 解密失败，返回空字符串或其他错误处理
        return "解密失败"

