# =====================================REGULAR EXPRESSIONS========================================

# ==============FINDALL AND m\w\w==============
import re
str='Amazon america pradip hello a'
result = re.findall(r'a\w\w',str)
print(result)

# =================SPLIT METHOD IN REGXX===============
str='Amazon/america: pradip# hello$ a'
result = re.split(r'\W+',str)
print(result)

# ====================SEQUENCES CHARACTERS=================

# ============FIND WORD===========
str='Amazon america pradip hello a'
result=re.findall(r'a[\w]*',str)
print(result)

str='Amazon america pradip hello a'
result=re.findall(r'\ba[\w]*\b',str)
print(result)

# ============= FIND DIGIT ==================
str='Amazon america 1st and 2nd and 3rd pradip hello a'
result=re.findall(r'\d[\w]*',str)
print(result)

# =============== SEARCH_ _ _GROUP METHOD ===============
str='Amazon america 1st and 2nd pradi and 3rd hello 4 46 7  pradip hello a'
result=re.findall(r'\b\w{5}\b',str)
result=re.findall(r'\b\w{4,}\b',str)
result=re.findall(r'\b\d+\b',str)
print(result)

str='Amazon america 1st and 2nd pradi and 3rd hello pradip hello a'
result=re.search(r'\b\w{5}\b',str)
print(result.group())

# ======================= QUANTIFIERS IN REGEX ======================

# *,+,?,{m}
str='Amazon america 1st and 2nd ant akl abc and 3rd 3 45 6777 pradip hello a'
result=re.findall(r'a[nk][\w]*',str)
print(result)

# =========================SPECIAL CHARACTERS IN REGEX=======================

str='Amazon america pradip he hemn hejkf hello a'
result=re.findall(r"^am",str,re.IGNORECASE)
if result:
    print("yes")
else:
    print("no") 


str='Amazon america pradip he hemn hejkf Hello'
result=re.findall(r"hello$",str,re.IGNORECASE)
if result:
    print("yes")
else:
    print("no")

str='Amazon america pradip he4 5 6 7 8 890 78 hemn hejkf Hello'
result=re.findall(r'[A-Z][a-z]*',str)
print(result)  

# ==================REGEX ON THE FILE================
f=open('gmail.txt','r')
for line in f:
    res=re.findall(r'\S+@\S+',line)
    if len(res)>0:
        print(res)
f.close()       