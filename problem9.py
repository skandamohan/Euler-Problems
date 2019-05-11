'''https://projecteuler.net/problem=9'''
'''Please see the README document for details'''

'''a^2+b^2=c^2
a + b + c= 1000
the below is not an optimized solution but it works
'''


def run (sum) :
  for i in range (1,1000):
    for j in range (1,1000):
      for k in range (1,1000):
        if(i + j + k == 1000):
          if ((i**2)+(j**2)==(k**2)) :
            print(i,j,k)




if __name__ == "__main__":
  print ("https://projecteuler.net/problem=9")
