morseAlphabet ={
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
" " : "/",
"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"0" : "-----"

}

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())
#print(inverseMorseAlphabet)


testCode = "...././.-../.-../---//-../.-/../.-../-.--//.--./.-./---/--./.-./.-/--/--/./.-.//--./---/---/-..//.-../..-/-.-./-.-//---/-.//-/...././/-.-./..../.-/.-../.-.././-./--././...//-/---/-../.-/-.--"

    # parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code, positionInString = 0):
	
	if positionInString < len(code):
		morseLetter = ""
		for key,char in enumerate(code[positionInString:]):
			if char == "/":
				positionInString = key+positionInString+1
				try:
					letter = inverseMorseAlphabet[morseLetter]
				except:
					letter = "?"
				return letter + decodeMorse(code, positionInString)
			else:
				morseLetter += char
	return ""


#print(decodeMorse("--/.-/-./../.../..../-.-/..-/--/.-/.-./.-."))
comb=open("comb").read().split("\n")
morse=["..",".-","./","-.","--","-/","/.","/-","//"]
string=open("morbid.txt").read()
for num in comb:
	dictionary={}
	count=0
	morsetext=""
	for i in num:
		dictionary.update({i:morse[count]})
		count+=1
	for i in string:
		morsetext+=dictionary[i]


	morsedecode=decodeMorse(morsetext)
	#print(morsedecode.count("?"))
	if(morsedecode.count("?") <= 20):
		print(morsedecode)
