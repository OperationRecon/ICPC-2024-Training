n = int(input())
spots = 2*n-2
p = ((n-3))*(4*pow(4,spots-(n+2))*pow(3,2))+(2*4*pow(4,spots-(n+1))*pow(3,1))
print(int(p))