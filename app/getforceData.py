# _*_ coding:utf-8 _*_
# 这是为机床录入实时数据的附带代码
print("lets begin")


f = open(
    "C:\\Users\\admin\\Desktop\\abschlussproject\\getforcetest.txt", mode="r"
)
for each_line in f:
    (mytime, FX, FY, FZ) = each_line.split("\t", 3)
    FZ = FZ[:-1]
    print(FZ)
    print(mytime, FX, FY, FZ)
