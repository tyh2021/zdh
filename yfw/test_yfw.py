#coding=utf-8
import  requests
import re
import time
import pytest

h={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Authorization":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlcyI6bnVsbCwicmVzb3VyY2VzIjpbXSwiY2xpZW50X2lkIjoidGVjc3VuX3BjX2NsaWVudCIsImF1ZCI6WyJvcmRlciJdLCJwYXNzd29yZCI6IiQyYSQxMCRabkJDbkY3TmxYOUtNb0VsclNVWUouLm9SRGRxOVhSVTlacmVCR1ovcDZPQlBsNy55ZGFDZSIsInNjb3BlIjpbInJlYWQiXSwib3JnYW5pemF0aW9uIjoiMzk2MzEzNzcwNTIzNDc1OTY4IiwibmFtZSI6IuiwreaciOWNjiIsImlkIjo0NTAwODQ5NTIxNjM1Njk2NjQsInVzZXJUeXBlIjozLCJleHAiOjE2MTU4ODMyODEsImVtYWlsIjoiIiwianRpIjoiYThjOWY4Mzg5YWUwNDE4NzgzYjk5MWQ5N2YzZjBjYTAiLCJ1c2VybmFtZSI6InRhbnl1ZWh1YSJ9.eEoIrOucy52uSgLYOO4FqNhNNV2LXf87SWofAUyQHt4"
    }

class TestClass:
    def get_myId(self):
        p={
        "page":"1",
        "size":"10",
        "type":"",
        "key":"个人就业扶持政策",
        "flag":"true"
        }
        url_searchl="http://192.168.1.252/api/info/api/v2/policy"
        r=requests.get(url=url_searchl,params=p,headers=h)
        mydata=r.json()
        myid=mydata['data']['list'][0]['id']
        return myid;

    def zdh_serch(self):
     p={
     "page":"1",
     "size":"10",
     "type":"",
     "key":"个人就业扶持政策",
     "flag":"true"
     }
     url_searchl="http://192.168.1.252/api/info/api/v2/policy"
     r=requests.get(url=url_searchl,params=p,headers=h)
     mydata=r.json()
     search_len=mydata['data']['total']
     return search_len;

    def test_add(self):
        url_add="http://192.168.1.252/api/info/api/v2/policy"
        body={
        "title":"个人就业扶持政策",
         "content":"<p>个人政策内容</p>",
         "summary":"个人政策测试",
         "tags":"个人就业",
         "areaAddr":[440000,440100,440106],
        "category":1,
         "msgs":["不限"],
         "strings":[-1],
         "area":"天河区",
         "areaCode":440106,
         "city":"广州市",
         "cityCode":440100,
         "province":"广东省",
         "provinceCode":440000
        }
        requests.post(url=url_add,json=body,headers=h)
        s=self.zdh_serch()
        # print(s)
        assert s==1,"新增政策成功，total的值为：%s"%s


    # def test_updata(url):
    #     get_data=test_get_id(url_searchl)
    #     id=str(get_data)
    #     id2=get_data
    #     body={
    #         "title":"个人就业扶持政策",
    #         "content":"<p>"+"内容修改时间："+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"</p>",
    #         "summary":"个人政策测试",
    #         "id":id2,
    #         "tags":"个人就业",
    #         "areaAddr":[440000,440100,440106],
    #         "category":1,"msgs":["不限"],
    #         "strings":[-1],
    #         "province":"广东省",
    #         "provinceCode":440000,
    #         "city":"广州市",
    #         "cityCode":440100,
    #         "area":"天河区",
    #         "areaCode":440106
    #     }
    #     url=url+id
    #     r=requests.put(url=url,json=body,headers=h)
    #     mydata=r.json()
    #     msg=mydata['msg']
    #     assert msg=="处理成功","当前a的值为：%s"%msg
    #     # if msg=="处理成功":
        #     print("编辑成功--用例执行成功")
        # else:
        #     print("编辑失败--用例执行失败")
    #
    def test_delete(self):
        get_id=self.get_myId()
        id=str(get_id)
        url_delete="http://192.168.1.252/api/info/api/v2/policy/"
        url_delete=url_delete+id
        requests.delete(url=url_delete,headers=h)
        s=self.zdh_serch()
        # # print(s)
        assert s==0,"删除政策成功，total的值为：%s"%s




    if __name__ == '__main__':
        pytest.main(["-s","test_yfw.py"])
    # url_searchl="http://192.168.1.252/api/info/api/v2/policy"
    # url_add="http://192.168.1.252/api/info/api/v2/policy"
    # url_update="http://192.168.1.252/api/info/api/v2/policy/"
    # url_delete="http://192.168.1.252/api/info/api/v2/policy/"

    # test_get_id(url_searchl)
    # test_get_total(url_searchl)
    #
    # test_add(url_add)
    # test_updata(url_update)
    # test_delete(url_delete)
