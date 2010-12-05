import serial
import binascii

SERIAL_PORT="/dev/ttyUSB0"


def add_hex2(hex1, hex2):
    """add two hexadecimal string values and return as such"""
    return hex(int(hex1, 16) + int(hex2, 16))
 
    print add_hex2('0xff', '0xff')  # 0x1fe
    
def sub_hex2(hex1, hex2):
    """subtract two hexadecimal string values and return as such"""
    return hex(int(hex1, 16) - int(hex2,16))
 
print add_hex2('0xff', '0xff')  # 0x1fe


def getFromMeter():
        import serial
        ser = serial.Serial(SERIAL_PORT, baudrate=2400, parity=serial.PARITY_SPACE, bytesize=7,timeout=30)
        print "waiting for device reading..."
        s = ser.readline()
        print "Fetched data"        
        h=binascii.hexlify(s)
        process_string(s)
        
       
def process_string(s):
    counter=0
    shift=2
    newstring=""
    while counter<len(s):
        b=s[counter:shift]
        counter=counter+2
        shift=shift+2
        if int(b, 16)>128:
            b= sub_hex2(b, '0x80')
            b=b[2:]
            newstring="%s%s" % (newstring, b)
        else:
            newstring="%s%s" % (newstring, b)
    newstring="%s%s" % (newstring, "0")        
    n= newstring.decode("hex")
    return n

def parse_values(n):
    d={}
    x=n.split(",")
    d['body_type']=x[0]
    d['gender']=x[1]
    d['height_in']=x[2]
    d['weight']=x[3]
    d['impedence']=x[4]
    d['fat_percent']=x[5]
    d['fatmass']=x[6]
    d['freefatmass']=x[7]
    d['tbw']=x[8]
    d['age']=x[9]
    d['bmi']=x[10]
    return d

if __name__ == "__main__":
    s="30acb1acb7302e30acb136b22e30ac35b2b4acb1b72e33acb2b82e30acb133b42e30ac39b82e30ac33b4acb2332eb2acb7b2b7398d0a"
    r= parse_values(process_string(s))
    print r