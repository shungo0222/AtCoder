N = int(input())

num = N % 10

if ((num==2)or(num==4)or(num==5)or(num==7)or(num==9)):
	print('hon')
elif ((num==0)or(num==1)or(num==6)or(num==8)):
	print('pon')
else:
    print('bon')