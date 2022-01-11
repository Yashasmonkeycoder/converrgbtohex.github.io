set = input("enter color").strip()
code = "HEX"
for x in set:
  if x == ',':
    code = "RGB"
conv = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g"}
def toHEX():
  try:
    val = set.split(",")
    t1 = str(float(val[0])/16).split(".")
    v1 = conv[int(t1[0])]
    v2 = conv[int(float("0."+t1[1])*16)]
    t2 = str(float(val[1])/16).split(".")
    v3 = conv[int(t2[0])]
    v4 = conv[int(float("0."+t2[1])*16)]
    t3 = str(float(val[2])/16).split(".")
    v5 = conv[int(t3[0])]
    v6 = conv[int(float("0."+t3[1])*16)]
    print("HEX value: #",v1,v2,v3,v4,v5,v6)
  except:
    print("Something is not correct, check again ex of rgb code: 200,20,60")
def toRGB():
  try:
    conv2 = {str(v): k for k, v in conv.items()}
    h1 = []
    for bb in set:
      h1.append(bb)
    n1 = (int(conv2[h1[0]])*16)+(int(conv2[h1[1]]))
    n2 = (int(conv2[h1[2]])*16)+(int(conv2[h1[3]]))
    n3 = (int(conv2[h1[4]])*16)+(int(conv2[h1[5]]))
    print("RGB value: rgb(",n1,",",n2,",",n3,")")
  except:
    print("something is not correct, please enter in small letters and try. error:HEX") 
if code == "RGB":
  exec("toHEX()")
elif code == "HEX":
  exec("toRGB()")
else:
  print("oh no! something went wrong")
#made by chota dimag yashas