using ITensors

a = Index(2)
b = Index(2)
c = Index(2)

Z = ITensor(a,b)
X = ITensor(c,b)

Z[a=>1,b=>1] =  1.0
Z[a=>2,b=>2] = -1.0

X[b=>1,c=>2] = 1.0
X[b=>2,c=>1] = 1.0

# The * operator finds and
# contracts common index 'b'
# regardless of index order:

R = Z * X

@show R[a=>2,c=>1]
