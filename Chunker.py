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

x = readByte(input("Enter the path of Image: "))

def suTf(content: str):
    byteContent = bytes(f"suTf\n\n{content}\n\n", "gbk")
    length = len(byteContent)-4
    length = bytes([(length>>8*x)&0xff for x in range(3,-1,-1)])
    crc32 = CRC32(byteContent)
    crc32 = bytes([(crc32>>8*x)&0xff for x in range(3,-1,-1)])
    return length+byteContent+crc32

content = suTf(input("Enter the content you want to write: "))


with open("temp.png", "ab+") as file:
    for b in x[:33]:
        file.write(b)
    file.write(content)
    for b in x[33:]:
        file.write(b)