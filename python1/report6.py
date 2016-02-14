import re,sys,operator,math
flag=0
size=0
elements=[]
node={}
mul={"p":1e-12, "n":1e-9, "u":1e-6, "m":1e-3, "k":1e3, "meg":1e6}
def getValue(val=''):
        v=0.0
        l=re.match("(^[+-]?[0-9]+)([\.][0-9]+)?([e][+-]?[0-9]+)?([a-z]*)?",val).groups()
        if l[1]==None:
                v=float(l[0])
        else :
                v=float(''.join(l[:2]))
        if l[2]!=None:
                v *= math.pow(10,float(l[2][1:]))
        if l[3]=='':
                return v
        else:
                if mul.has_key(l[3]):
                        return v*mul[l[3]]
                else :
                        print 'Invalid Multiplier'
                        sys.exit(0)
def insertDict(a=''):
        global size
        if node.has_key(a)==False:
                if a=='0' or a=='GND':
                        node[a]=0
                        return
                node[a]=size+1
                size=size+1
f = open(sys.argv[1], 'r')
for line in f:
    if line.lower()=='.circuit\n':
        flag=1
        continue
    elif flag==0:
        continue
    elif line.lower()=='.end\n':
        break
    if line[0]=='*' or line[0]=='\n' or line[0]=='#' or line[0]=='.':
        continue
    line = line[:-1].split('#')[0]
    l = line.split(' ')[:4]
    if len(l)!=4:
        print 'Error'
        sys.exit(0)
    insertDict(l[1])
    insertDict(l[2])
    elements.append(l)
    print line
print 'Reconstructed Listing'
for x in elements:
    x[3]=str(getValue(x[3]))
    print x[0]+' '+str(node[x[1]])+' '+str(node[x[2]])+' '+x[3]
print 'List of Nodes'

for (key,val) in sorted(node.items(), key=operator.itemgetter(1)):
        print str(val)+':'+key
