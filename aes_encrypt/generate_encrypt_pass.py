import aes_encrypt_pass
import os

aes = aes_encrypt_pass.prpcrypt()
plain_passwords_file = "plain_pass.txt"
encry_passwords_file = "encry_pass.txt"

def del_encry_pass_file(encry_passwords_file):
    if os.path.exists(encry_passwords_file):
        os.remove(encry_passwords_file)

def read_file(plain_passwords_file):
    with open(plain_passwords_file,'r') as f:
        lines = f.readlines()
        for line in lines:
            temp = str(aes.encrypt(line.rstrip('\n')),'utf-8')
            with open(encry_passwords_file,'a') as w:
                w.write(temp + '\n')


if __name__ == '__main__':
    del_encry_pass_file(encry_passwords_file)
    read_file(plain_passwords_file)
