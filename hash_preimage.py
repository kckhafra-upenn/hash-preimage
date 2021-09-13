import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'
    x = os.urandom(64)
    scale=16
    length = len(target_string)
    xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:]
    match=False
    newLen=len(xBitsTotal)-length
    while(match==False):
        xLastKbits=xBitsTotal[newLen:len(xBitsTotal)]

        if(target_string==xLastKbits):
            match=True
        else:
            x = os.urandom(64)
            xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:]
    return(x)

# hash_preimage("01011100")