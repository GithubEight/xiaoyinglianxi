print("这是一个判断学生成绩是否合格的程序",end='\n')
score=input("请输入学生的分数:")
s=float(score)
if (s>=60 and s<=100):
    print("恭喜你")
elif (s>0 and s<60):
    print("很遗憾")
else:
    print("您输入的成绩不正确")
