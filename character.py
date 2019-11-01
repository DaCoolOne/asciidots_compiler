

# Directions. Works with binary operations. For example, UP | DOWN = VERTICAL. HORIZONTAL & LEFT = True (LEFT)
class DIRECTION:
	NONE = 0
	UP = 1
	DOWN = 2
	LEFT = 4
	RIGHT = 8
	VERTICAL = 3
	HORIZONTAL = 12
	ALL = 15

class GUIDE:
	NONE = 0
	SEND_UP = 1
	SEND_DOWN = 2
	SEND_LEFT = 4
	SEND_RIGHT = 8
	REFLECTOR = 16
	REFLECT_A = 32
	REFLECT_B = 33

class SPECIAL:
	NONE = 0
	TILDA = 1
	EXCLAMATION = 2
	SPLITTER = 3
	COLON = 4
	SEMICOLON = 5
	QUESTION = 6
	END = 7
	START = 8
	HASHTAG = 9
	DOLLAR = 10
	CURLY = 11
	SQUARE = 12
	STRING = 16
	STRING_A = 17
	STRING_B = 18

def compact(dir):
	if dir == DIRECTION.NONE:
		return -1
	else:
		return ((dir & 2) >> 1) + ((dir & 4) >> 1) + ((dir & 8) >> 3) * 3

class character:
	def __init__(self, direction, guide, special = SPECIAL.NONE, char = ""):
		self.direction = direction
		self.guide = guide
		self.special = special
		self.char = char

char_map = {
	" " : character(DIRECTION.NONE, GUIDE.NONE),
	"|" : character(DIRECTION.VERTICAL, GUIDE.NONE),
	"!" : character(DIRECTION.VERTICAL, GUIDE.NONE, SPECIAL.EXCLAMATION),
	"-" : character(DIRECTION.HORIZONTAL, GUIDE.NONE),
	"+" : character(DIRECTION.ALL, GUIDE.NONE),
	"~" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.TILDA),
	"*" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.SPLITTER),
	"\\": character(DIRECTION.ALL, GUIDE.REFLECT_A),
	"/" : character(DIRECTION.ALL, GUIDE.REFLECT_B),
	"(" : character(DIRECTION.ALL, GUIDE.SEND_RIGHT | GUIDE.REFLECTOR),
	")" : character(DIRECTION.ALL, GUIDE.SEND_LEFT | GUIDE.REFLECTOR),
	"[" : character(DIRECTION.HORIZONTAL, GUIDE.NONE, SPECIAL.SQUARE),
	"]" : character(DIRECTION.HORIZONTAL, GUIDE.NONE, SPECIAL.SQUARE),
	"{" : character(DIRECTION.HORIZONTAL, GUIDE.NONE, SPECIAL.CURLY),
	"}" : character(DIRECTION.HORIZONTAL, GUIDE.NONE, SPECIAL.CURLY),
	">" : character(DIRECTION.ALL, GUIDE.SEND_RIGHT),
	"<" : character(DIRECTION.ALL, GUIDE.SEND_LEFT),
	"^" : character(DIRECTION.ALL, GUIDE.SEND_UP),
	"v" : character(DIRECTION.ALL, GUIDE.SEND_DOWN),
	";" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.SEMICOLON),
	":" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.COLON),
	"&" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.END),
	"." : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.START),
	"?" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.QUESTION),
	"#" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.HASHTAG),
	"$" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.DOLLAR),
	"'" : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.STRING_A),
	'"' : character(DIRECTION.ALL, GUIDE.NONE, SPECIAL.STRING_B),
}
char_map["•"] = char_map["."]

char_map_keys = char_map.keys()

def get_character(c):
	if c in char_map_keys:
		return char_map[c]
	else:
		# Todo, make this return something sensible
		return character(DIRECTION.ALL, GUIDE.NONE, char = c)

