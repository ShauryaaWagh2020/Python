# Assuming Tina intended:
#  x=3, y=5, z=7
# But mistakenly did:
x, y, z = 7,3,5 # Incorrect order

print("Before:\nIncorrect Order: x=",{x},"y=",{y}, "z=",{z})

# Correcting the order:
# We want x=3, y=5, z=7
# # Based on current values: y=3, z=5, x=7
x, y, z = y, z, x

print("After:\nCorrect Order: x=",{x}," y=",{y}," z=",{z})