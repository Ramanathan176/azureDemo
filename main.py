import pandas as pd


pf = pd.read_csv("data.csv")
pf["Fullname"] = pf["Lastname"] + " " + pf["Firstname"]


def can_vote(age):
    if age >= 21:
        return "Can vote"
    else:
        return "Cannot vote"


pf["Voting_Status"] = pf["Age"].apply(can_vote)
# pf.to_csv("updated_data.csv", index=False)
# pf.to_excel("updated_data.xlsx",index=False)
print(pf)
