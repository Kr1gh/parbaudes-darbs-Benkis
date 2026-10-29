# ----------------------------------------------------------------------
# C1. Atzīmju kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar septiņām atzīmēm. Izvadi to skaitu, summu, vidējo, augstāko un zemāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā atzīmes, nosauc ar vārdu atzimju_saraksts.

atzimju_saraksts = [8, 6, 4, 9, 5, 7, 6]
print("Skaits:", len(atzimju_saraksts))
print("Summa:", sum(atzimju_saraksts))
print("Vidējais:", sum(atzimju_saraksts) / len(atzimju_saraksts))
print("Augstākais:", max(atzimju_saraksts))
print("Zemākais:", min(atzimju_saraksts))
