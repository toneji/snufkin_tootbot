#! /usr/bin/env python
# -*- coding: utf-8 -*-

from mastodon import Mastodon

url = "https://mastodon.com" #インスタンス先
 
Mastodon.create_app("snufkin", #クライアント名
    api_base_url = url,
    to_file = "cred.txt"
    )
 
mastodon = Mastodon(
    client_id="cred.txt",
    api_base_url = url
    )
 
mastodon.log_in(
    "hoge@example.com", #ログインメールアドレス
    "********", #パスワード
    to_file="auth.txt"
    )
