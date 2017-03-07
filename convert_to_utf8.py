#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
import chardet

'''
 将知道文件夹下的c文件转化为unix 格式的utf-8 编码
'''
mydir=r'D:\github\libgo\libgo'
if len(sys.argv)==2:
    mydir=sys.argv[1]
    
def get_charset(s):
    f=open(path,'rb')
    data=f.read()
    ret=chardet.detect(data)
    f.close()
    return ret['encoding']
    
def dos2unix(file_name):
    print(file_name)
    f=open(file_name,'rb')
    lines=f.read()

    ar=bytearray(lines)
    ar=ar.replace(b'\r\n',b'\n')
    f.close()
    f=open(file_name,'wb')
    f.write(ar)
    f.close()
  
def change_tab_to_space(file_name):
    f=open(file_name)
    lines=f.readlines()
    results=[]
    for s in lines:
        if '\t' in s:
            n=s.replace('\t','    ')
            results.append(n)
        else:
            results.append(s)
    f.close()
    f=open(file_name,'w')
    for l in results:
        f.writelines(l)
    f.close()
  
def change_file_charset(file_name, charset='UTF-8-SIG'):
    if os.path.isfile(file_name)==False:
        return
    ext=os.path.splitext(file_name)[1]
    if ext not in ['.cpp','.h','.hpp']:
        return
    old_charset=get_charset(file_name)
    if old_charset==charset:
        return
    print (file_name,old_charset)  
    
    f = open(file_name,'rb')
    s = f.read()
    #print(s)
    f.close()

    
    u = s.decode(old_charset)
    f = open(file_name, 'wb')
    s = u.encode(charset)
    f.write(s)
    f.close()

    

if __name__=='__main__':

    for r,d,f in os.walk(mydir):
        for p in f:
            path=os.path.join(r,p)
            #ret=get_charset(path)
            #print(path,ret)
            dos2unix(path)
            change_file_charset(path)