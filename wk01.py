"""
# -*- coding:utf-8 -*- 
  cron: 30 12-23 * * *
  new Env('���A��05'); 
"""
import requests,secrets,time,hashlib,string,random,json,os,sys
import datetime
from lib2to3.pygram import python_grammar_no_print_and_exec_statement
import os
import time
import time
import random
import base64
import requests
import hashlib
import uuid
import json

now = str(round(time.time()*1000))
kami=""
cookies=os.getenv("wk01")
ua = ""



class DY:
    def __init__(self, cookie):
        self.url = cookie.split("#")[0]
        self.cookie = cookie.split("#")[1]
        self.argus = cookie.split("#")[2]
        self.ladon = cookie.split("#")[3]
        

    def run(self):
            
                 jbsl = self.user()
                 jb1 = jbsl
                 print(f"========��ʼ���н���ǩ��========")
                 point_ss , point_s = self.sign()
                 print(f"ǩ���������--{point_s}")
                 print(f"ǩ���������--{point_ss}")
                 ttt = random.randint(25,35)
                 print(f"ǩ����潱�����--��Ϣ{ttt}��")
                 time.sleep(ttt)    
                 pointgg , pointggg = self.task_box(4019)
                 print(f"ǩ����潱�����--{pointgg}")
                 print(f"ǩ����潱�����--{pointggg}")
                 time.sleep(20) 
                 ttt = random.randint(25,35)
                 print(f"ǩ����潱��2���--��Ϣ{ttt}��")
                 time.sleep(ttt)    
                 pointgg , pointggg = self.task_box(4107)
                 print(f"ǩ����潱��2���--{pointgg}")
                 print(f"ǩ����潱��2���--{pointggg}")
                 time.sleep(20) 
                 print(f"========��ʼ���гԷ�����========")
                 self.eat_coin()
                 print(f"========��ʼ������·׬Ǯ========")
                 pointgg , pointggg = self.task_box(4014)
                 print(f"��·׬���--{pointgg}")
                 print(f"��·׬���--{pointggg}")
                 print(f"========��ʼ�����׬���========")
                 pointgg , pointggg = self.task_box(4006)
                 print(f"�����׬���--{pointgg}")
                 print(f"�����׬���--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"�����2׬���--��Ϣ{ttt}��")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(4018)
                 print(f"�����2׬���--{pointgg}")
                 print(f"�����2׬���--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"�����3׬���--��Ϣ{ttt}��")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(3012)
                 print(f"�����3׬���--{pointgg}")
                 print(f"�����3׬���--{pointggg}")
                 print(f"========��ʼ������׬���========")
                 self.treasure_box()
                 pointgg , pointggg = self.task_box(4108)
                 print(f"����������--{pointgg}")
                 print(f"����������--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"���������������--��Ϣ{ttt}��")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(4010)
                 print(f"���������������--{pointgg}")
                 print(f"���������������--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"�������������2���--��Ϣ{ttt}��")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(4010)
                 print(f"�������������2���--{pointgg}")
                 print(f"�������������2���--{pointggg}")
                 time.sleep(20)

                 print(f"========��ʼ�˺Ų��ʲ�========")
            
                 jbsl = self.user()
                 jb2 = jbsl
                 jbzg = jb2 - jb1
                 print(f"========��ʼ����������========")
                 print(f"�������нű�����ý��--{jbzg}")
                 
            
   
           
             
    
    def kami(self):
        url = f"https://api2.2cccc.cc/apiv3/card_login&card={kami}&software=jrttkmo&center_id=17898"
        response = requests.request("GET", url=url)
        kamican = response.json().get('code')
        if kamican == "1":
               kamicans = response.json().get('data').get('less_time')
        else:
            kamicans = response.json().get('msg')
        return kamicans , kamican
    
    def kamidu(self,):
        url = f"https://api2.2cccc.cc/apiv3/config&client_type=card&client_content={kami}&type=read&center_id=17898" 
        response = requests.request("GET", url=url)
        if response.json().get('code') == "1":
               if response.json().get('data').get('config')  == "":
                   kamijqm = "��⵽����ͷ��ʹ�ñ��ű���������ȡ�������ϴ��Ǽ�"
                   kamijqmyz = "��⵽����ͷ��ʹ�ñ��ű���������ȡ�������ϴ��Ǽ�"
               else:
                   kamijqm = "�������ȡ�ɹ���"
                   kamijqmyz = response.json().get('data').get('config')
               return kamijqm , kamijqmyz
        else:
            kamijqm = "��ȡʧ�ܣ�"
            kamijqmyz = "��ȡʧ�ܣ�"
        return kamijqm , kamijqmyz
    
    def kamiwrite(self,md55):
        url = f"https://api2.2cccc.cc/apiv3/config&client_type=card&client_content={kami}&type=write&value={md55}&center_id=17898" 
        response = requests.request("GET", url=url)
        if response.json().get('code') == "1":
            kamijqmm = "�Ǽǳɹ���"
            return kamijqmm
        else:
            kamijqmm = "δ֪����"
            return kamijqmm

    def get_mac_address(self):
      mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
      print("��ȡ������ɹ���")
      return ":".join([mac[e:e+2] for e in range(0,11,2)])


    def user(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/sj/v1/income/page_data?_request_from=web&{self.url}"
        headers = {
            'User-Agent': ua,
            'x-argus': self.argus,
            'x-ladon': self.ladon,
            'Cookie': self.cookie,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("err_no") == 0:
                jbjj = response_json.get('data').get('score_balance') / 33000
                jbj = round(jbjj, 2)
                print(f"���ս�ң�{response_json.get('data').get('today_score_amount')}��� �ֽ�{jbj} Ԫ")
                jbsl = response_json.get('data').get('score_balance')
            else:
                print(f"��ȡ�û���Ϣ����{response_json}")
                jbsl = 0
        else:
            print("�û����ݹ��ڻ��ߴ���")
            jbsl = 0
        return jbsl
    
    def sign(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/news/v1/sign_in/done_task?{self.url}"
        payload = '{}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': 'com.ss.android.article.news/9360 (Linux; U; Android 13; zh_CN; V2055A; Build/TP1A.220624.014; Cronet/TTNetVersion:85102f3e 2023-06-05 QuicVersion:4ad3af5d 2023-05-09)',
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_s = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                point_ss = response.json().get('data').get('reward_amount')
                return point_s , point_ss
            else:
                point_ss = "�Ѿ�������"
                return point_s  , point_ss
            
    def eat_coin(self):
        current_hour = time.localtime().tm_hour
        if (5 <= current_hour <= 9) or (11 <= current_hour <= 14) or (17 <= current_hour <= 20) or (21 <= current_hour <= 24):
            url = f"https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/eat/done?{self.url}"
            body = "{}"
            headers = {
                'User-Agent': ua,
                'x-argus': self.argus,
                'x-ladon': self.ladon,
                'Cookie': self.cookie,
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Connection': 'keep-alive'
            }
            response = requests.post(url, headers=headers, data=body)
            if response.status_code == 200:
                response_json = response.json()
                if response_json.get("err_no") == 0:
                    score_amount = response_json.get('data').get('score_amount')
                    pointgg , pointggg = self.task_box(4011)
                    print(f"�Է�׬Ǯ�����--{pointgg}")
                    print(f"�Է�׬Ǯ�����--{pointggg}")
                    return True
                else:
                    print(f"[�Է�׬Ǯ]ʧ�ܣ���ʱ�������ȡ")
                    return True
            else:
                print(f"����ʧ��")
            return False
        else:
            print(f"[�Է�׬Ǯ]ʧ�ܣ�����ʱ�����")
        return False            

            
        
            
    def task_box(self,id):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = {"amount":691,"weight":0,"task_id":id,"is_post_login":False,"ad_from":"coin","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":False,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}
        payload = json.dumps(payload)
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_ssp = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                point_sp = response.json().get('data').get('reward_amount')
                return point_ssp , point_sp
            else:
                point_sp = "�Ѿ�������"
                return point_ssp  , point_sp   

    def treasure_box(self):
        url = f"https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/treasure_box/detail?{self.url}"
        headers = {
            'User-Agent': ua,
            'x-argus': self.argus,
            'x-ladon': self.ladon,
            'Cookie': self.cookie,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("err_no") == 0 and response_json.get('data').get('left_seconds') != 0:
                print(f"[��������]ʧ�ܣ�����{response_json.get('data').get('left_seconds')}��")
                return True
            else:
                url = f"https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/treasure_box/done?{self.url}"
                body = "{\"auto_open\":false}"
                headers = {
                    'User-Agent': ua,
                    'x-argus': self.argus,
                    'x-ladon': self.ladon,
                    'Cookie': self.cookie,
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
                }
                response = requests.post(url, headers=headers, data=body)
                if response.status_code == 200:
                    response_json = response.json()
                    print(f"[��������]��ý��: {response_json.get('data').get('reward_amount')}")
                    return True
                else:
                    print(f"����ʧ��")
                    return False
        else:
            print(f"����ʧ��")
        return False


    def xs_sign(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/novel_sdk/v1/task/done/sign_in?{self.url}"
        payload = '{}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        pointxss = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                pointxxss = response.json().get('data').get('amount')
                return pointxss , pointxxss
            else:
                pointxxss = "�Ѿ�������"
                return pointxss , pointxxss  

    def eat(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/news/v1/eat/done_eat?_request_from=web&{self.url}"
        payload = '{}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_cf = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                point_cff = response.json().get('data').get('score_amount')
                return point_cf , point_cff
            else:
                point_cff = "�Ѿ�������"
                return point_cf  , point_cff  
            

            
    def get_step(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":190,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent':ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        pointstep = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                pointstepp = response.json().get('data').get('reward_amount')
                return pointstep , pointstepp
            else:
                pointstepp = "�Ѿ�������"
                return pointstep , pointstepp




    def eat_sp(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":181,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_cfs = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                point_cffs = response.json().get('data').get('reward_amount')
                return point_cfs , point_cffs
            else:
                point_cffs = "�Ѿ�������"
                return point_cfs  , point_cffs  
            
    def read(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/news/v1/activity/done_whole_scene_task?{self.url}"
        payload = '{"group_id": "","scene_key": "IndexTabFeed","is_golden_egg": false}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_read = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                point_readd = response.json().get('data').get('score_amount')
                return point_readd , point_read
            else:
                point_readd = "�Ѿ�������"
                return point_readd , point_read
            
    def kgg(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":210,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent':ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        pointgg = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                pointggg = response.json().get('data').get('reward_amount')
                return pointgg , pointggg
            else:
                pointggg = "�Ѿ�������"
                return pointgg , pointggg 
             
    def open_box(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":188,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point2 = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "�ɹ�":
                point = response.json().get('data').get('reward_amount')
                return point2 , point
            else:
                point = "�Ѿ�������"
                return point2 , point
        
    def open_boxlx(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = "{\"task_id\":225,\"exci_extra\":{\"cid\":1770200687669342,\"req_id\":\"20230701160644C93FF92F37A3A1714A5C\",\"rit\":80047},\"extra\":{\"stage_score_amount\":[],\"track_id\":\"\",\"draw_score_amount\":null,\"draw_track_id\":null,\"task_id\":\"\",\"task_name\":\"\",\"enable_fuzzy_amount\":false,\"custom_id\":null}}"
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point4 = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_no") == 0:
                point3 = response.json().get('data').get('reward_amount')
                return point4,point3
            else:
                point3 = "�Ѿ�������"
                return point4,point3

    

if __name__ == "__main__":
    cookies = cookies.split("@")
    print(f"����������������⵽{len(cookies)}���˺�")
    print(f"==========================================")
    print(f"��������")
    i = 1
    for cookie in cookies:
        print(f"========���˺�{i}����ʼ���нű�========")
        i += 1
        DY(cookie).run()
        
        time.sleep(random.randint(5, 10))
        if i > len(cookies):
            break
        else:
            print("�ӳ�һС��,׼������һ���˺�")