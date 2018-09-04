import time
import random
from os import system

# Wait for random length of time between 2 and 6 seconds and return None
def wait():
	waittime = random.randrange(2, 6)
	time.sleep(waittime)
	return None

def compare(result):
	if result > 500:
		return 'It is really slow!'
	if result > 320:
		return 'It is not that bad.'
	if result > 250:
		return 'It is pretty good.'
	if result > 0:
		return 'It is great!'
	if result == 0:
		return 'Cheater! Too early!'
	return None

while True:
	input("Wait for a sign and click Enter as fast as you can!     Get ready and click enter to start")
	wait()
	print("##################\n###### CLICK #####\n####### NOW ######\n##################")
	# Time in seconds right after "click now" appeared
	starttime = time.time()
	input()
	# Time difference after user clicked enter and starttime
	timedifference = time.time() - starttime
	# Time converted to XXX ms
	reactiontime = int(round(timedifference, 3) * 1000)
	print("Your reaction time is {}ms\n{}".format(reactiontime, compare(reactiontime)))
	input()
	system('cls')
	