v = []

# Record a hit.
# @param timestamp - The current timestamp (in 
#					 seconds granularity). */

def hit(timestamp):
	v.append(timestamp)

# Time Complexity : O(1)

# Return the number of hits in the past 5 minutes.
# @param timestamp - The current timestamp (in
# seconds granularity). */
def getHits(timestamp):
	# for (i = 0; i < v.length; ++i) {
	for i in range(0,len(v)):
		if (v[i] > timestamp - 300):
			break
	return len(v) - i

# Time Complexity : O(n)

