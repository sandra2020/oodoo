import os,shutil
# a=os.listdir('f:/cc/0912')
# head='老肥@第一会所@'
# h_len=len(head)
# print(h_len)
# for i in a:
#     if i[0:h_len]==head:
#         print('f:/cc/0912/'+i[h_len:])
#         os.rename('f:/cc/0912/'+i,'f:/cc/0912/'+i[h_len:])

# [ThZu.Cc]兔子先生TZ-070-AV2夏日性爱运动会终极惩罚
# os.rename('f:/cc/0912/[ThZu.Cc]兔子先生TZ-070-AV2夏日性爱运动会终极惩罚','f:/cc/0912/兔子先生TZ-070-AV2夏日性爱运动会终极惩罚')
#
a=os.walk('d:/')
list_d=[]
for path,file,name in a:
    for i in name:
        if i[0:9]=='[ThZu.Cc]':
            print(path+'/'+i,path+'/'+i[9:])
            os.rename(path+'/'+i,path+'/'+i[9:])
        #
        # if i in ['uur9 3.com.mp4','聚 合 全 網 H 直 播.html','社 區 最 新 情 報.mp4','最 新 位 址 獲 取.txt','x u u 6 2 . c o m.mp4','thzkk.com.url','桃花族地址发布器.chm','u u r 9 3.c om.mp4','與sis001保持聯絡的終極秘笈 2018年5月27日更新.TXT','第一会所 宣传图.jpg','SIS001影视联盟.gif','第一会所-综合社区.url','感冒清@www.sis001.com.url','論壇開放註冊，更多精彩，歡迎關注！.txt']or i[-8:]=='.torrent':
        #     list_d.append(path+'/'+i)
# print(list_d)
# num=0
# for i_d in list_d:
#     num=num+1
#     print(i_d)
#     os.remove(i_d)
# print(num)


# a=os.walk('f:/cc')
# for path,dir,name in a :
#     for i in name:
#         if i[-4:]!='.jpg':
#             print(i)