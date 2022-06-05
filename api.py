# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:46:49 2022

@author: zbookuser
"""

import requests


class MoyKlass:
    def __init__(self):
        self.base_url = "https://api.moyklass.com/"
        
    
    def get_token(self, apiKey):
        '''Авторизация. Получение токена для работы с API'''
        
        data = {
            'apiKey': apiKey
            
        }
        
        res = requests.post(self.base_url + 'v1/company/auth/getToken', data = data)
        status = res.status_code
       
        results = ""
       
        try: 
            results = res.json()
        except:
            results = res.text
        
        return status, results
    
    
    
    def get_list_manager(self, token):
        '''Возвращает список сотрудников'''
        
        headers = {
            'x-access-token': token
        }
        
        res = requests.get(self.base_url + 'v1/company/managers', headers = headers)
        status = res.status_code
       
        results = ""
       
        try: 
            results = res.json()
        except:
            results = res.text
        
        return status, results
    
    
    
    def create_new_manager(self, token: str, name: str, phone: str):
        '''Создает нового сотрудника'''
        
        headers = {
            'x-access-token': token
        }
        
        data = {
            'name': name
            'phone': phone
            'filials': [0]
            'roles': [2]
        }
        res = requests.post(self.base_url + 'v1/company/managers', headers = headers, data = data)
        status = res.status_code
           
         results = ""
        
         try: 
             results = res.json()
         except:
             results = res.text
         
         return status, results  
       