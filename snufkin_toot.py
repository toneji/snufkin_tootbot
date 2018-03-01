#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import random
import linecache
from mastodon import Mastodon
 
#toot準備
mastodon = Mastodon(
        client_id="cred.txt", 
        access_token="auth.txt",
        api_base_url = "https://mastodon.com") #インスタンス
 
#1〜49の乱数生成
rand = random.randint(1,49)
 
#変数に名言を代入
target_line = linecache.getline('tool_list.txt', rand)
 
#キャッシュをクリア
linecache.clearcache() 
 
#toot
mastodon.toot(target_line)
