good = """ 888         
                        888         
                        888         
 .d88b.  8888b.  .d88b. 888 .d88b.  
d8P  Y8b    "88bd88P"88b888d8P  Y8b 
88888888.d888888888  88888888888888 
Y8b.    888  888Y88b 888888Y8b.     
 "Y8888 "Y888888 "Y88888888 "Y8888  
                     888            
                Y8b d88P            
                 "Y88P"    """
bad = """       .,oo8888888888888888ooo,.
    ,od88888888888888888888888888oo,
 ,o0MMMMMMMMNMMMMM8888888888888888888o.
d888888888V'.o   ```VoooooooOOOOOOOOIII,
l888LLLLl:  O , ,O    ``VlMM88888IIAMMMMMOMb,
l8888888LLb `VooV',O,MoodlM88888IIIMMMMV'ddMOMb,
l88888888888booooooOlllllIIIIIIIIIAMMV',dMMOOMMMb,
888888888888888888LLLLIAMMMMMMMMMMMMMMMMMOOOMMMMMMb,
8M8888888888LLLMMMAAMMMAAMMMMMMMMMMMMMMOOOOMMMMMMMMb
88M8888888lll888888mmmmmmmmmmmmmmvvvvvvvvvvvvv,`MMMM
8888M888888llllllllllllllV::::V''~~        ~~'V lMMV
M8888MMM888888TTTMl8lllllb:::V'                `IiM'
MMMMM8888M8k88888l8Mklllllk:A'                  `V'
lMMMMMM888888888888MMMMMlll:M  Gary G. Nass
l8MM8MMMM8888888888888MMMMllM """
escaped = True
if not escaped:
    outcome = "Doom: Oh no! Keep trying."
    print(bad)
else:
    outcome = "Legend: Yay! We made it."
    print(good)
print(outcome)