#class
print("class")

# classの定義
class User:
    def __init__(self, name): 
        # インスタンス生成時に呼ばれる
        # インスタンス変数（属性の初期化）
        self.name = name
        print("Userクラスのinitが呼ばれました")
        print("name: ", self.name)

    def hello(self):
        print("Helloが呼ばれました")
        print("name: ", self.name)

# userというインスタンスを生成しています。
user = User("Sample User")

# userのhelloを呼ぶ
user.hello()

