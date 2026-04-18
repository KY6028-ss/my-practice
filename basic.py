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