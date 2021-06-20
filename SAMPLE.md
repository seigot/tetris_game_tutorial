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

## `加算代入演算子（+=）、減算代入演算子（-=）`

ボードの盤面評価時に使用しています。<br>
仮にブロックを置いた際に、消えるラインの数をカウントしています。

```
# filled with block
fullLines += 1
```

## `max,min,sum`

ボードの盤面評価時に使用しようとしました。（コメントアウトしています）<br>
フィールド上に積まれているブロックの高さの最大値を取得しようとしています。<br>

```
#### maxDy
#maxDy = max(BlockMaxY) - min(BlockMaxY)
```

## `論理演算子（and, or）`

後述する`if文`の条件式に使用しています。<br>
その他、いたるところで使用しています。<br>

```
if hasBlock == True and hasHole == False:
   # filled with block
   fullLines += 1
```

## `括弧 ()`

`if文`の条件式や、探索時の計算時に多用しています。<br>
その他、いたるところで使用しています。<br>

## `if文`

ブロックを置く位置の探索時、最適と判断した位置の評価スコアを保持する際に使用しています。<br>
その他、いたるところで使用しています。<br>

```
# evaluate board
EvalValue = self.calcEvaluationValueSample(board)
# update best move
if EvalValue > LatestEvalValue:
    strategy = (direction0, x0, 1, 1)
    LatestEvalValue = EvalValue
```

## `比較演算子`

`if文`同様に評価スコアを扱う際に多用しています。<br>
その他、いたるところで使用しています。<br>

## `list型`

ボードの盤面評価時に使用しています。<br>
評価時の一時データ格納用（ブロックの高さが平坦になるかどうかを計算する用）に使っています。

```
### absolute differencial value of MaxY
BlockMaxDy = []
for i in range(len(BlockMaxY) - 1):
    val = BlockMaxY[i] - BlockMaxY[i+1]
    BlockMaxDy += [val]
for x in BlockMaxDy:
    absDy += abs(x)
```

## `辞書型`

`GameStatus`データ管理に使用しています。
フィールド情報などを以下のように取得します。

```
# default board definition
self.board_data_width = GameStatus["field_info"]["width"]
self.board_data_height = GameStatus["field_info"]["height"]
```

## `tuple型`

サンプルプログラムでは使ってない。

## `len`

ボードの盤面評価時に使用しようとしました。<br>
盤面評価時の評価データリストの長さを求める際に使います。<br>

## `for x in [1,2,3,4]:`

探索時に使っています。<br>
探索時にブロックの回転数を全て考慮したいため以下のように使用しています。<br>

```
# search with current block Shape
for direction0 in CurrentShapeDirectionRange:
    # search with x range
    x0Min, x0Max = self.getSearchXRange(self.CurrentShape_class, direction0)
```

## `for x0 in for range(2,8)`

探索時に使っています。<br>
探索時にx軸方向の位置を全て考慮したいため以下のように使用しています。<br>

```
for x0 in range(x0Min, x0Max):
# get board data, as if dropdown block
    board = self.getBoard(self.board_backboard, self.CurrentShape_class, direction0, x0)
```

## `continue`

サンプルプログラムでは使っていない。

## `3種類のrange,(range(1,3),range(height - 1, 0, -1):,range(width),)`

`for x in [1,2,3,4]:`、`for x0 in for range(2,8)`と使い方は同じ

## `while`

探索時に使用しています。<br>
フィールドに仮にブロックを置く際、どれくらいのブロック数落下可能かを調べる際に使用しています。

```
# update dy
for _x, _y in coordArray:
    _yy = 0
    while _yy + _y < self.board_data_height and (_yy + _y < 0 or board[(_y + _yy) * self.board_data_width + _x] == self.ShapeNone_index):
        _yy += 1
    _yy -= 1
    if _yy < dy:
        dy = _yy
```

## `関数`
`block_controller.py`において`def GetNextMove(self, nextMove, GameStatus):`として使用しています。

## `ライブラリ`
`block_controller.py`において`pprint`、`copy`をimportして使用しています。

```
import pprint
import copy
```

## `class`

`block_controller.py`において`class Block_Controller(object):`として使用しています。
