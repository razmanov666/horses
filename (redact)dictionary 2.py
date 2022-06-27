
#GET

# метод get() вовзращает значение по указанному ключу.
# Если указанного ключа не существует то он вернет метод none

a = {'euro_food': 'pizza','uzbek-food':'cheburek','japan-food':'sushi'}
b = a.get('japan-food')
print(b)

y = {'espana':'FCB','apl':'leeds united','holland':'feinord'}
n = y.get('espana')
print(n)

c = {'0':0,'1':1,'2':2}
m = c.get('1')
print(m)

yuo = {'1':'NWA','first1':'108','3':'ug'}
p = yuo.get('3')
f = yuo.get('first1')
print(p,f)

fcb = {'messi':1,'inesta':10,10:'xavi'}
s = fcb.get(10,'inesta') #почему инеста не выдает свою 10ку
print(s)



# ITEMS

# Команда items() возвращает объект представления,
# который отображает список пар кортежей словаря (ключ, значение).

q = {'f': 1,'w': 2,'e': 3}
w = q.items()
print(w)


# # я хотел вывести значение одного ключа
# e = {'f': 1,'w': 2,'e': 3}
# w = e(f) #почему не работает через () и не работает через []
# print(w)
# # почему нет
# # только целый словарь он превращает в кортеж???

dictionary = {'f': 1,'w': 2,'e': 3}
s = dictionary.items()
print(s)
# реально как я понимаю items дает только одно значения


#values

# Метод values() возвращает объект представления,
# который отображает список всех значений в словаре.
# выдает значения по ключу

s = {'laliga': 1,"lique": 'only_marselee'}
a = s.values()
print(a)

e = {'laliga': 1,"lique": 'only_marselee'}
a = e.values() # вводил ла лига что бы он вернул один аргумент но он выводит только значения в словаре целиком
print(a)

k = {'tra':'ta','papa':'pa','la':'la'}
a = k.values()
print(a)

i = {11:2,99:3,66:2}
a = i.values()
print(a)

#KEY

# Этот метод также возвращает итерируемый объект.
# Он является списком всех ключей в словаре.
# Как и метод items(), этот отображает изменения в самом словаре.
#
# key - возвращает все ключи без значений
#


a = {'time':23,'food':'burgers','night':'beer'}
e = a.keys()
print(e)


i = {11:23,12:'burgers',13:'beer'}
o = i.keys()
print(o)

u = {'e':3,'r':4,'s':5}
l = u.keys()
print(l)






#CLEAR

# очищает словарЬ

A = {'e':3,'r':4,'s':5}
o = A.clear()
print(o)

# понятно обычный метод полного удаления словаря все понятно


# COPY

# возвращает копию словаря

j = {'e':300,'r':472,'s':555}
c = j.copy()
print(c)

# понятно но смысл его использования не совсем где на практике это нужно







# dict.fromkeys

# создает словарь с ключами из seq и значением value (по умолчанию None).

# синтаксис - dict.fromkeys(seq[, value])

# Существует метод словаря, который позволяет создавать словарь из двух наборов данных. Вот его синтаксис:
# Параметр keys принимает коллекцию, содержащую ключи. Параметр value можно и не указывать,
# тогда все ключи будут содержать пустые значения.
# Если указывать этот параметр, то его значение будет передано всем ключам:


# example = dict.fromkeys([1, 2, 3], 'Здесь может быть Ваша реклама')
# print(example)
# # Вывод:
#
# {1: 'Здесь может быть Ваша реклама', 2: 'Здесь может быть Ваша реклама', 3: 'Здесь может быть Ваша реклама'}


m = {'s':303,'z':473,'c':559}
s = m.fromkeys('s',559)
print(s)
# не понятно особо

g = {'s':303,'z':473,'c':559,'f':777,'x':899,'i':111,'t':222}
d = g.fromkeys('i','s')
print(d)

#суть понятна но зачем это нужно на практике такой замороченный ход непонятно зачем



#POP()

#pop() – удаляет и возвращает значение ключа


# dict = {
# 'car': 'машина',
# 'apple': 'яблоко',
# 'orange': 'апельсин'
# }
# print(dict.pop('car')) #Выведет ‘машина’
# print(dict) #Выведет {'apple': 'яблоко', 'orange': 'апельсин'}

g = {'s':'litva','z':'estonia','c':'Belarus','f':'armenia','x':'kyrgistan','i':111,'t':222}
print(g.pop('f'))

# почему я просто не могу использовать items()


# popitem()

# удаляет и возвращает имя и значение ключа

# Метод dict.popitem() удалит и вернет двойной кортеж (key, value) из словаря dict.
# Пары возвращаются с конца словаря, в порядке LIFO (последним пришёл - первым ушёл).
# Метод полезен для деструктивной итерации по словарю, как это часто используется в заданных алгоритмах.
# Если словарь пуст, вызов dict.popitem() вызывает исключение KeyError.
# Изменено в Python-3.7: порядок LIFO теперь гарантирован.
# В предыдущих версиях метод dict.popitem() возвращал бы произвольную пару ключ/значение.


q = {'s':'hongkok','z':'bangkok','c':'shanghai','f':'tokyo','x':'nankin','i':'kualalumpur','t':222}
x = q.popitem()
c = q.popitem()
j = q.popitem()
print(x,c,j)

# понятно но суть практического применения есть вопросы



# setdefault()

# Метод setdefault() возвращает значение ключа (если ключ находится в словаре).
# Если нет, он вставляет ключ со значением в словарь.

q = {'s':'hongkok','z':'bangkok','c':'shanghai','f':'tokyo','x':'nankin','i':'kualalumpur','t':222}
y = q.setdefault('s')
print(y)

# суть понятна



