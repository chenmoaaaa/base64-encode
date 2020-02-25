# edit remark of v2ray's link

import base64
import json

def remark_decode(line):
    line_json = base64.b64decode(line.replace('vmess://','').encode('utf-8')).decode('utf-8')
    return json.loads(line_json)

def remark_change(line,new_remark):
    vmess_json = remark_decode(line)
    print('old_remark:',vmess_json['ps'])
    vmess_json['ps'] = new_remark
    new_link = 'vmess://' + base64.b64encode(json.dumps(vmess_json).encode('utf-8')).decode('utf-8')
    print('new_remark:',remark_decode(new_link)['ps'])
    return new_link

if __name__ == '__main__':

    with open('url.txt','r') as f_input:
        for i,line in enumerate(f_input):
            if(line.startswith('vmess')):
                vmess_json = remark_decode(line)
                print('Line',i,':',vmess_json['ps'])
                new_link = remark_change(line,'new_name')
                print('new name is', remark_decode(new_link)['ps'])
                print('new link is', new_link)
            else:
                print('Line',i,'is not a vmess link')
