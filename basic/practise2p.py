word = "raghav"
lettersfrequency = {}

for ch in word:

    lettersfrequency[ch] = 1+lettersfrequency.get(ch, 0)

print(lettersfrequency)


for key, value in lettersfrequency.items():
    print(key, value)


# for ch in word:
#     if lettersfrequency.get(ch) == None:
#         lettersfrequency[ch] = 1
#     else:
#         lettersfrequency[ch] = 1+lettersfrequency[ch]

# print(lettersfrequency)


# d={}
# print(type(d))
# d=dict()
# print(type(d))
# print(d)
# d["dhoni"]="Keeper"
# d["kohli"]="batsman"
# print(d)
# print(d["dhoni"])
# print(d["kohli"])
# # print(d["Amitabh"])
# data=d.get("Amitabh",f"Not found")
# print(data)
