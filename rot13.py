
"""
Turn a string into another, rot13'd.
Requirements:
    + Hello -> Uryyb
    + Case preserved
    + Ponctuation preserved
    + Whitespace preserved
"""

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
	"j", "k", "l", "m", "n", "o", "p", "q", "r",
	"s", "t", "u", "v", "w", "x", "y", "z"
      ]

def parse(source):
    string = ""
    for char in source:
	# lowercase characters
	if char in abc:
	    position = abc.index(char)
	    rotate = (position + 13) % 26
	    string += abc[rotate]
	    
	# uppercase characters
	elif char.lower() in abc:
	    position = abc.index(char.lower())
	    rotate = (position + 13) % 26
	    string += abc[rotate].upper()
	# other cases
	else:
	    # Leave it as is
	    string += char
	
    return string