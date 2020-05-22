import pandas as pd
import numpy as np
import difflib

# 显示所有行，列
pd.options.display.max_columns = None
pd.options.display.max_rows = None
np.set_printoptions(threshold=np.inf)

# ---------------------------------------------------------------------------------------
# 数据初始化
test_all = pd.DataFrame()
example_count = 0
train_counts = 0
list_classification = []
print('类型：\n', list_classification)
w1 = 0.6
w2 = 0.5
w3 = 0.3
w4 = 0.2
w5 = 0.1
w6 = 0.1
#  偏置初始化
# 通常偏置项初始化为0，或比较小的数，如：0.01

# 将偏差初始化为零是可能的，也是很常见的，因为非对称性破坏是由权重的小随机数导致的。
# 因为ReLU具有非线性特点，所以有些人喜欢使用将所有的偏差设定为小的常数值如0.01，
# 因为这样可以确保所有的ReLU单元在最开始就激活触发(fire)并因此能够获得和传播一些梯度值。
# 然而，这是否能够提供持续的改善还不太清楚(实际上一些结果表明这样做反而使得性能更加糟糕)，
# 所以更通常的做法是简单地将偏差初始化为0.
Bias = 0.1
aim_output = 1
# 这里的 eta 表示学习率，一般取 0~1 之间的值。
# eta 值越大学习速率也越快，也就是每一次训练，权值和偏置的变动越大，但也并不是越大越好。
# 如果 eta 过大容易产生震荡而不能稳定到目标值，若 eta 值越小，则效果相反。这里我们简单的取 eta=1
eta = 1

# ---------------------------------------------------------------------------------------


# 获取重复值
def find_same(dataframe):
    b = dataframe.drop_duplicates(keep=False)
    c = dataframe.drop_duplicates(keep='first')
    d = b.append(c)
    e = d.drop_duplicates(keep=False)
    return e


# 获取相似度
def get_equal_rate(str1, str2):
    if str1 == str2 == 'nan':
        return 0
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


# --------------------------------------------------------------------------------------------------------------------------
# 训练函数
def train(test_use, i, j):
    name_ratio = get_equal_rate(test_use['PAT_NAME'][i], test_use['PAT_NAME'][j])
    # print('姓名相似度：\n', name_ratio)
    sex_ratio = get_equal_rate(str(test_use['GENDER_CODE'][i]), str(test_use['GENDER_CODE'][j]))
    # print('性别相似度：\n', sex_ratio)
    birth_ratio = get_equal_rate(str(test_use['BIRTH_DATE'][i]), str(test_use['BIRTH_DATE'][j]))
    # print('出生日期相似度：\n', birth_ratio)
    phone_ratio = get_equal_rate(str(test_use['MOBILE_NUM'][i]), str(test_use['MOBILE_NUM'][j]))
    # print('手机号码相似度：\n', phone_ratio)
    faminlyAddr_ratio = get_equal_rate(str(test_use['FAMILY_ADDR'][i]), str(test_use['FAMILY_ADDR'][j]))
    # print('家庭住址相似度：\n', faminlyAddr_ratio)
    contactPerson_ratio = get_equal_rate(str(test_use['CONTACT_PERSON_NAME'][i]), str(test_use['CONTACT_PERSON_NAME'][j]))
    # print('联系人姓名相似度：\n', contactPerson_ratio)

    x1 = name_ratio
    x2 = sex_ratio
    x3 = birth_ratio
    x4 = phone_ratio
    x5 = faminlyAddr_ratio
    x6 = contactPerson_ratio

    global w1
    global w2
    global w3
    global w4
    global w5
    global w6
    global Bias
    global train_counts

    train_counts += 1

    z = x1*w1 + x2*w2 + x3*w3 + x4*w4 + x5*w5 + x6*w6 + Bias
    real_output = np.tanh(z)
    err = aim_output - real_output
    # print('误差：\n', err)
    w1 = w1 + eta*err*x1
    w2 = w2 + eta*err*x2
    w3 = w3 + eta*err*x3
    w4 = w4 + eta*err*x4
    w5 = w5 + eta*err*x5
    w6 = w6 + eta*err*x6
    Bias = Bias + eta*err
    print('修正', train_counts, '次过后的权值和偏置：\n', w1, w2, w3, w4, w5, w6, Bias)
    z = x1*w1 + x2*w2 + x3*w3 + x4*w4 + x5*w5 + x6*w6 + Bias
    real_output = np.tanh(z)
    err = aim_output - real_output
    print('训练', train_counts, '次后的误差：\n', err)

    # if real_output > 0.9:
    #     print('合并该两条记录')
# --------------------------------------------------------------------------------------------------------------------------


empi_unique = pd.read_excel(
        io=r'D:\Python\Projects\weight_train\data\EMPI_UNIQUE.xls'
                                )
