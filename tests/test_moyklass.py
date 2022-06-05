# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:43:43 2022

@author: zbookuser
"""

from api import MoyKlass
from settings import apiKey


mk = MoyKlass()


def test_get_token_for_apiKey(aKey = apiKey):
    status, results = mk.get_token(aKey)
    assert status == 200
    assert 'accessToken' in results
    
