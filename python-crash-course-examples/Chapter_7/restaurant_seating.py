# Display a message asking the user how many
# people are in their dinner group

groupSize = input("How many people are in your dinner group? ")
groupSize = int(groupSize)

# If the group size is greater than eight, tell
# tell them they would have to wait for a table,
# otherwise tell them their table is ready.

if groupSize > 8: # If the group size is bigger then 8.
	print(f"\nPlease wait to be seated.")
elif groupSize > 0: # If the group size is at least 1 or larger.
	print(f"\nPlease follow me to be seated.")
else: # If the user inputed a size of 0 or lower.
	print(f"\nI do not understand.")