# 身份证集合
ID_Code = empi_unique['ID_CODE']
# print('ID_Code:\n', ID_Code)
# print('---------------------------------------')
# ID_Code_dropna：有身份证信息的数据
ID_Code_dropna = ID_Code.dropna()
# print('有身份证信息的数据:\n', ID_Code_dropna)
# ID_Code_dropna_index：有身份证的索引
ID_Code_dropna_index = list(ID_Code_dropna.index)
# print('有身份证的索引：\n', ID_Code_dropna_index)
# ID_Code_no_index：没有身份证的索引
ID_Code_no_index = list(set(ID_Code.index) - set(ID_Code_dropna_index))
# print('没有身份证的索引：\n', ID_Code_no_index)
# ID_Code_na：没有身份证信息的数据
ID_Code_na = ID_Code[ID_Code_no_index]
# print('没有身份证信息的数据：\n', ID_Code_na)
# 居民健康卡数据
Health_Card = empi_unique['HEALTH_CARD']
# 没有身份证的居民健康卡的数据
Health_Card_noID = Health_Card[ID_Code_no_index]
# 没有身份证，但有居民健康卡的数据
Health_Card_only = Health_Card_noID.dropna()
# print('没有身份证，但有居民健康卡的数据：\n', Health_Card_only)
Health_Card_only_index = list(Health_Card_only.index)
# 医保卡号数据
Med_Card = empi_unique['MED_INSURANCE_CARD']
# 没有身份证，也没有居民健康卡的医保卡数据索引
Med_Card_index = list(set(Health_Card_noID.index) - set(Health_Card_only.index))
# 没有身份证，也没有居民健康卡的医保卡数据
Med_Card_only = Med_Card[Med_Card_index]
# 没有身份证，也没有居民健康卡，但有医保卡的数据
Med_Card_only = Med_Card_only.dropna()
# print('没有身份证，没有居民健康卡，但有医保卡的数据：\n', Med_Card_only)
Med_Card_only_index = list(Med_Card_only.index)


# 找出有身份证信息的重复值，ID_Code_dropna
same_id = find_same(ID_Code_dropna)
same_id_index = list(set(same_id.index))
list_all = []
for same_value_index in same_id_index:
    list_sameID = []
    for value_index in ID_Code_dropna_index:
        if same_id[same_value_index] == ID_Code_dropna[value_index]:
            list_sameID.append(value_index)
    list_all.append(list_sameID)
# print('身份证一致的集合索引 list_all：\n', list_all)

# 身份证一致，取出姓名、性别、出生日期关键信息
key_data = empi_unique[['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE']]
list_sameID_key = []
for i in range(len(list_all)):
    list_sameID_key_one = []
    list_sameID_key_one = key_data.loc[list_all[i]]
    list_sameID_key.append(list_sameID_key_one)
print('身份证一致的关键信息集合 list_sameID_key:\n', list_sameID_key)
print('list_sameID_key的类型：', type(list_sameID_key))

# 判断关键信息一致性
# print('list11111:\n', list1[0]['PAT_NAME'])
# print('list1的长度：\n', len(list1))
# 判断姓名是否一致
for i in list_sameID_key:
    data_ID = pd.DataFrame()
    name_dup = i['PAT_NAME'].duplicated()
    name_false_count = 0
    for j in name_dup:
        if j == False:
            name_false_count = name_false_count + 1
    if name_false_count < 2:
        # print('姓名一致')
    #     判断性别是否一致
        sex_dup = i['GENDER_CODE'].duplicated()
        sex_false_count = 0
        for j in sex_dup:
            if j == False:
                sex_false_count = sex_false_count + 1
        if sex_false_count < 2:
            # print('姓名，性别一致')
        #     判断出生日期是否一致
            birth_dup = i['BIRTH_DATE'].duplicated()
            birth_false_count = 0
            for j in birth_dup:
                if j == False:
                    birth_false_count = birth_false_count + 1
            if birth_false_count < 2:
                # print('姓名，性别，出生日期一致')
                # i就是一个训练集
                i_index = list(i.index)
                print('训练集i的索引：\n', i_index)
                data_ID = data_ID.append(i)
                data_ID_index = list(data_ID.index)
                test_use = empi_unique[
                    ['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE', 'MOBILE_NUM', 'FAMILY_ADDR', 'CONTACT_PERSON_NAME']].loc[data_ID_index]
                # print('机器学习使用的训练集：\n', test_use)
                for m in i_index:
                    for n in i_index:
                        if m == n:
                            continue
                        train(test_use, m, n)
                test_all = test_all.append(i)
                example_count += 1
            else:
                continue
                # print('姓名，性别一致，出生日期不一致')
        else:
            continue
            # print('姓名一致，性别不一致')
    else:
        continue
        # print('姓名不一致')


