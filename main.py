import json,os,urllib.request as U
Z='PPPPZZZZRRTVQQRUPPPTQONPQRRLPPPPFHJJHLPPJPRSJQSTJPSTJQRSHLPQFHJJLNNNNPPPNPQRNQQRNPRRNRRRNQPPLNNNPPPPQRRROPPPOPPPOPPPOPPPOPPPPPPQLNNONPPPNPQQOPQQPPQQNQQQNPQPLNNOJHHFJHHFJHHFJHHFLJJHNLLLTTPPTVRPNPQSPRSUPSVXPSWYORVXNQTUKKPPIJLM'
T={}
for n,p in enumerate('PNBRQKk'):
 t=[0]*120
 for s in range(64):t[21+s//8*10+s%8]=(100,320,330,500,900,60000,0)[n]+(ord(Z[n*32+s//8*4+min(s%8,7-s%8)])-80)*5
 T[p]=t
D=dict(P=(-10,-20,-11,-9),N=(-21,-19,-8,12,21,19,8,-12),B=(-11,-9,9,11),R=(-10,1,10,-1));D['Q']=D['K']=D['B']+D['R']
u=lambda b,i,p:b[:i]+p+b[i+1:]
def J(b,i):
 if'p'in(b[i-9],b[i-11])or'n'in[b[i+d]for d in D['N']]:return 1
 for n,d in enumerate(D['K']):
  j=i+d
  while b[j]=='.':j+=d
  if b[j]in'q'+'br'[n>3]:return 1
def G(P):
 b,_,w,c,e,k=P
 for i,p in enumerate(b):
  if p in D:
   for d in D[p]:
    j=i+d
    while 1:
     q=b[j]
     if q<'!'or q in D:break
     if p=='P'and(d%10<1 and q!='.'or d==-20 and(i<81 or b[i-10]!='.')or d%10 and q=='.'and j!=e and abs(j-k)>1):break
     yield i,j,'Q'*(p=='P'and j<29)
     if p in'PNK'or q>'Z':break
     if i in(91,98)and b[j+d]=='K'and w[i>91]:yield j+d,j-d,''
     j+=d
def N(P):b,s,w,c,e,k=P;return b[::-1].swapcase(),-s,c,w,119-e,119-k
def V(P,m):
 i,j,r=m;b=P[0];p,q=b[i],b[j];s=T[p][j]-T[p][i]
 if q>'Z':s+=T[q.upper()][119-j]
 if abs(j-P[5])<2:s+=60000
 if p=='K'and abs(i-j)==2:s+=T['R'][(i+j)//2]-T['R'][91+7*(j>i)]
 if r:s+=T[r][j]-T['P'][j]
 if j==P[4]and p=='P':s+=T['P'][109-j]
 return s
def M(P,m,v=0):
 i,j,r=m;b,s,w,c,e,k=P;p=b[i];s+=v or V(P,m);b=u(u(b,j,p),i,'.');w=(w[0]*(i!=91),w[1]*(i!=98));c=(c[0]*(j!=21),c[1]*(j!=28));k=0
 if p=='K':
  w=(0,0)
  if abs(j-i)==2:k=(i+j)//2;b=u(u(b,91+7*(j>i),'.'),k,'R')
 if r:b=u(b,j,r)
 if j==e and p=='P':b=u(b,j+10,'.')
 return N((b,s,w,c,(p=='P')*(i-j==20)*(i-10),k))
def S(P,d,a,b,r):
 global n
 n+=1
 if I>1<n>20000:1/0
 q=P[0]
 if q in R and r:return r%2*40-20
 t=H.get(q)
 if t and t[0]>=d and t[2]*(t[1]-(b if t[2]>0 else a))>=0:return t[1]
 o=a;bm=t and t[3];x=q.find('K');c=J(q,x);e=P[1]
 if c:d=max(d,1)
 elif d==1 and e+200<a:d=0
 if d<1:
  y=q.find('k');w=max(0,14-sum(map(q.count,'NBRQnbrq')));e+=(T['k'][x]-T['k'][119-y])*w//7+(e>200)*(14-abs(x//10-y//10)-abs(x%10-y%10))*w//2
  if e>=b:return e
  a=max(a,e);best=e
 else:
  best=-1e9
  if d>2 and e>=b and not c:
   s=-S(N(P[:4]+(0,0)),d-3,-b,1-b,r+1)
   if s>=b:return s
 for x,(v,m) in enumerate(sorted(((V(P,m),m)for m in(G(P)if r else LM)),key=lambda x:x[0]+(d>0)*((x[1]==bm)*1e5+(x[1]==X[r])*300+Y.get(x[1],0)),reverse=1)):
  if d<1 and v<70:break
  if v>50000:return 60000-r
  p=M(P,m,v);l=x>3 and d>2 and v<70 and not c;s=-S(p,d-1-l,-b,-a,r+1)
  if l and s>a:s=-S(p,d-1,-b,-a,r+1)
  if s>best:best,bm=s,m
  if s>a:a=s
  if a>=b:
   if d>0:X[r]=m;Y[m]=Y.get(m,0)+d*d
   break
 if d>0:
  if best==r+1-60000 and not c:best=0
  H[q]=(d,best,(best>=b)-(best<=o),bm)
 return best
def B(P):
 global n,H,X,Y,I,LM
 LM=[m for m in G(P)for c in[M(P,m)]if not any(V(c,x)>50000 for x in G(c))]
 n=0;H={};X=[0]*999;Y={};m=LM[0]
 for I in range(1,99):
  try:S(P,I,-1e9,1e9,0)
  except:break
  t=H.get(P[0])
  if t and t[3]in LM:m=t[3]
 return m
A=lambda s:ord(s[0])+4-int(s[1])*10
C=lambda i:chr(96+i%10)+str(10-i//10)
def F(f):
 p,t,c,e=f.split()[:4]
 b='\n'*20+''.join(' '+r+'\n'for r in p.split('/'))+'\n'*20
 for x in'12345678':b=b.replace(x,'.'*int(x))
 P=b,sum(T[q][i]if q in D else-T[q.upper()][119-i]for i,q in enumerate(b)if q.isalpha()),('Q'in c,'K'in c),('k'in c,'q'in c),e!='-'and A(e),0
 return N(P)if t=='b'else P
def Q(p,d):return json.load(U.urlopen(U.Request(os.environ['MAKEFUN_ENV_URL'].rstrip('/')+p,json.dumps(d).encode(),{'Content-Type':'application/json'})))
while 1:
 try:g=Q('/game',{});k=g['game']
 except:break
 f=g.get('opening')or'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'
 P=F(f);o=119*(' b 'in f);R=set()
 while 1:
  try:
   R.add(P[0]);m=B(P);P=M(P,m);R.add(P[0]);i,j,r=m
   s=Q('/move',{'game':k,'move':C(abs(o-i))+C(abs(o-j))+r.lower()})['opp_move'];P=M(P,(abs(119-o-A(s[:2])),abs(119-o-A(s[2:4])),s[4:].upper()))
  except:break
