# `tetris_gameのブロック操作用サンプルプログラム(block_controller_sample.py)`でのpython使用例

## `print`

数値や文字列を出力します。<br>
`tetris_game`ではプログラム作成時の補助のため、ブロックの動きや、確認用文字列をデフォルトで出力しています。<br>

```
print(nextMove)                        # ブロックの動きを出力
print("###### SAMPLE CODE ######")     # 文字列を出力
```

大量データをそのまま出力すると見づらいため、`pprint(pretty-print`で出力を整形している部分もあります。

```
pprint.pprint(GameStatus, width = 61, compact = True)  # GameStatusを整形して出力
```

## `演算子（*,/,+.-）`
四則演算を行います。<br>
`tetris_game`では、サンプルプログラムでの盤面評価スコアの計算に使用しています。<br>
足し算(+)と引き算(-)よりも、掛け算(*)と割り算(/)の計算が優先されます。<br>

```
# calc Evaluation Value
score = 0
score = score + fullLines * 10.0           # try to delete line 
score = score - nHoles * 1.0               # try not to make hole
score = score - nIsolatedBlocks * 1.0      # try not to make isolated block
score = score - absDy * 1.0                # try to put block smoothly
```

boardのデータへアクセスする際にも使用しています。<br>
データは一次元に管理しているため、`(x, y)`の座標は`[x + y*(ボードの横幅)]`番目に格納されていることになります。<br>

```
board[_y * self.board_data_width + _x] == self.ShapeNone_index
```

## `加算代入演算子（+=）、減算代入演算子（-=）`
## `max,min,sum`
## `論理演算子（and, or）`
## `括弧 ()`
## `if文`
## `演算子`
## `list型`
## `辞書型`
## `tuple型`
## `len`
## `for x in [1,2,3,4]:`
## `for x0 in for range(2,8)`
## `continue`
## `3種類のrange,(range(1,3),range(height - 1, 0, -1):,range(width),)`
## `while`
## `関数`
## `ライブラリ`
## `class`