# 找出有居民健康卡号的重复值，Health_Card_only
same_HealthCard = find_same(Health_Card_only)
same_HealthCard_index = list(set(same_HealthCard.index))
list_all_health = []
for same_value_index in same_HealthCard_index:
    list_same_HealthCard = []
    for value_index in Health_Card_only_index:
        if same_HealthCard[same_value_index] == Health_Card_only[value_index]:
            list_same_HealthCard.append(value_index)
    list_all_health.append(list_same_HealthCard)
# print('居民健康卡号一致的集合索引 list_all_health：\n', list_all_health)

# 居民健康卡号一致，取出姓名、性别、出生日期关键信息
key_data = empi_unique[['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE']]
list_same_HealthCard_key = []
for i in range(len(list_all_health)):
    list_same_HealthCard_key_one = []
    list_same_HealthCard_key_one = key_data.loc[list_all_health[i]]
    list_same_HealthCard_key.append(list_same_HealthCard_key_one)
# print('居民健康卡号一致的关键信息集合 list_same_HealthCard_key:\n', list_same_HealthCard_key)

# 判断关键信息一致性
# print('list11111:\n', list1[0]['PAT_NAME'])
# print('list1的长度：\n', len(list1))
# 判断姓名是否一致
for i in list_same_HealthCard_key:
    name_dup = i['PAT_NAME'].duplicated()
    name_false_count = 0
    for j in name_dup:
        if j == False:
            name_false_count = name_false_count + 1
    if name_false_count < 2:
        # print('姓名一致')
    #     判断性别是否一致
        sex_dup = i['GENDER_CODE'].duplicated()
        sex_false_count = 0
        for j in sex_dup:
            if j == False:
                sex_false_count = sex_false_count + 1
        if sex_false_count < 2:
            # print('姓名，性别一致')
        #     判断出生日期是否一致
            birth_dup = i['BIRTH_DATE'].duplicated()
            birth_false_count = 0
            for j in birth_dup:
                if j == False:
                    birth_false_count = birth_false_count + 1
            if birth_false_count < 2:
                # print('姓名，性别，出生日期一致')
                # i就是一个训练集
                i_index = list(i.index)
                print('训练集i的索引：\n', i_index)
                data_ID = data_ID.append(i)
                data_ID_index = list(data_ID.index)
                test_use = empi_unique[
                    ['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE', 'MOBILE_NUM', 'FAMILY_ADDR', 'CONTACT_PERSON_NAME']].loc[
                    data_ID_index]
                # print('机器学习使用的训练集：\n', test_use)
                for m in i_index:
                    for n in i_index:
                        if m == n:
                            continue
                        train(test_use, m, n)
                test_all = test_all.append(i)
                example_count += 1
            else:
                continue
                # print('姓名，性别一致，出生日期不一致')
        else:
            continue
            # print('姓名一致，性别不一致')
    else:
        continue
        # print('姓名不一致')


# 找出有医保卡号的重复值，Med_Card_only
same_Med_Card = find_same(Med_Card_only)
same_Med_Card_index = list(set(same_Med_Card.index))
list_all_Med_Card = []
for same_value_index in same_Med_Card_index:
    list_same_Med_Card = []
    for value_index in Med_Card_only_index:
        if same_Med_Card[same_value_index] == Med_Card_only[value_index]:
            list_same_Med_Card.append(value_index)
    list_all_Med_Card.append(list_same_Med_Card)
# print('居民健康卡号一致的集合索引 list_all_Med_Card：\n', list_all_Med_Card)

# 居民医保卡号一致，取出姓名、性别、出生日期关键信息
key_data = empi_unique[['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE']]
list_same_Med_Card_key = []
for i in range(len(list_all_Med_Card)):
    list_same_Med_Card_key_one = []
    list_same_Med_Card_key_one = key_data.loc[list_all_Med_Card[i]]
    list_same_Med_Card_key.append(list_same_Med_Card_key_one)
# print('居民健康卡号一致的关键信息集合 list_same_Med_Card_key:\n', list_same_Med_Card_key)

