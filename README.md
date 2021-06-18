# tetris_game_tutorial

[tetris_game](https://github.com/seigot/tetris_game)プログラミング用のチュートリアルです。<br>
このチュートリアルを理解すれば[tetris_gameのブロック操作用サンプルプログラム(block_controller_sample.py)](https://github.com/seigot/tetris_game/blob/master/doc/files/block_controller_sample.md)が読めるようになることを目指しています。<br>
<br>
プルリクエスト募集中です。<br>
<br>

## まず動かしてみる
[tetris_game](https://github.com/seigot/tetris_game)の「実行環境準備」を参照して、まず動かしてみる。<br>
困った時は[FAQ](https://github.com/seigot/tetris_game/blob/master/doc/files/FAQ.md)など参照。

## Githubリポジトリfork
[tetris_game](https://github.com/seigot/tetris_game)の「コード作成のはじめかた」を参照してforkする。<br>

## エディタ

世の中には色々なエディタがありますが、最終的には自分の好みで選択するのがよさそうです。<br>

|  エディタ名  |  特徴  |  備考  |
| ---- | ---- | ---- |
|  vi  |  -  |  -  |
|  emacs  |  -  |  -  |
|  gedit  |  -  |  -  |
|  vscode  |  Microsoftのエディタ、機能まぁまぁ、グラフィカルで操作はわかりやすい、ただ重い  |  -  |
|  spyder  |  pythonの統合開発環境（エディタ進化版）、デバッグとかしやすい、ただ重い  |  -  |
|  nano  |  vimよりマシな操作感、軽い、ただ結局コマンドを覚えないと保存すらできない  |  -  |
|  vim  |  とりあえず感覚的に操作できないからハードル高い、ただ覚えれば効率は一番いいかも  |  -  |
|  その他  |  -  |  -  |

#### 参考リンク<br>
更新するかも

## コマンド

ターミナルから使うコマンドです。<br>
今回は最低限以下を使えれば問題ないはず。<br>

```
cd     : ディレクトリの移動。change directoryの略
ls     : 現在のディレクトリのファイルを表示。listの略
rm     : ファイルを削除。removeの略
rm  -r : ディレクトリを削除。
```

#### 参考リンク<br>
[ターミナルのよく使うコマンド](https://qiita.com/ryo2132/items/b7e312b0eb50fc449841)

## git 
gitはソフトウェアのバージョン管理システムです。<br>
github上での`tetris_game`用ソースコード管理をコマンドラインから操作することが可能です。<br>
多くのコマンドが存在しますが、今回は最低限以下を使えれば問題ないはず。<br>

```
git add (ファイル名)   # 指定したファイルを変更対象に登録
git commit           # addしたファイルを登録する（ローカルのgitに登録する）
git push             # 変更を登録する（リモートのgitに登録する）
git pull             # 変更を取り込む
```

上記コマンドの練習をする場合、以下の練習用リポジトリの１．〜３．を実施してみてください。<br>
[test_pull_request](https://github.com/seigot/test_pull_request)<br>
その他、詳しくは参考サイトを参照下さい。<br>

#### 参考リンク
[いまさらだけどGitを基本から分かりやすくまとめてみた](https://qiita.com/gold-kou/items/7f6a3b46e2781b0dd4a0)<br>
[【メモ】GitHubでgit clone〜git pushまで](https://qiita.com/nt-7/items/c5ea999a2638e03ee418)<br>
[[git] 基本操作（clone、add、commit、pushなど）を覚えて、開発出来るようになる](https://www.yoheim.net/blog.php?q=20140104)<br>
[【Git】基本コマンド](https://qiita.com/konweb/items/621722f67fdd8f86a017)

### 具体的なgitコマンド実行例

例) `tetris_game`をcloneしてきて、`block_controller2.py`という名のファイルをお試しでpushする<br>
  （`block_controller2.py`というお試しファイルのpushを好まない人はスキップして問題ありません）

![Screenshot](https://github.com/seigot/tetris_game_tutorial/blob/main/doc/how_to_use_git.PNG)

コマンド

```
cd ~                                                        # homeに移動
rm -rf tetris_game                                          # ディレクトリ削除
git clone http://github.com/(自分のリポジトリ名)/tetris_game  # (自分のリポジトリ名)/tetris_gameをcloneしてくる
cd tetris_game                                              # tetris_gameへ移動
cp block_controller.py block_controller2.py                 # とりあえずお試しファイルをコピー
git add block_controller2.py                                # お試しファイルを変更対象に登録
git commit -m "sample commit"                               # addしたファイルを登録する（ローカルのgitに登録する）
  ## もしplease tell me who you are とでたら、、ログに出ている以下を入力 
   git config --global user.email "You@example.com"
   git config --global user.name "YourName"
  ## その後、以下を実行してcommit
   git commit -m "sample commit"
   もしくは、
   git commit
   (エディタは esc+:wq  で終了できる)
git push                                                    # 変更を取り込む
   --> Githubアカウント(ユーザ名、パスワード)入力
```

## python
pythonはプログラミング言語の１つです。<br>
研究用途でも用いられる事が多く、サポートも豊富であり、プロトタイプ開発などに便利です。<br>
文法に関しても色々ハマり所はありますが、今回は最低限以下を使えれば問題ないはず。<br>

[print](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%96%87%E5%AD%97%E5%88%97%E3%81%A8%E6%95%B0%E5%80%A4%E3%81%AE%E9%81%95%E3%81%84)<br>
[演算子（*,/,+.-）](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%95%B0%E5%80%A4)<br>
[加算代入演算子（+=）、減算代入演算子（-=）](https://techacademy.jp/magazine/24516)<br>
[max,min,sum](https://himibrog.com/python-min-max-sum/)<br>
[論理演算子（and, or）](https://www.python.jp/train/logical_oper/index.html)<br>
[括弧 ()](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%95%B0%E5%80%A4)<br>
[if文](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90-if%E6%96%87)<br>
[演算子](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%9D%A1%E4%BB%B6%E5%BC%8F%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9)<br>
[list型](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E3%83%AA%E3%82%B9%E3%83%88%E5%9E%8B)<br>
[辞書型](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E8%BE%9E%E6%9B%B8%E5%9E%8B)<br>
[tuple型](https://www.python.jp/train/tuple/index.html)<br>
[len](https://qiita.com/Macchino5/items/a64347f9e832406d3c24)<br>
[for x in [1,2,3,4]:](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#for%E6%96%87)<br>
[for x0 in for range(2,8)](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#for%E6%96%87)<br>
[continue](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#for%E6%96%87)<br>
[3種類のrange,(range(1,3),range(height - 1, 0, -1):,range(width),)](https://udemy.benesse.co.jp/development/python-work/python-for.html)<br>
[while](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#while%E6%96%87)<br>
[関数](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E9%96%A2%E6%95%B0%E3%81%A8%E3%81%AF)<br>
[ライブラリ](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA)<br>
[class](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E6%8C%87%E5%90%91)<br>
<br>
[おまけ:PythonでFizz Buzz書いてみた](https://qiita.com/Sekky0905/items/7e2b13f2a001384c7fc4)<br>
その他、詳しくは参考サイトを参照下さい。<br>

#### 参考リンク
[【初心者向け】無料でPythonの基本文法を5時間で学ぼう！](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb)<br>
[Pythonの基礎基本を30分ですべて終わらせる](https://qiita.com/nol_miryuu/items/33fcdb1c4a656644ffe2)
[Python3基礎文法](https://qiita.com/Fendo181/items/a934e4f94021115efb2e)<br>
[初心者がPythonの練習](https://qiita.com/pugiemonn/items/c98e4e24daa177975240)<br>

### 具体的なpythonコマンド実行例

```
python3 tutorial1.py
```

## `tetris_gameのブロック操作用サンプルプログラム(block_controller_sample.py)`での使用例
以下を作成中<br>
[tetris_gameのブロック操作用サンプルプログラム(block_controller_sample.py)でのpython使用例](https://github.com/seigot/tetris_game_tutorial/blob/main/SAMPLE.md)

## 次のステップ

[tetris_game](https://github.com/seigot/tetris_game)の[ブロック操作用プログラムについて](https://github.com/seigot/tetris_game/blob/master/doc/files/block_controller.md)や[ブロック操作用サンプルプログラム](https://github.com/seigot/tetris_game/blob/master/doc/files/block_controller_sample.md)を読み進めて下さい。<br>
