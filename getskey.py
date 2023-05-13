import base58
byte_array = base58.b58decode("2w6f5AxJ2yJ21QPFLEaVZBoCSvRDBa3fBYX5121r41bRZbMgAB8Fcokyw8kw6f2cTyoqUZs4rGrerSQ88q3U8FWb")
json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"
print(json_string)

main_publickey="idkhelpig"

f=open(str(main_publickey)+".json","w")
f.write(json_string)
f.close