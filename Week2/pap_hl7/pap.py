from hl7apy.core import Message

m = Message("ADT_A01")
m2 = Message()
m3 = Message("ORU_R01")

for each in m3:
    print(each)
    
