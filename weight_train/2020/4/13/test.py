import difflib
import pandas as pd


def get_equal_rate(str1, str2):
    if str1 == str2 == 'nan':
        return 0
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

test_use = pd.read_excel(r'D:\Python\Projects\weight_train\data\EMPI_UNIQUE_1000.xls')

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
# print('训练集中准确的样本数量为:\n', example_count)
# print('测试集的分类的样本数量为：\n', test_count)
# # 判断合并记录数与样本数是否一致，比如，不低于90%，则视为基本一致
# if test_count >= example_count*0.9:
#     print('合并记录数与样本数一致')
#     # 获取成功的测试集的匹配因子，Matching_factor，匹配因子
#     Matching_factor = test_use.columns.values.tolist()
# #     获取成功的测试集所使用的权重参数
#     name_weight, gender_weight, birth_weight, \
#     phone_weight, familyAddr_weight, contactPerson_weight \
#         = w1, w2, w3, w4, w5, w6
#     print('成功的匹配因子为：\n', Matching_factor)
#     print('成功的权重参数，以及偏置为')
#     print('姓名权重：', name_weight)
#     print('性别权重：', gender_weight)
#     print('出生日期权重：', birth_weight)
#     print('联系电话权重：', phone_weight)
#     print('现住址权重：', familyAddr_weight)
#     print('联系人姓名权重：', contactPerson_weight)
#     print('偏置：', Bias)
# else:
#     print('合并记录数与样本数不一致，进入增强学习')
# #     利用样本外的诊疗记录，检查合并记录，调整匹配因子


# -----------------------------------------------------------------------------------------------------------------------
