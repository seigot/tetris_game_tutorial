<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [tetris_tutorial](#tetris_tutorial)
  - [まず動かしてみる](#%E3%81%BE%E3%81%9A%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B)
  - [Githubリポジトリfork](#github%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AAfork)
  - [エディタ](#%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF)
      - [参考<br>](#%E5%8F%82%E8%80%83br)
  - [ターミナルから使うコマンド](#%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%8B%E3%82%89%E4%BD%BF%E3%81%86%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)
      - [参考<br>](#%E5%8F%82%E8%80%83br-1)
  - [git](#git)
      - [参考](#%E5%8F%82%E8%80%83)
    - [gitコマンド使用例（`https://github.com/seigot/test_pull_request`を使う場合）](#git%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E4%BD%BF%E7%94%A8%E4%BE%8Bhttpsgithubcomseigottest_pull_request%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)
    - [gitコマンド使用例（`http://github.com/(自分のアカウント名)/tetris`を使う場合）](#git%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E4%BD%BF%E7%94%A8%E4%BE%8Bhttpgithubcom%E8%87%AA%E5%88%86%E3%81%AE%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E5%90%8Dtetris%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)
    - [githubへpushする際の認証方法の変更](#github%E3%81%B8push%E3%81%99%E3%82%8B%E9%9A%9B%E3%81%AE%E8%AA%8D%E8%A8%BC%E6%96%B9%E6%B3%95%E3%81%AE%E5%A4%89%E6%9B%B4)
  - [python](#python)
      - [参考](#%E5%8F%82%E8%80%83-1)
    - [python使用例](#python%E4%BD%BF%E7%94%A8%E4%BE%8B)
  - [`tetrisのブロック操作用サンプルプログラム(block_controller_sample.py)`での使用例](#tetris%E3%81%AE%E3%83%96%E3%83%AD%E3%83%83%E3%82%AF%E6%93%8D%E4%BD%9C%E7%94%A8%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0block_controller_samplepy%E3%81%A7%E3%81%AE%E4%BD%BF%E7%94%A8%E4%BE%8B)
  - [次のステップ](#%E6%AC%A1%E3%81%AE%E3%82%B9%E3%83%86%E3%83%83%E3%83%97)
  - [その次のステップ](#%E3%81%9D%E3%81%AE%E6%AC%A1%E3%81%AE%E3%82%B9%E3%83%86%E3%83%83%E3%83%97)
- [以下、参考](#%E4%BB%A5%E4%B8%8B%E5%8F%82%E8%80%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# tetris_tutorial

[tetris](https://github.com/seigot/tetris)プログラミング用のチュートリアルです。<br>
このチュートリアルを理解すれば[tetrisのブロック操作用サンプルプログラム(block_controller_sample.py)](https://github.com/seigot/tetris/blob/master/doc/files/block_controller_sample.md)が読めるようになることを目指しています。<br>
<br>
プルリクエスト募集中です。<br>
<br>

## まず動かしてみる
[tetris](https://github.com/seigot/tetris)の「実行環境準備」を参照して、まず動かしてみる。<br>
困った時は[FAQ](https://github.com/seigot/tetris/blob/master/doc/files/FAQ.md)など参照。

## Githubリポジトリfork
[tetris](https://github.com/seigot/tetris)をforkする。これは[tetris](https://github.com/seigot/tetris)の右上の「Fork」ボタンを押せばOK<br>
[tetris](https://github.com/seigot/tetris)を「コード作成のはじめかた」にも詳細を記載している<br>

## エディタ

世の中には色々なエディタがありますが、最終的には自分の好みで選択するのがよさそうです。<br>

|  エディタ名  |  特徴  |  備考  |
| ---- | ---- | ---- |
|  vi  |  -  |  -  |
|  emacs  |  -  |  -  |
|  gedit  |  -  |  -  |
|  vscode  |  Microsoftのエディタ、機能まぁまぁ、グラフィカルで操作はわかりやすい、ただ重い<br> [MacOSでVisual Studio Codeをインストールする手順](https://qiita.com/watamura/items/51c70fbb848e5f956fd6)<br>[Microsoft Visual Studio Codev1.56.0](https://winget.run/pkg/Microsoft/VisualStudioCode)<br>[UbuntuにVSCodeをインストールする3つの方法](https://qiita.com/yoshiyasu1111/items/e21a77ed68b52cb5f7c8)  |  -  |
|  spyder  |  pythonの統合開発環境（エディタ進化版）、デバッグとかしやすい、ただ重い  |  -  |
|  nano  |  vimよりマシな操作感、軽い、ただ結局コマンドを覚えないと保存すらできない  |  -  |
|  vim  |  とりあえず感覚的に操作できないからハードル高い、ただ覚えれば効率は一番いいかも  |  -  |
|  その他  |  -  |  -  |

#### 参考<br>
更新するかも

## ターミナルから使うコマンド

ターミナルから使うコマンドです。<br>
今回は最低限以下を使えれば問題ないはず。<br>

```
cd     : ディレクトリの移動。change directoryの略
ls     : 現在のディレクトリのファイルを表示。listの略
rm     : ファイルを削除。removeの略
rm  -r : ディレクトリを削除。
```

#### 参考<br>
[ターミナルのよく使うコマンド](https://qiita.com/ryo2132/items/b7e312b0eb50fc449841)

## git 
gitはソフトウェアのバージョン管理システムです。<br>
github上での`tetris`用ソースコード管理をコマンドラインから操作することが可能です。<br>
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

#### 参考
[いまさらだけどGitを基本から分かりやすくまとめてみた](https://qiita.com/gold-kou/items/7f6a3b46e2781b0dd4a0)<br>
[【メモ】GitHubでgit clone〜git pushまで](https://qiita.com/nt-7/items/c5ea999a2638e03ee418)<br>
[[git] 基本操作（clone、add、commit、pushなど）を覚えて、開発出来るようになる](https://www.yoheim.net/blog.php?q=20140104)<br>
[【Git】基本コマンド](https://qiita.com/konweb/items/621722f67fdd8f86a017)

### gitコマンド使用例（`https://github.com/seigot/test_pull_request`を使う場合）

- リポジトリをforkする<br>

まず、[test_pull_request](https://github.com/seigot/test_pull_request)にアクセスしてリポジトリを`fork`する。  
右上の「Fork」ボタンを押せばOK

- リポジトリをcloneする<br>

次に、forkしたリポジトリを`git clone`する<br>
※`(自分のアカウント名)`の部分は、自分アカウント名に置き換える

```
git clone https://github.com/(自分のアカウント名)/test_pull_request

# 例 (自分のアカウント名)=seigotの場合
git clone https://github.com/seigot/test_pull_request
```

- `git add/commit/push`する、<br>

```
cd test_pull_request                      # git clone https://github.com/(自分のアカウント名)/test_pull_requestで取得したリポジトリに移動する。
echo "this_is_test_string" >> README.md   # README.mdファイルを更新する
git add README.md                         # git add
git commit -m "update README.md"          # git commit
git push                                  # git push
```

- 更新の確認 <br>

`https://github.com/(自分のアカウント名)/test_pull_request`にアクセスして、更新が反映されていればOK  
※`(自分のアカウント名)`の部分は、自分アカウント名に置き換える

### gitコマンド使用例（`http://github.com/(自分のアカウント名)/tetris`を使う場合）

例) `tetris`をcloneしてきて、`block_controller2.py`という名のファイルをお試しでpushする<br>
  （`block_controller2.py`というお試しファイルのpushを好まない人はスキップして問題ありません）

![Screenshot](https://github.com/seigot/tetris_game_tutorial/blob/main/doc/how_to_use_git2.png)

コマンド

```
cd ~                                                        # homeに移動
rm -rf tetris                                               # ディレクトリ削除
git clone http://github.com/(自分のアカウント名)/tetris       # (自分のアカウント名)/tetrisをcloneしてくる
cd tetris                                                   # tetrisへ移動
cp block_controller.py block_controller2.py                 # とりあえずお試しファイルをコピー
git add block_controller2.py                                # お試しファイルを変更対象に登録
git commit -m "sample commit"                               # addしたファイルを登録する（ローカルリポジトリに登録する）
  ## もしplease tell me who you are とでたら、、ログに出ている以下を入力 
   git config --global user.email "You@example.com"
   git config --global user.name "YourName"
  ## その後、以下を実行してcommit
   git commit -m "sample commit"
   もしくは、
   git commit
   (エディタは esc+:wq  で終了できる)
git push                                                    # リモートリポジトリに登録する
   --> Githubアカウント(ユーザ名、パスワード)入力
```

githubの自リポジトリ上に変更が加わっていることがみえたらOKです。

### githubへpushする際の認証方法の変更

2021/8/13より、Githubへ認証が必要なgit操作をする場合は、Passwordによる認証からアクセストークンを使用した認証に変わったようです。<br>
使用方法は以下の通り公式サイトを参照すればOK。  

> [個人アクセストークンを使用する](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token)
> [githubの個人アクセストークンを使用する](https://qiita.com/seigot/items/605661666f074547a89e)


## python
pythonはプログラミング言語の１つです。<br>
研究用途でも用いられる事が多く、サポートも豊富であり、プロトタイプ開発などに便利です。<br>
文法に関しても色々ハマり所はありますが、今回は最低限以下を使えれば問題ないはず。<br>

以下を参考にしています。<br>
> [【初心者向け】無料でPythonの基本文法を5時間で学ぼう！AI_Academy](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb)  
> [AtCoderで始めるPython入門](https://qiita.com/KoyanagiHitoshi/items/3286fbc65d56dd67737c)  
> [公式サイト: Top - python.jp](https://www.python.jp/)  

[print](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%96%87%E5%AD%97%E5%88%97%E3%81%A8%E6%95%B0%E5%80%A4%E3%81%AE%E9%81%95%E3%81%84)<br>
[演算子（*,/,+.-）](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%95%B0%E5%80%A4)<br>
[加算代入演算子（+=）、減算代入演算子（-=）](https://techacademy.jp/magazine/24516)<br>
[max,min,sum](https://himibrog.com/python-min-max-sum/)<br>
[論理演算子（and, or）](https://www.python.jp/train/logical_oper/index.html)<br>
[括弧 ()](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%95%B0%E5%80%A4)<br>
[if文](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90-if%E6%96%87)<br>
[比較演算子](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb#%E6%9D%A1%E4%BB%B6%E5%BC%8F%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9)<br>
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

#### 参考
[【初心者向け】無料でPythonの基本文法を5時間で学ぼう！](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb)<br>
[Pythonの基礎基本を30分ですべて終わらせる](https://qiita.com/nol_miryuu/items/33fcdb1c4a656644ffe2)
[Python3基礎文法](https://qiita.com/Fendo181/items/a934e4f94021115efb2e)<br>
[初心者がPythonの練習](https://qiita.com/pugiemonn/items/c98e4e24daa177975240)<br>

### python使用例
[tutorial](https://github.com/seigot/tetris_game_tutorial/tree/main/tutorial)にお試し用pythonプログラムを置きました。<br>
使用手順の詳細は[tutorial/README.md](https://github.com/seigot/tetris_game_tutorial/blob/main/tutorial/README.md)を参照ください。


```
git clone http://github.com/seigot/tetris_game_tutorial  # tutorialディレクトリをclone
cd tetris_game_tutorial/tutorial                         # tutorialディレクトリへ移動
python3 tutorial1.py                                     # tutorial用プログラム実行
...
```

## `tetrisのブロック操作用サンプルプログラム(block_controller_sample.py)`での使用例
[tetrisのブロック操作用サンプルプログラム(block_controller_sample.py)でのpython使用例](https://github.com/seigot/tetris_game_tutorial/blob/main/SAMPLE.md)

## 次のステップ

[tetris](https://github.com/seigot/tetris)の[ブロック操作用プログラムについて](https://github.com/seigot/tetris/blob/master/doc/files/block_controller.md)や[ブロック操作用サンプルプログラム](https://github.com/seigot/tetris/blob/master/doc/files/block_controller_sample.md)を読み進めて下さい。<br>

## その次のステップ

自身のリポジトリ配下の[ブロック操作用プログラム(block_controller.py)](https://github.com/seigot/tetris/blob/master/game_manager/block_controller.py)をアップデートしてハイスコアを狙って下さい。<br>

# 以下、参考
[【初心者向け】無料でPythonの基本文法を5時間で学ぼう！AI_Academy](https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb)  
[AtCoderで始めるPython入門](https://qiita.com/KoyanagiHitoshi/items/3286fbc65d56dd67737c)  
[公式サイト: Top - python.jp](https://www.python.jp/)  
