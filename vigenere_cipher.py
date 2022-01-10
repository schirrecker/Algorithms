class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        self.long_key = str(self.key)
        self.init_key()
        
    def init_key(self):
        if len(self.key) < len(self.abc):
            for i in range(len(self.key), len(self.abc)):
                self.long_key += self.key[i % len(self.key)]
        
    def encode(self, text):
        code = ""
        i = 0
        for l in text:
            if 97 <= ord(l) <= 122:
                code += chr(((ord(l)+ord(self.long_key[i])-97*2)%26)+97)
            elif 65 <= ord(l) <= 90:
                code += chr(((ord(l)+ord(self.long_key[i])-65*2)%26)+65)
            i += 1
        return code
        
    def decode(self, text):
        code = ""
        i = 0
        for l in text:
            if 97 <= ord(l) <= 122:
                code += chr(((ord(l)-ord(self.long_key[i]))%26)+97)
            elif 65 <= ord(l) <= 90:
                code += chr(((ord(l)-ord(self.long_key[i]))%26)+65)
            i += 1
        return code


key = 'password'
abc = 'abcdefghijklmnopqrstuvwxyz'
c = VigenereAutokeyCipher(key, abc)

print (c.long_key)
print (c.encode('codewars'))
print (c.decode('laxxhsj'))

key2 = 'PASSWORD'
abc2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c2 = VigenereAutokeyCipher(key2, abc2)

print(c2.encode('AAAAAAAAPASSWORDAAAAAAAA'))
