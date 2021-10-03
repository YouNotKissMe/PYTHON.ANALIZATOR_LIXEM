
osnovnoyFile=open('Code/DA.txt','r',encoding="utf-8")
#osnovnoyFile=osnovnoyFile.read()
#удаление комментариев , не многострочных ,
#многострочных комментариев в питоне нет
balance=''
for line in osnovnoyFile:
    if line[0]=='#':
        balance+=''
    else:
        if line.find('#'):
            balance+=line[0:line.find('#')]
        else:
            balance+=line

strokoviekonstanti=[]

#print(balance)
# закончили удаление комментариев в питоне , разминка окончена
#удаление строковых констант и добавление их в массив
zed=0
a=-1
b=-1
while zed < len(balance)-1:
    if balance[zed]=="'":
        if a>=0:
            b=zed
            strokoviekonstanti.append(balance[a:b+1])
            a=-1
            b=-1
            zed+=1
        else:
            a=zed
            zed+=1
    else:
        zed+=1
zed=0
#print(strokoviekonstanti)
while zed <= len(balance)-1:

    if balance[zed]=="'":
        if a>=0:
            b=zed

            balance=balance[0:a]+ balance[b+1:len(balance)]
            a=-1
            b=-1
            zed+=1

        else:
            a=zed
            zed+=1
    else:
        zed+=1


zed=0
print(balance)
#закончили упражнение со строковыми константами,
#    ключевые слова
filewithrezdelitel=open('yjedano/da2.txt','r')
rezdelitel=filewithrezdelitel.read().split()
for i in rezdelitel:
    balance=balance.replace(i,' ')
#print(balance)
filewithslova=open('yjedano/da1.txt','r')
slova=filewithslova.read().split()
balance=balance.split()
for c in balance:
    for i in slova:
        for c in balance:
            if c==i:
                balance.remove(i)
#print(balance)
#Разбираемся с числами
chisla=[]
for i in balance:
    if i.isdigit():
        chisla.append(i)
        #balance.remove(i)
chisla=set(chisla)
chisla=[i for i in chisla]
for i in balance:
    for i in chisla:
        for c in balance:
            if c==i:
                balance.remove(i)
#print(chisla)
identidecator=[]
leks=True
for i in balance:
    if str.isalpha(i[0]):
        identidecator.append(i)
    else:
        leks=False
identidecator=set(identidecator)
identidecator=[i for i in identidecator]
print(identidecator)

'''в переменной 1)identifecator-переменные ,
                2)chisla - численные константы,
                3)slova - ключевые слова,
                4)strokoviekonstanti-строковые константы
                5)rezdelitel'''
#print(identidecator,' ',chisla,' ',slova,' ', strokoviekonstanti,' ',rezdelitel,' ')
osnovnoyFile=open('Code/DA.txt','r',encoding="utf-8")
balance=''

for line in osnovnoyFile:
    if line[0]=='#':
        balance+=''
    else:
        if line.find('#'):
            balance+=line[0:line.find('#')]
        else:
            balance+=line
print(balance)
#leks=True #####убрать
zed=0
b=''
for i in rezdelitel:
    balance=balance.replace(i,' '+i+' ')
zed=0
a=-1
#print(strokoviekonstanti)
while zed < len(balance)-1:
    if balance[zed]=="'":
        if a>=0:
            b=zed
            for s in strokoviekonstanti:
                if balance[a:b+1]==s:

                    balance=balance[0:a]+'Привет'+str(strokoviekonstanti.index(s))+ balance[b+1:len(balance)]
            a=-1
            b=-1
            zed+=0
        else:
            a=zed
            zed+=1
    else:
        zed+=1
overwotch=''
c=''
zed=0
dlinna=[i for i in rezdelitel if len(i)==2]
#print(dlinna)
balance=balance.split()
#print(range(len(balance)))
for j in range(len(balance)-1):
    #print(j)
    if c=='':
        c=balance[j]
        #print(c)
        zed+=1
    else:
        if c+balance[j] in dlinna:
            #print(c+balance[j])
            balance[j]=c+balance[j]
            balance[j-1]=''
            c=''
        else:
            c=''
for i in balance:
    overwotch +=i+' '
overwotch=overwotch.split()
#print(overwotch)
zed=0
zef=list(range(0,len(strokoviekonstanti)))
#print('Привет'+str(zef))
if leks==True:
    for i in overwotch:
        if i[0:-1]!='Привет':
                for a in identidecator:
                    if i == a:
                        print(str(overwotch.index(i)),'1 ', a)
                        zed += 1
                for b in chisla:
                    if i == b:
                        print(str(overwotch.index(i)),'2 ', b)
                        zed += 1

                for d in rezdelitel:
                    if i == d:
                        print(str(overwotch.index(i)),'5 ', d)
                        zed += 1
                for e in slova:
                    if i == e:
                        print(str(overwotch.index(i)),'3', e)
                        zed += 1
        else:
                print(str(overwotch.index(i)),'4',strokoviekonstanti[int(i[-1])])
                zed+=1

else:
     print('Ошибка')
print(zed,' ', len(overwotch))







