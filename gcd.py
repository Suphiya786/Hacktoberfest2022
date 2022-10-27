# Python3 program to demonstrate Basic Euclidean Algorithm


# Function to return gcd of a and b
def gcd(a, b):
	if a == 0:
		return b

	return gcd(b % a, a)

# Driver code
if __name__ == "__main__":
a = int(input())
b = int(input())
print("gcd(", a, ",", b, ") = ", gcd(a, b))
