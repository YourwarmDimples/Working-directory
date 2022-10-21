import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(
    r"F:\打工人\10.18_citiation\data\Table_1_Authors_career_2021_pubs_since_1788_wopp_extracted_202209.xlsx",
    sheet_name="Data")
data_list = data.values.tolist()

field = ["Applied Sciences", "Arts & Humanities", "Economic & Social Sciences", "Health Sciences", "Natural Sciences"]

subfield = ["Agriculture, Fisheries & Forestry", "Built Environment & Design", "Enabling & Strategic Technologies",
            "Engineering", "Information & Communication Technologies", "Communication & Textual Studies",
            "Historical Studies", "Philosophy & Theology", "Visual & Performing Arts", "Social Sciences",
            "Biomedical Research", "Clinical Medicine", "Psychology & Cognitive Sciences",
            "Public Health & Health Services", "Biology", "Chemistry", "Earth & Environmental Sciences",
            "Mathematics & Statistics", "Physics & Astronomy", "Economics & Business", "Unassigned"]

'''
这个逻辑如何：需求=>研究活动热度=>论文引用率高低=>学者总体排名=>学科比较
如果设计出一个简单参数 就更好
各学科之间的比较可以分三类：（1）全球比较（2）中美比较（3）国内比较
'''

# h = data["h21 (ns)"].values.tolist()
# hm = data["hm21 (ns)"].values.tolist()
# c_score = data["c (ns)"].values.tolist()
field_name = data["sm-field"].values.tolist()  # 里面代表的是sub-field

Agriculture = []
Built = []
Enabling = []
Engineering = []
Information = []
Communication = []
Historical = []
Philosophy = []
Visual = []
Social = []
Biomedical = []
Clinical = []
Psychology = []
Public = []
Biology = []
Chemistry = []
Earth = []
Mathematics = []
physics = []
Economics = []
Unassigned = []

# data_list[i][41] 代表sub-field
for item in subfield:
    for value in data_list:
        if value[41] == item:
            index = subfield.index(item)
            if index == 0:
                Agriculture.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 1:
                Built.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 2:
                Enabling.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 3:
                Engineering.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 4:
                Information.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 5:
                Communication.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 6:
                Historical.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 7:
                Philosophy.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 8:
                Visual.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 9:
                Social.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 10:
                Biomedical.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 11:
                Clinical.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 12:
                Psychology.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 13:
                Public.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 14:
                Biology.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 15:
                Chemistry.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 16:
                Earth.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 17:
                Mathematics.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 18:
                physics.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            elif index == 19:
                Economics.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score
            else:
                Unassigned.append([value[6], value[8], value[9], value[16]])  # h, hm, c_score

Agriculture = np.array(Agriculture)
Built = np.array(Built)
Enabling = np.array(Enabling)
Engineering = np.array(Engineering)
Information = np.array(Information)
Communication = np.array(Communication)
Historical = np.array(Historical)
Philosophy = np.array(Philosophy)
Visual = np.array(Visual)
Social = np.array(Social)
Biomedical = np.array(Biomedical)
Clinical = np.array(Clinical)
Psychology = np.array(Psychology)
Public = np.array(Public)
Biology = np.array(Biology)
Chemistry = np.array(Chemistry)
Earth = np.array(Earth)
Mathematics = np.array(Mathematics)
physics = np.array(physics)
Economics = np.array(Economics)
Unassigned = np.array(Unassigned)

'''
# 绘制 h-value
for index in range(len(subfield)):
    if index == 0:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Agriculture[:, 0], Agriculture[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 1:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Built[:, 0], Built[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 2:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Enabling[:, 0], Enabling[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 3:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Engineering[:, 0], Engineering[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 4:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Information[:, 0], Information[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 5:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Communication[:, 0], Communication[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 6:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Historical[:, 0], Historical[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 7:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Philosophy[:, 0], Philosophy[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 8:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Visual[:, 0], Visual[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 9:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Social[:, 0], Social[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 10:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Biomedical[:, 0], Biomedical[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 11:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Clinical[:, 0], Clinical[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 12:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Psychology[:, 0], Psychology[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 13:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Public[:, 0], Public[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 14:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Biology[:, 0], Biology[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 15:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Chemistry[:, 0], Chemistry[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 16:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Earth[:, 0], Earth[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 17:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Mathematics[:, 0], Mathematics[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 18:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(physics[:, 0], physics[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    elif index == 19:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Economics[:, 0], Economics[:, 1])
        plt.xlabel("Rank")
        plt.ylabel("h-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\h\{}.png".format(subfield[index]))
    else:
        pass
'''

'''
# 绘制 c-score

for index in range(len(subfield)):
    if index == 0:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Agriculture[:, 0], Agriculture[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 1:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Built[:, 0], Built[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 2:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Enabling[:, 0], Enabling[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 3:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Engineering[:, 0], Engineering[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 4:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Information[:, 0], Information[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 5:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Communication[:, 0], Communication[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 6:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Historical[:, 0], Historical[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 7:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Philosophy[:, 0], Philosophy[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 8:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Visual[:, 0], Visual[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 9:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Social[:, 0], Social[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 10:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Biomedical[:, 0], Biomedical[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 11:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Clinical[:, 0], Clinical[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 12:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Psychology[:, 0], Psychology[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 13:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Public[:, 0], Public[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 14:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Biology[:, 0], Biology[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 15:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Chemistry[:, 0], Chemistry[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 16:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Earth[:, 0], Earth[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 17:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Mathematics[:, 0], Mathematics[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 18:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(physics[:, 0], physics[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    elif index == 19:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Economics[:, 0], Economics[:, 2])
        plt.xlabel("Rank")
        plt.ylabel("hm-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\hm\{}.png".format(subfield[index]))
    else:
        pass
'''

# 绘制 hm-value
for index in range(len(subfield)):
    if index == 0:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Agriculture[:, 0], Agriculture[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 1:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Built[:, 0], Built[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 2:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Enabling[:, 0], Enabling[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 3:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Engineering[:, 0], Engineering[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 4:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Information[:, 0], Information[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 5:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Communication[:, 0], Communication[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 6:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Historical[:, 0], Historical[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 7:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Philosophy[:, 0], Philosophy[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 8:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Visual[:, 0], Visual[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 9:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Social[:, 0], Social[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 10:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Biomedical[:, 0], Biomedical[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 11:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Clinical[:, 0], Clinical[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 12:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Psychology[:, 0], Psychology[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 13:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Public[:, 0], Public[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 14:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Biology[:, 0], Biology[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 15:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Chemistry[:, 0], Chemistry[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 16:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Earth[:, 0], Earth[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 17:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Mathematics[:, 0], Mathematics[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 18:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(physics[:, 0], physics[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    elif index == 19:
        plt.figure(figsize=(20, 8), dpi=300)
        plt.scatter(Economics[:, 0], Economics[:, 3])
        plt.xlabel("Rank")
        plt.ylabel("c-score-value")
        plt.title("The distribution of data in {} is show in the plot".format(subfield[index]))
        plt.savefig(r"F:\Working directory\c-score\{}.png".format(subfield[index]))
    else:
        pass
