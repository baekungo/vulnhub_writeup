import base64,codecs,sys

def decodeString(str):
    s = codecs.decode(str[::-1], 'rot13')
    return base64.b64decode(s)

cryptoResult=decodeString(sys.argv[1])
print (cryptoResult)
