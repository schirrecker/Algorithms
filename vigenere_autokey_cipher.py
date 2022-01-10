'''
Vigenère:

message: my secret code i want to secure
key:     passwordpasswordpasswordpasswor

Vigenère Autokey:

message: my secret code i want to secure
key:     pa ssword myse c retc od eiwant
'''


class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.long_key = ""
        self.abc = abc

    def init_key(self, text):
        t = self.key + text
        t = "".join(t.split())
        count = 0
        for i in range(0, len(text)):
            if text[i] == " ":
                self.long_key += " "
            else:
                self.long_key += t[count]
                count += 1       

    def encode(self, text):
        self.init_key(text)
        code = ""
        i = 0
        for l in text:
            if 97 <= ord(l) <= 122:
                code += chr(((ord(l)+ord(self.long_key[i])-97*2)%26)+97)
            elif 65 <= ord(l) <= 90:
                code += chr(((ord(l)+ord(self.long_key[i])-65*2)%26)+65)
            else:
                code += l
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
            else:
                code += l
            i += 1
        return code


key = 'password'
abc = 'abcdefghijklmnopqrstuvwxyz'
c = VigenereAutokeyCipher(key, abc)

print (c.encode('codewars'))
print (c.decode('laxxhsj'))
print (c.encode('amazingly few discotheques provide jukeboxes'))
print (c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'))

key2 = 'PASSWORD'
abc2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c2 = VigenereAutokeyCipher(key2, abc2)

print(c2.encode('AAAAAAAAPASSWORDAAAAAAAA'))

