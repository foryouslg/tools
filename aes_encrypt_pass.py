from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

BS = AES.block_size
key = "1234123412ABCDEF"
vi = "ABCDEF1234123412"


def pad(s):
    # 定义 padding 即 填充 为PKCS7
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[0:-ord(s[-1])]

class prpcrypt():
    # def __init__(self,key,vi):
    def __init__(self):
        self.key = key.encode('utf-8')
        self.vi = vi.encode('utf-8')
        # self.key = "1234123412ABCDEF".encode('utf-8')
        # self.vi = "ABCDEF1234123412".encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self,text):
    	""" encrypt text
			text: plaint text
			return: bytes type cipher
    	"""
    	cryptor = AES.new(self.key,self.mode,self.vi)
    	text = pad(text).encode('utf-8')
    	self.ciphertext = cryptor.encrypt(text)

    	return b2a_hex(self.ciphertext)

    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,self.vi)
        plain_text = cryptor.decrypt(a2b_hex(text)).decode('utf-8').rstrip('\0')
        return unpad(plain_text)

if __name__ == '__main__':
    pc = prpcrypt()
    e = pc.encrypt("123456")
    print(e)
    d = pc.decrypt(e)
    print(d)