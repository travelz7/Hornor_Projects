import pandas as pd
import numpy as np

pd.options.display.max_columns = None
pd.options.display.max_rows = None
np.set_printoptions(threshold=np.inf)


def find_same(dataframe):
    b = dataframe.drop_duplicates(keep=False)
    c = dataframe.drop_duplicates(keep='first')
    d = b.append(c)
    e = d.drop_duplicates(keep=False)
    return e


empi_unique = pd.read_excel(
        io=r'D:\Python\Projects\weight_train\data\EMPI_UNIQUE.xls'
                                )
# 身份证集合
ID_Code = empi_unique['ID_CODE']
# print('ID_Code:\n', ID_Code)
# print('---------------------------------------')
# ID_Code_dropna：有身份证信息的数据
ID_Code_dropna = ID_Code.dropna()
print('有身份证信息的数据:\n', ID_Code_dropna)
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
print('没有身份证，但有居民健康卡的数据：\n', Health_Card_only)
# 医保卡号数据
Med_Card = empi_unique['MED_INSURANCE_CARD']
# 没有身份证，也没有居民健康卡的医保卡数据索引
Med_Card_index = list(set(Health_Card_noID.index) - set(Health_Card_only.index))
# 没有身份证，也没有居民健康卡的医保卡数据
Med_Card_only = Med_Card[Med_Card_index]
# 没有身份证，也没有居民健康卡，但有医保卡的数据
Med_Card_only = Med_Card_only.dropna()
print('没有身份证，没有居民健康卡，但有医保卡的数据：\n', Med_Card_only)

# 找出有身份证信息的重复值，ID_Code_dropna
same_id = find_same(ID_Code_dropna)
same_id_index = list(set(same_id.index))
list_all = []
for same_value_index in same_id_index:
    list = []
    for value_index in ID_Code_dropna_index:
        if same_id[same_value_index] == ID_Code_dropna[value_index]:
            list.append(value_index)
    list_all.append(list)
print('身份证一致的集合索引 list_all：\n', list_all)

# 身份证一致，取出姓名、性别、出生日期关键信息
key_data = empi_unique[['PAT_NAME', 'GENDER_CODE', 'BIRTH_DATE']]
list1 = []
for i in range(len(list_all)):
    list = []
    list = key_data.loc[list_all[i]]
    list1.append(list)
print('身份证一致的关键信息集合 list1:\n', list1)

# 判断关键信息一致性
print('list11111:\n', list1[0]['PAT_NAME'])


