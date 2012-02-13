import serial, omhe.core
import binascii, sys
from omhe.core.parseomhe import parseomhe
from omhe.core import upload2restcat

RESTCAT_SERVER="http://restcat.physique7.com:80"
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
                print "It appears the connection timed out.  Please start over."
                ser.close()
                exit(1)
            print "Successfully Fetched Data! How awesome!"        
            h=binascii.hexlify(s)
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
    #h="302c312c37302e302c3136332e382c3437352c31362e302c32362e322c3133372e362c3130302e382c33352c32332e352c373239380d0a"
    h=getFromMeter()
    if len(h)>10:
        r= parse_values(process_string(h))
        #print r
        
        email= raw_input("Please enter the user's email address: ")
        pin = raw_input("Please enter the user's PIN or PASSWORD: ")
        
        #upload the weight
        try:
            """ Instantaiate an instance of the OMHE class"""
            o = parseomhe()
            """Parse it if valid, otherwise raise the appropriate error"""
            try:
                omhe_str="wt=%s#tanita_body_scan" % (r['weight'])
                d=o.parse(omhe_str)
                """Send the OMHE dictionary to RESTCat"""
            except():
                print "Failed to parse OMHE string"
                sys.exit(1)
            
            userpass="%s:%s" % (email, pin)
            sender=email
            receiver=email
            subject=email
            restcat_server=RESTCAT_SERVER
            out_file="out.json"
            result=upload2restcat.upload2restcat(d, userpass, sender, receiver,
                                                 subject, restcat_server,
                                                 out_file, idr=None)
            httpcode=result.getinfo(result.HTTP_CODE)
            #print "HTTP Response Code=%s" % (result.getinfo(result.HTTP_CODE),)
            result.close()
            if int(httpcode)==200:
                print "Successfully uploaded weight"
            else:
                print "Weight Upload failed. Error code %s" % (httpcode)
        except():
            print "An unexpected error occurred. Here is the post-mortem:"
            print sys.exc_info()
            
        #upload the fat mass
        try:
            """ Instantaiate an instance of the OMHE class"""
            o = parseomhe()
            """Parse it if valid, otherwise raise the appropriate error"""
            try:
                omhe_str="fm=%s#tanita_body_scan" % (r['fatmass'])
                d=o.parse(omhe_str)
                """Send the OMHE dictonary to RESTCat"""
            except():
                print "Failed to parse OMHE string"
                sys.exit(1)
            
            userpass="%s:%s" % (email, pin)
            sender=email
            receiver=email
            subject=email
            restcat_server=RESTCAT_SERVER
            out_file="out.json"
            result=upload2restcat.upload2restcat(d, userpass, sender, receiver,
                                                 subject, restcat_server,
                                                 out_file, idr=None)
            httpcode=result.getinfo(result.HTTP_CODE)
            #print "HTTP Response Code=%s" % (result.getinfo(result.HTTP_CODE),)
            result.close()
            if int(httpcode)==200:
                print "Successfully uploaded fat mass"
            else:
                print "Fatmass Upload failed. Error code %s" % (httpcode)
        except():
            print "An unexpected error occurred. Here is the post-mortem:"
            print sys.exc_info()