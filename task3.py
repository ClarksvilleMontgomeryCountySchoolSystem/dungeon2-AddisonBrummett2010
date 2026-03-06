good = """ 888                                              
888                                              
888                                              
88888b.  8888b. 88888b.  8888b. 88888b.  8888b.  
888 "88b    "88b888 "88b    "88b888 "88b    "88b 
888  888.d888888888  888.d888888888  888.d888888 
888 d88P888  888888  888888  888888  888888  888 
88888P" "Y888888888  888"Y888888888  888"Y888888  """
bad = """
 /`-.__                                 /\
 `. .  ~~--..__                   __..-' ,'
   `.`-.._     ~~---...___...---~~  _,~,/
     `-._ ~--..__             __..-~ _-~
         ~~-..__ ~~--.....--~~   _.-~
                ~~--...___...--~~                       
 """
guard_awake = True
if guard_awake:
    outcome = "Doom: Be careful you could get caught."
    print(bad)
else:
    outcome = "Shadow: Listen for footsteps."
    print(good)
print(outcome)