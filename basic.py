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
print("")