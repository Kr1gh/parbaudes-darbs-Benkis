# ----------------------------------------------------------------------
# C2. Degviela un braucieni
# ----------------------------------------------------------------------

# Tvertnē ir 50 litri degvielas. Viens brauciens patērē 7 litrus. Izvadi, cik braucienu var veikt un cik degvielas paliek pāri. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Katru rezultāta rindu beidz ar punktu.

t = 50
b = 7
k = 0
while t >= b:
  t = t - b
  k = k + 1
if k == 1:
  print("Var veikt", k, "braucienu.")
else:
  print("Var veikt", k, "braucienus.")
if t == 1:
  print("paliek pāri", t, "litrs.")
else:
  print("paliek pāri", t, "litri.")
