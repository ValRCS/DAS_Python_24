# risinot uzdevumu, tiek pieņemts, ka tiek ievadīts gramatiski korekts teikums!
# tiek pieņemts, ka vārdu no pārējās teksta virknes atdala tukšums, pieturzīme vai rindas beigas vai sākums

# Lai šo risinājumu uzlabotu, ērti būt izmantot sarakstus!
 
vards_begin="nav" # meklējamās frāzes sākuma vārds
vards_end="slikt" # meklējamās frāzes beigu vārds
fraze="ir lab" # aizvietojamā frāze

rinda=input("Ievadiet gramatiski korektu teksta rindu: ")

poz1=str.find(rinda.lower(), vards_begin,0) # 0 is actually the default value
poz2=str.rfind(rinda.lower(), vards_end, poz1) # šoreiz šādi var darīt, jo ja poz1=-1, tad poz2 vairs neinteresē

# pārbaudam vai pirms vārda ir atstarpe
if poz1>0 and rinda[poz1-1] != " ":
    poz1=-1

#pārbaudam vai pēc vārda ir atstarpe vai pieturzīme
if poz1>-1 and len(rinda)>len(vards_begin) and rinda[poz1 + len(vards_begin)] != " " and rinda[poz1 + len(vards_begin)] != ",":
    poz1=-1

#pārbaudam, vai pirs otrā vārda ir atstarpe
if poz2>0 and rinda[poz2-1] != " ":
    poz2=-1

#pārbaudam vai pēc otrā vārda ir atstarpe vai pieturzīme
if len(rinda) > poz2+len(vards_end):
    if poz2>0 and rinda[poz2 + len(vards_end)] != " " and rinda[poz2 + len(vards_end)] != "," and rinda[poz2 + len(vards_end)] != "." and rinda[poz2 + len(vards_end)] != "!" and rinda[poz2 + len(vards_end)] != "?":
        poz2=-1

# rezultāta izvade
if poz1 == 0:
    fraze = fraze.capitalize()

# šeit ja nav atrasts ne pirmais, ne otrais vārds tad izvadām visu rindu
if poz1>-1 and poz2>-1:
    print(rinda[0:poz1] + fraze + rinda[poz2+len(vards_end):])
else:
    print(rinda)