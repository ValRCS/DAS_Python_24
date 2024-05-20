# 3. Pilsēta
# Pilsētā ir zināms skaits iedzīvotāju p0
# Katru gadu nāk klāt procentuāls skaits perc
# Katru gadu nāk klāt(vai aizbrauc) arī zināms
# skaits delta
# Mums ir jāzina, kad(ja vispār) pilsēta
# sasniegs iedzīvotāju skaitu p_target
# Uzrakstiet funkciju get_city_year(p0, perc, delta, p_target) kas atgriež gadus (pilnus) kad p_target tiks sasniegts.
# Ja p nevar sasniegt, tad atgriežam -1
# Piemērs:
# get_city_year(1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 pēc 1.gada
# 1070 + 1070 * 0.02 + 50 => 1141 pēc 2.gada
# 1141 + 1141 * 0.02 + 50 => 1213 pēc 3.gada
# PS. Ievērojam, ka padodam perc kā procentu kas jāpārvērš decimāl skaitlī.
# Pārbaudam, vai strādā ar sekojošiem parametriem:
# get_city_year(1000, 2, -50, 5000) -> -1 # samērā aktuāla problēma
# get_city_year(1500, 5, 100, 5000) -> 15
# get_city_year(1500000, 2.5, 10000, 2000000) -> 10


def get_city_year(p0, perc, delta, p_target):
    i=0
    rez=p0
    
    while rez<=p_target and i>-1:
        rez=rez+rez*perc*0.01+delta    
        i+=1

        if rez<=p0:
            i=-1
        print(rez, i)

    return i

print(get_city_year(1000, 2, -50, 5000) ) # -1
print(get_city_year(1500, 5, 100, 5000)) # 15
print(get_city_year(1500000, 2.5, 10000, 2000000)) # 10
print(get_city_year(1000,-3,40,2000)) # TODO FIXME this should be -1 but it is infinite loop