# 判断关键信息一致性
# print('list11111:\n', list1[0]['PAT_NAME'])
# print('list1的长度：\n', len(list1))
# 判断姓名是否一致
for i in list_same_Med_Card_key:
    name_dup = i['PAT_NAME'].duplicated()
    name_false_count = 0
    for j in name_dup:
        if j == False:
            name_false_count = name_false_count + 1
    if name_false_count < 2:
        # print('姓名一致')
    #     判断性别是否一致
        sex_dup = i['GENDER_CODE'].duplicated()
        sex_false_count = 0
        for j in sex_dup:
            if j == False:
                sex_false_count = sex_false_count + 1
        if sex_false_count < 2:
            # print('姓名，性别一致')
        #     判断出生日期是否一致
            birth_dup = i['BIRTH_DATE'].duplicated()
            birth_false_count = 0
            for j in birth_dup:
                if j == False:
                    birth_false_count = birth_false_count + 1
            if birth_false_count < 2:
                # print('姓名，性别，出生日期一致')
                # i就是一个训练集
                i_index = list(i.index)
                print('训练集i的索引：\n', i_index)
                data_ID = data_ID.append(i)
                data_ID_index = list(data_ID.index)
                test_use = empi_unique[
                    ['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE', 'MOBILE_NUM', 'FAMILY_ADDR', 'CONTACT_PERSON_NAME']].loc[
                    data_ID_index]
                # print('机器学习使用的训练集：\n', test_use)
                for m in i_index:
                    for n in i_index:
                        if m == n:
                            continue
                        train(test_use, m, n)
                test_all = test_all.append(i)
                example_count += 1
            else:
                continue
                # print('姓名，性别一致，出生日期不一致')
        else:
            continue
            # print('姓名一致，性别不一致')
    else:
        continue
        # print('姓名不一致')
# print('test:\n', test_all)
print('样本总量:\n', example_count)
test_all_index = list(test_all.index)
# print('训练集索引：\n', test_all_index)
test_use = empi_unique[['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE', 'MOBILE_NUM', 'FAMILY_ADDR', 'CONTACT_PERSON_NAME']].loc[test_all_index]
print('总训练集：\n', test_use)
# print('训练集类型：\n', type(test_use))

# -----------------------------------------------------------------------------------------------------------------------
# 双循环
# 复制一个测试集
test_use_copy = test_use.copy(deep=True)
# count来计数比较次数
test_count = 0
# list_classification用来保存分类结果，序列中每一个元素都是一个DataFrame，这个DataFrame里面保存了信息相似度大于90%的同一类数据
list_classification = []
for index_i, row_i in test_use.iterrows():
    classification = pd.DataFrame()
    for index_j, row_j in test_use_copy.iterrows():
        name_ratio = get_equal_rate(test_use['PAT_NAME'][index_i], test_use_copy['PAT_NAME'][index_j])
        sex_ratio = get_equal_rate(str(test_use['GENDER_CODE'][index_i]), str(test_use_copy['GENDER_CODE'][index_j]))
        birth_ratio = get_equal_rate(str(test_use['BIRTH_DATE'][index_i]), str(test_use_copy['BIRTH_DATE'][index_j]))
        phone_ratio = get_equal_rate(str(test_use['MOBILE_NUM'][index_i]), str(test_use_copy['MOBILE_NUM'][index_j]))
        familyAddr_ratio = get_equal_rate(str(test_use['FAMILY_ADDR'][index_i]), str(test_use_copy['FAMILY_ADDR'][index_j]))
        contactPerson_ratio = get_equal_rate(str(test_use['CONTACT_PERSON_NAME'][index_i]), str(test_use_copy['CONTACT_PERSON_NAME'][index_j]))

        x1 = name_ratio
        x2 = sex_ratio
        x3 = birth_ratio
        x4 = phone_ratio
        x5 = familyAddr_ratio
        x6 = contactPerson_ratio

        z = x1*w1*0.3333 + x2*w2*0.2778 + x3*w3*0.1667 + x4*w4*0.1111 + x5*w5*0.0556 + x6*w6*0.0556 + Bias
        # print('检验概率：\n', z)
        if(z > 0.9):
            classification = classification.append(row_j)
            test_use_copy = test_use_copy.drop([index_j])
    if classification.empty != True:
        test_count += 1
        list_classification.append(classification)
print('最后的分类结果list_classification:\n', list_classification)
print('训练集中准确的样本数量为:\n', example_count)
print('测试集的分类的样本数量为：\n', test_count)
# 判断合并记录数与样本数是否一致，比如，不低于90%，则视为基本一致
if test_count >= example_count*0.9:
    print('合并记录数与样本数一致')
    # 获取成功的测试集的匹配因子，Matching_factor，匹配因子
    Matching_factor = test_use.columns.values.tolist()
#     获取成功的测试集所使用的权重参数
    name_weight, gender_weight, birth_weight, \
    phone_weight, familyAddr_weight, contactPerson_weight \
        = w1, w2, w3, w4, w5, w6
    print('成功的匹配因子为：\n', Matching_factor)
    print('成功的权重参数，以及偏置为')
    print('姓名权重：', name_weight)
    print('性别权重：', gender_weight)
    print('出生日期权重：', birth_weight)
    print('联系电话权重：', phone_weight)
    print('现住址权重：', familyAddr_weight)
    print('联系人姓名权重：', contactPerson_weight)
    print('偏置：', Bias)
else:
    print('合并记录数与样本数不一致，进入增强学习')
#     利用样本外的诊疗记录，检查合并记录，调整匹配因子


# -----------------------------------------------------------------------------------------------------------------------


