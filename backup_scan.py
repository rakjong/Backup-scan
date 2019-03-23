import requests
import sys
import time

def backup_scan():
    if  len(sys.argv) == 1 or sys.argv[1] == '-h':
        print('Usage :')
        print("eg: python3 backup_scan.py http://www.freebuf.com /root/dict.txt /root/result.txt")
        exit()
    domain = sys.argv[1]
    dict_rar_path = sys.argv[2]
    output_file = sys.argv[3]
    try:
        dict_file = open(dict_rar_path, 'r+')
        headers = {
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                   'Accept-Encoding': 'gzip, deflate',
                   'Connection': 'close',
                   'Upgrade-Insecure-Requests': '1'
        }
        result_file = open(output_file, 'a+')
        result_file.write('='*50+'\n')
        result_file.write(time.asctime( time.localtime(time.time()) )+'\n')
        for i in dict_file:
            if i.startswith('/'):
                url = domain + i.strip('\n') # 字符串从字典中获取出来时候是带有 \n 的，直接拼接会出现问题
            else:
                url = domain+'/' + i.strip('\n')
            resp = requests.get(url=url, headers=headers)
            time.sleep(0.5)
            if resp.status_code == 200:
                print('[+]'+url)
                result_file.write(url+'\n')
            else:
            	pass
                #print('[-]'+url)
    except Exception as e:
        print(e)

    result_file.close()
    print("="*(len(output_file)+14))
    print('The Result is %s'%output_file)
    print("="*(len(output_file)+14))

def main():  # 方便以后扩展
    backup_scan() 

if __name__ == '__main__':
    main()
