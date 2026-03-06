good = """ *-*,
        ,*\/|`| \
        \'  | |'| *,
         \ `| | |/ )
          | |'| , /
          |'| |, /
        __|_|_|_|__
       [___________]
        |         |
        |         |
        |         |
        |_________| """
bad = """   _    _
            | |  | |
           -| |  | |-
       _    | |- | |
     -| |   | |  | |-
      |.|  -| ||/  |
      | |-  |  ___/
     -|.|   | | |
      |  \_|| |
       \____  |
        |   | |-
            | |
           -| | mga
            |_| """
drawbridge_raised = True
if drawbridge_raised:
    outcome = "Doom: Wait for drawbridge."
    print(bad)
else:
    outcome = "Thunder: Cross it."
    print(good)
print(outcome)