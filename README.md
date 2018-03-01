# snufkin_tootbot
スナフキンが名言をMastodonにtootします

【動作確認】<br>
macOS 10.13.3 High Sierra<br>
Python 3.6.4<br>

【下準備】<br>
以下のコマンドで、Mastodon APIをインストールしてください。<br>
pip install Mastodon.py<br>
（うまくいかない場合は、sudo pip3 install Mastodon.pyで）<br>

【セットアップ】<br>
setup.pyに「インスタンス先」「ログインメールアドレス」「パスワード」を書き込み、実行。<br>
python3.6 setup.py<br>

cred.txtとauth.txtが作成されるので、それを既存のものと入れ替える。<br>

【実行】<br>
snufkin_toot.pyの「インスタンス」を編集してから、以下を実行。<br>
python3.6 snufkin_toot.py<br>

これで、tool_list.txtの中の名言をランダムにツゥートする。<br>

【発展】<br>
名言を増やしたい場合は、tool_list.txtに付け加える。その場合、snufkin_toot.pyのramdom関数を編集することを忘れずに。<br>
自動化したい場合はHerokuを使う方法もあり。<br>

【参考】<br>
このプログラムは以下のサイトを参考にしました。ありがとうございます。<br>
[Python]Mastodon botを作ってトゥート!してみた!!<br>
https://routecompass.net/mastodon/#i-3<br>
【Mastodon bot】20%の確率で性器を露出するドラえもん<br>
https://routecompass.net/mastodon-bot/#i-5<br>
