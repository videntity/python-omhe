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
 
#print add_hex2('0xff', '0xff')  # 0x1fe


def getFromMeter():
        import serial
        try:
            ser = serial.Serial(SERIAL_PORT, baudrate=2400, parity=serial.PARITY_NONE, bytesize=7,timeout=30)
            print "Waiting for device reading..."
            s = ser.readline()
            if len(s)< 10:
                print "It appears the connection timmed out.  Please start over."
                ser.close()
                exit(1)
            print "Successfully Fetched Data"        
            h=binascii.hexlify(s)
            print h
            ser.flushOutput()
            ser.flushInput()
            ser.flush()
            ser.close()
            return h
        except(serial.serialutil.SerialException):
            print "Something went wrong. Please try unplugging and replugging the USB connection"
            return ""
       
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
    try:
        n= newstring.decode("hex")
    except(TypeError):
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
    #h="g302d63b772302db3330963b45b62b1930962b2934963b1a69bc962b1822e63334d4d9b2e4ded93396b0a"
    h=getFromMeter()
    if len(h)>10:
        r= parse_values(process_string(h))
        print r
    
