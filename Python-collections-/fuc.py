def fun(a,b,*r):
  return( print(a*b,"times %s"%(r)))

x=fun(2,3,[1,2,3,45],2000)
print(x)

