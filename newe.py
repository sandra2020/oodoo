import os
a=os.listdir('f:/cc')
print(a)
for i in a:
    b=os.listdir('f:/cc/'+i)
    # print(b)
    for i_1 in b:
        # if i_1[0:15]=='感冒清@sis001.com@':
        #     print('f:/cc/'+i+'/'+i_1[15:])
        #     os.rename('f:/cc/'+i+'/'+i_1,'f:/cc/'+i+'/'+i_1[15:])
        if i_1[0:9]=='[ThZu.Cc]':
            print('f:/cc/'+i+'/'+i_1[9:])
            os.rename('f:/cc/'+i+'/'+i_1,'f:/cc/'+i+'/'+i_1[9:])
# a=os.walk('f:/cc/0912')
# for path,dir,name in a :
#     for i in name:
#         print(i)