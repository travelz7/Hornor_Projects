def loadDataSet(fileName):
    """
    对文件进行逐行解析，从而得到第行的类标签和整个特征矩阵
    Args:
        fileName 文件名
    Returns:
        dataMat  特征矩阵
        labelMat 类标签
    """
    dataMat = []
    labelMat = []
    fr = open(fileName)
    print(fr)
    for line in fr.readlines():
        lineArr = line.strip().split( )
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

if __name__ == "__main__":
    # 获取特征和目标变量
    dataArr, labelArr = loadDataSet('D:/Python/Projects/6_数据可视化/Data/testSet.txt')


