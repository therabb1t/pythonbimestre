tabuada=int(input("De qual número vamos gerar a tabuada? : "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
