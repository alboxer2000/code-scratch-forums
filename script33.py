G=len
import sys
def A(code,data):
	H=']';F=code;B=data;A=0;D=0;E=[]
	while D<G(F):
		C=F[D]
		if C=='>':
			A+=1
			if A==G(B):B.append(0)
		elif C=='<':A=0 if A<=0 else A-1
		elif C=='+':B[A]=0 if B[A]>=255 else B[A]+1
		elif C=='-':B[A]=255 if B[A]<=0 else B[A]-1
		elif C=='.':sys.stdout.write(chr(B[A]))
		elif C==',':B[A]=ord(sys.stdin.read(1))
		elif C=='[':
			E.append(D)
			if B[A]==0:
				while F[D]!=H:D+=1
		elif C==H:
			if B[A]!=0:D=E[G(E)-1]
			else:E.pop()
		D+=1
def B():B='>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.';A(B,[0]*30000)
if __name__=='__main__':B()
