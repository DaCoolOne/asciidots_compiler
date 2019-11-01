

# Executes pathtracer using a list queue thingy.

# Current instruction is pushed to the queue with a time of execution.

# Each operation has an input queue with an id for direction. Items are appended to queue if id matches. Otherwise items are 

"""

.-*-#1-{+}-$#-&
  \-#1--/

     |
     |
     v

1. (0) Create dots. Place split operation in the queue at t = 2.
2. (2) Split operation places two set operations into the queue at t = 4 and t = 5
3. (4) First set operation. Places add_place operation into the queue at t = 8
4. (5) Second set operation. Places add_place operation into the queue at t = 10
5. (8) Queue id set to horizontal. Value placed in horizontal queue.
6. (10) Queue performs add operation on a + b and places print operation into the queue at t = 14.
7. (11) Value outputed to console. End operation placed at t = 16.
8. End of program. 16 tick program run in just 8 ticks.

"""

import traceback

try:
	
	from runner import Compiler
	
	c = Compiler("script.dots")
	
except Exception as e:
	print(traceback.format_exc())

while True:
	pass



















