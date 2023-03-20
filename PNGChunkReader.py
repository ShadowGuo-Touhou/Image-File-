from CRC32 import CRC32

def readByte(path:str, len:int = 0):
    '''Read len bytes from a file, default to all bytes'''
    with open(path, "rb") as file:
        len = float("inf") if len == 0 else len
        byte = file.read(1)
        byteArray = []
        while(byte and len>0):
            byteArray.append(byte)
            byte = file.read(1)
            len -= 1
        return byteArray

x = readByte(r"C:\Users\203379015\OneDrive - Fulton County Schools\Desktop\CRC32\1x1.png")
#y = readByte(r"C:\Users\203379015\OneDrive - Fulton County Schools\Desktop\CRC32\temp.png")
print(x)


type = b"suTf"
content = b"Hello!"
length = b"\x00\x00\x00\x06"
crc = b"\x51\x22\x39\x61"

with open("temp.png", "ab+") as file:
    for b in x[:48]:
        file.write(b)
    file.write(length)
    file.write(type)
    file.write(content)
    file.write(crc)
    for b in x[48:]:
        file.write(b)