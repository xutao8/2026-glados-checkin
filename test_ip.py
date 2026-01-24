#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试IP对签到结果的影响"""

import requests

COOKIE = 'koa:sess=eyJ1c2VySWQiOjYzNjgyMCwiX2V4cGlyZSI6MTc5NTAxMzA5NzY2MCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=w1budvt9D3wj-Ujqs3mc7CkCvik'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': COOKIE,
    'Origin': 'https://glados.cloud',
    'Referer': 'https://glados.cloud/console/checkin',
}

print('=' * 60)
print('IP 与签到关系测试')
print('=' * 60)

# 测试1：通过代理
print('\n📡 测试1：通过代理 (127.0.0.1:7890)')
try:
    proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
    my_ip = requests.get('https://api.ipify.org', timeout=5, proxies=proxies).text
    print(f'   出口IP: {my_ip}')
    
    resp = requests.post('https://glados.cloud/api/user/checkin', 
                         headers=headers, 
                         json={'token': 'glados.cloud'}, 
                         timeout=15,
                         proxies=proxies)
    result = resp.json()
    print(f'   签到结果: {result.get("message", "无")}')
except Exception as e:
    print(f'   错误: {e}')

# 测试2：直连（无代理）
print('\n📡 测试2：直连（无代理，模拟 GitHub Actions）')
try:
    my_ip = requests.get('https://api.ipify.org', timeout=5).text
    print(f'   出口IP: {my_ip}')
    
    resp = requests.post('https://glados.cloud/api/user/checkin', 
                         headers=headers, 
                         json={'token': 'glados.cloud'}, 
                         timeout=15)
    result = resp.json()
    print(f'   签到结果: {result.get("message", "无")}')
except Exception as e:
    print(f'   错误: {e}')

print('\n' + '=' * 60)
