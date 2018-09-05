# Get Started
# [=]作為指派之用，有後蓋前的特性。
# 命名原則：區分大小寫，可用大小寫字母、數字跟底線[_]，但是第一個字不可以是數字。
# 部分保留字也不可用，雖然可以用case sensitive的特性來繞過(ex. if不可用但是IF可用)，但是相當不建議。

# 串列List, 寫法：li0[物件1, 物件2, ...]
# 物件可以使用各種類別，包含串列本身。不過str要用單引號包起來，串列則用中括號包覆。
print ('串列範例')
li0 = ['alice', 30, 95, 'engineer', ['C', 'Python']]
a = li0[4]
b = li0[4][1]
print (a)
print (b)

print ('---------->8----------') #=====分隔線=====

#可變(mutable)不可變(imutable)物件
# int / float / str都不可變, 變更的部分不是物件內容變更，而是轉向指派其他物件而已。
print ('可變/不可變')
a = 3
a = 4  #把a指派給另外一個物件
print (a)
b = a
print (b)
b = 3
print (b, a) #把b指派給另外一個物件，a不變。
# list是可變的
a = [100, 200, 300]
b = a
print (b)
b[0] = 99
print (a) #變更別名b, a也跟著變了。使用上要留意。

print ('---------->8----------') #=====分隔線=====

print ('元組範例')
#元組tuple，可以用來解決list可變的問題。寫法與list基本上相同，只是把中括號改成小括號。
t0 = (11, 22, 33)
a = t0[0]
print (a)
b = t0
print (b[0])
#b[0] = 44 #會跳錯誤訊息，因為tuple是不可變的。

print ('只含一個元素的list或tuple')
a = ['apple is good']
print (a[0])
b = ('banana is good') #第一個物件後面要加逗點，不然會印不出來
c = ('cat is good',)
print (b[0])
print (c[0])

print ('---------->8----------') #=====分隔線=====

print ('運算子')
'''
除法有分 / 跟 //。 
/為一般除法，結果為浮點數float; //為地板除法(floor division), 會找出最接近的最小整數。
'''
a, b, c = 17, 3, -3
print (a / b)
print (type(a / b))
print (a // b)
print (type(a // b))
print (a / c) 
print (a // c) #接近-5.666666667的最"小"整數為-6，而不是-5.
'''
*為乘法，**為冪次方。17*3=17*17*17=4913
%為取餘數，17除以3=5餘2. 17%3=2.
'''
print (a * b)
print (a ** b)
print (a % b)
print (type(a % b))
#int / list / tuple可以透過+來串接以及*來重複幾次，類型與原本相同。
print ('hello' + ' ' + 'world')
print (type('hello' + ' ' + 'world'))
print ('hello ' * 4)
print (type('hello ' * 4))
print ([0, 1, 2]+[3, 4, 5])
print (type([0, 1, 2]+[3, 4, 5]))
print ((0, 1, 2) * 4)
print (type((0, 1, 2) * 4))

print ('---------->8----------') #=====分隔線=====


