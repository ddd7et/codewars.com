string = "This website is for losers LOL!" 
vovwl = [1, 5, 9, 15, 21] 
print(string)

new_s = ""
for s in string:

	if not any(c in vovwl for c in (ord(s)-64, ord(s)-96 )):
		new_s += s


print(new_s)
# "Ths wbst s fr lsrs LL!".