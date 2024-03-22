v = []


def hit(timestamp):
	v.append(timestamp)

# Time Complexity : O(1)

def getHits(timestamp):
	for i in range(0,len(v)):
		if (v[i] > timestamp - 300):
			break
	return len(v) - i

# Time Complexity : O(n)

