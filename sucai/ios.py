#coding=UTF-8
import json
import os
filename='ios.txt'
orientation=1
playable_ads_without_video=2

endcard_url='http://interactive.mintegral.com/qa_task/t145/v2/0611tkwg_5033a3-204bf34b63ef9ef14f2957a975f98042.zip?' \
            'md5filename=204bf34b63ef9ef14f2957a975f98042&foldername=0611tkwg_5033a3'


def change_data(filename=filename,endcard_url=endcard_url,orientation=orientation,playable_ads_without_video=playable_ads_without_video):

    f1 = open(filename, 'r+')
    json_str = f1.read()
    dict_data = json.loads(json_str)
    # print(type(dict_data))
    # print(dict_data)
    dict_data['data']['ads'][0]["endcard_url"] =endcard_url
    dict_data['data']['ads'][0]['rv']['orientation']=orientation
    dict_data['data']['ads'][0]['playable_ads_without_video']=playable_ads_without_video
    # print(dict_data)
    end_data=json.dumps(dict_data,ensure_ascii=True,sort_keys=True,indent=4)
    print(end_data)
    with open('newios.txt','w+') as wf:
        wf.write(end_data)

change_data()


