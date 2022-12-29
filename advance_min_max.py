# numbers=[4,5,6,2,3,1,4,5,2,5,8,4,14,1,2,5,8,8,4,1,1,25,5,58,47,1,5,5,5,8,21,14,4]
# print(max(numbers))
names=["ankit","messi","einstein","bieber","raj","utsab"]
# how we can calculate which word have the maximum length with max function
# sabse phele normally
def func(item):
    return len(item)

print(max(names,key = func))
# yaha hua kya??? names ke elements ko func mai dal ke nayee kist banaye or uska max nikal ke usko correpondence mai names mai se value de di

dict1={
    "ankit":{"math":99,"science":78},
    "soham":{"math":200,"science":100},
    "raj":{"math":45,"science":56},
    "utsab":{"math":56,"science":55},
    "bieber":{"math":69,"science":69}
}
print(max(dict1,key=lambda x:dict1[x]["science"]))
print(max(dict1,key=lambda x:dict1[x]["math"]))
print(min(dict1,key=lambda x:dict1[x]["science"]))
print(min(dict1,key=lambda x:dict1[x]["math"]))
