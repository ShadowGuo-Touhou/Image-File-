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

x = readByte(r"1x1.png")

def suTf(content: str):
    byteContent = bytes(f"suTf\n{content}\n", "utf-8")
    length = len(byteContent)-4
    length = bytes([(length>>8*x)&0xff for x in range(3,-1,-1)])
    crc32 = CRC32(byteContent)
    crc32 = bytes([(crc32>>8*x)&0xff for x in range(3,-1,-1)])
    return length+byteContent+crc32

content = suTf("你好陌生人，我顶你个肺!Bye bye!")


with open("temp.png", "ab+") as file:
    for b in x[:33]:
        file.write(b)
    file.write(content)
    for b in x[33:]:
        file.write(b)