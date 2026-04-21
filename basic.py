#変数宣言
num = 1
name = 'Mike'
is_ok = True

#変数の出力と型を確認
print(num, type(num))
print(name,type(name))
print(is_ok, type(is_ok))

#変数の型変換
num = 1
name = '1'

new_num = int(name)
print (new_num, type(new_num))

num: int =1
name: str = 'Mike'
is_ok: bool = True
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

print("-----------------------------------------")
#printで出力
#sepは区切り文字、endは出力後の文字
print('Hi','Mike',end='ーー')
print('Hi','Mike',sep=',',end='\n')
print("-----------------------------------------")
#値
print(1+1,1-1,1*1,1/1,1%1,1**1,1//1,sep='\n')
pie = 3.14159
print("丸めた円周率は" + str(round(pie, 2)))
#mathモジュールで計算できる
import math
result = math.sqrt(25)
print("25の平方根は" + str(result))

y = math.log2(2)
print("2の対数は" + str(y))

#print(help(math))
print("-----------------------------------------")
#文字列の出力
print("Hello World")
print('Hello World')
print("I don't know")
print('I don\'t know')
print("say \"I don't know\"")
print("hello.\nHow are you?")
print(r"C:\name\name")#raw文字列
print("-----------------------------------------")
#文字列の連結
print("""\
line1
line2
line3\
""")
print("-----------------------------------------")
print("Hi" * 3 + "Mike")
print("Py" + "thon")
s = "aaaaaaaaaaaaaaaa"\
    "bbbbbbbbbbbbbbbb"
print(s)
print("-----------------------------------------")
#文字列のインデックスとスライス
word = "Python"
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])#0から2の手前まで
print(word[:2])
print(word[2:])

word = "j" + word[1:]#文字列は変更できないため、インデックスを指定して変更することはできない。新しい文字列を作成する必要がある。
print(word)
print("-----------------------------------------")
n = len(word)#文字列の長さを取得
print(n)
print("-----------------------------------------")
#文字のメソッド
s = "My name is Mike. Hi Mike."
print(s)
is_start = s.startswith("My")#始まりが「My」かどうかを判定する
print(is_start)
is_start = s.startswith("X")#始まりが「X」かどうかを判定する
print(is_start)

print("-----------------------------------------")
print(s.find("Mike"))#「Mike」の最初　11番目にある
print(s.rfind("Mike"))#「Mike」の最後 20番目にある
print(s.count("Mike"))#「Mike」の個数
print(s.capitalize())#最初の文字を大文字にするほかは小文字
print(s.title())#全ての単語の最初の文字を大文字にする
print(s.upper())#全ての文字を大文字にする
print(s.lower())#全ての文字を小文字)
print(s.replace("Mike","Nancy"))#「Mike」を「Nancy」に置き換える):

#文字列のフォーマット formatメソッド　数字が文字列に変換され代入される
print("a is {}".format("apple"))
print("a is {} {} {}".format(1,2,3))
print("a is {0} {1} {2}".format(1,2,3))#インデックス指定
print("a is {2} {1} {0}".format(1,2,3))#インデックス指定（逆順）
print('My name is {0} {1}. I am {1} {0}'.format("KY","6028"))
print('My name is {name} {family}. I am {family} {name}'.format(name="KY", family="6028"))#キーワード引数で指定

#f-string　文字列の前にfをつけると、{}の中に変数や式を入れることができる
a = "apple"
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'x is {x}, y is {y}, z is {z}')
print(f'{x}{y}{z}{z}{y}{x}')
print(f'x + y is {x + y}')
