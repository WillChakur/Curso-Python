#Trabalhos
trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
tv_30 = trabalho_terca or trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
ficar_em_casa = (trabalho_quinta == False) and (trabalho_terca == False)

print("Tv50={} Tv32={} Sorvete={} Ficar_em_casa={}".format(tv_50, tv_30, sorvete, ficar_em_casa))

#O .format junto com as chaves funcinam como o %d no C
