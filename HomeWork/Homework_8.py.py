#1
family = {
"Artem": {'Age = 13; Data birhday = 25.10.2009; Phone = +380955080681; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = IT, Football, play computer games; '},
'Olena': {'Age = 52; Data birhday = 02.08.1970; Phone = +380503868040; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = Cook, play violin ' },
'Ihor' : {'Age = 53; Data birhday = 25.12.1969; Phone = +380503358550; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = IT, cook, play computer games; '},
'Maria': {'Age = 20; Data birhday = 12.10.2002; Phone = +380669042218; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = tiktok, beuty, gymnastik; '},
'Anna' : {'Age = 13; Data birhday = 25.10.2009; Phone = +380955080681; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = Beuty, instagramm; '},
}
a= family[input('who do you want to know about? ')]
print(a)

#2, 2.1

for element in family:
    print(element)

print(family)

#3

family = {'Artem': 'Age = 13; Data birhday = 25.10.2009; Phone = +380955080681; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = IT, Football, play computer games; ', 'Olena': 'Age = 52; Data birhday = 02.08.1970; Phone = +380503868040; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = Cook, play violin', 'Anna': 'Age = 13; Data birhday = 25.10.2009; Phone = +380955080681; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/2; Hobby = Beuty, instagramm; ', 'Ihor': 'Age = 53; Data birhday = 25.12.1969; Phone = +380503358550; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = IT, cook, play computer games;', 'Maria': 'Age = 20; Data birhday = 12.10.2002; Phone = +380669042218; Adress = Ukriane, Kyiv 04210, Heroiv Stangrada 8/1; Hobby = tiktok, beuty, gymnastik;' }

print('Enter the key: ')
key = input()
if key in family:
   print(family[key])
else:
   print('The key is not in the dictionary')



#4

vokabelspusok = [11,72,23,84,25,66,37,68,99,20,81,42,23,84,35,16,47,18,89,90]
for h in enumerate(vokabelspusok):
    print(h)

#5

#Done


