# python implementation to find LIS

# Return length of LIS in arr[] of size N
def lis(arr):
	s = set()
	for i in range(len(arr)):
	
		# Check if the element was actually inserted
		# An element in set is not inserted if it is
		# already present
		if arr[i] not in s:
			s.add(arr[i])
			
			# Find the position of inserted element
			# Find the next greater element in set
			next_greater = [x for x in s if x > arr[i]]
			
			# If the new element is not inserted at the end, then
			# remove the greater element next to it (This is tricky)
			if next_greater:
				s.remove(min(next_greater))
				
	# Note that set s may not contain actual LIS, but its size gives
	# us the length of LIS
	return len(s)

arr = [8, 9, 12, 10, 11]
print(lis(arr))

# This Code is Contributed by Prasad Kandekar(prasad264)
