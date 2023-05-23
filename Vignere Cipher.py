from __future__ import division
import string
import numpy as np
#left shift function
def shift(list_1,num_1):
return list_1[num_1:] + list_1[:num_1]
num_dict = dict(zip(range(0,26),string.ascii_lowercase))
# for reverse mapping: numbers to letter
alpha_percent = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,
                 0.06966,0.00153,0.00772,0. 04025,0.02406,0.06749,0.07507,0.01929,
                 0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02 36,0.0015,
                 0.01974,0.00074]
alpha1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ciphertext = 'IACIOIPNKXXRMQOWAMUOPKDYXVBCXWAUZATPTEDOAXZRVTECEUTAASCYYV MLMOZAXIPRMMBXENNIYSZRDOGPWBFQGKOHTPXAMAOWYJISOMKQILWMMLM LQMZSVRVJKSIQOWISTNILHVABHMMLQABTBOMGCIMXCCKMGGMFCWHOPRMPX ELUZKHYTQIBPMBUJCMTIFNXHVBFVVWXPVIOLFMFDLXWQIZAXIVGCIMQIAWWK MAFJUXXPVIOLMVPZPXHQAZLPMBUHZLZIAYMFIGRMTTWBADOAXUENEASQSJZZ SBBAKHYZFZGHYLBIBDRWJVTEXPNOQFPQFOMGMVTNIBHRHGQNWIAYOTZMIZV MXWUDAYEDBPZBXMRSXKIAFDWGTCGHMPMAROCITMAXMMLMEZCISVEZTTXM QOPXIDRIBLSNGCMEEAGOEHHILNRNPQHNA TWBBIQLLURIBTRLNYUBVIGDWGAMEZCGFWHILXHJHGTRJWETWNJIAXGRSCNHMGMIYDBCYAGOQVOTRNUXXWQZIML BUZVAIIQYMWWMEDWNWTLWCMWILIWPMLBIBEMSRDBFMAFOCITMAXMBWCEZ LHRBLJCKIRHNBTWXYPKDCIFOPXCUNFMXQJHOQPMAUTWNHSRZXKMOUOWNXW SOPBWBUZAXGZBJSLAMEZCIEONDVLXEBPTWEAFJWGGZBVSTKQEGILEUNIIGCLN TLHCWHOPBRSVHIYVIVYATMLGPXIIVPZQGHQTIIGXTLQIEMIAOTRVMCMMLWQA BUXQWEDMLSNGCMLXMRGGZPQGOMKMVZMAOEVQZUXCMENMRIAVNIBHJRAW KIGBPEXVMQVZGILCGCVOGOPBMLIGYWXWVGVTMIZSVKMWWUWWMLMEHMLE QQOCITMAXMBQXNOQXRBYTTXXAGCQGOIOJCMAPNOKTRPNQMAEXCZVXHBBO WFQGVQMPVQGOMGXWZMKTVBRMIUSCGDBLLMNYLXHIAYBHPLUDUMLMTDAM SNUZZEIBGZZ'
ciphertext= ciphertext.lower() ciphertext=list(ciphertext) ciphertext1=ciphertext coinc_list=[]
iter1=1
#Finding coincidences using Kerckhoff’s method while iter1<=30:
count = 0
for j in range(iter1,(len(ciphertext))):
if ciphertext[j-iter1] == ciphertext[j]: count+=1
if iter1 >= 2 and iter1 <= 30:
print ('No: of coincidences after',iter1,'shift :',count)
coinc_list.append(count)
iter1+=1
max_1=max(coinc_list)
print ('\n Maximum no: of coincidence(max_1):',max_1) max_1=coinc_list.index(max_1)
max_1+=1
max_2=sorted(set(coinc_list))[-2]
print ('2nd highest no: of coincidence(max_2):',max_2) max_2=coinc_list.index(max_2)
max_2+=1
max_3=sorted(set(coinc_list))[-3]
print ('3rd highest no: of coincidence:(max_3)',max_3)
max_3=coinc_list.index(max_3)
max_3+=1
max_4=sorted(set(coinc_list))[-4]
print ('4th highest no: of coincidence:(max_4)',max_4)
max_4=coinc_list.index(max_4)
max_4+=1
max_5=sorted(set(coinc_list))[-5]
print ('5th highest no: of coincidence(max_6):',max_5)
max_5=coinc_list.index(max_5)
max_5+=1
max_6=sorted(set(coinc_list))[-6]
print ('6th highest no: of coincidence:(max_6)',max_6)
max_6=coinc_list.index(max_6)
max_6+=1
key_list=[max_1,max_2,max_3,max_4,max_5,max_6]
print ('\n'+'Possible keyword size are:',max_1,',',max_2,',',max_3,',',max_4,',',max_5,',',max_6) gcd1=np.gcd(max_1,max_2)
gcd1=np.gcd(gcd1,max_3)
gcd1=np.gcd(gcd1,max_4)
gcd1=np.gcd(gcd1,max_5)
gcd1=np.gcd(gcd1,max_6)
print ('GCD:',gcd1)
i=0
while i<=5:
key_1=key_list[i]
print ('\n'+'Assuming',key_1,'as keyword size')
#dividing cipher text into L parts z_list=[[]for x1 in range(0,key_1)] value1=0
while value1<key_1:
for i2 in range(value1,len(ciphertext),key_1): z_list[value1].append(ciphertext[i2])
value1+=1
#cracking cipher text to plain text
value1=0 Keyword1=[]
while value1<key_1:
W_list=[]
for charc in alpha1:
b_1 = z_list[value1].count(charc) b_1 = b_1/26
b_1 = round(b_1,7) W_list.append(b_1)
val_I =24 J_list=[] value_t=0 while val_I>=0:
VAL_B= shift(alpha_percent,value_t) VAL_K = np.dot(W_list,VAL_B) VAL_K = round(VAL_K,6) J_list.append(V AL_K)
val_I -= 1
value_t+=1 Max1=max(J_list)
list_F = [D for D, E in enumerate(J_list) if E==Max1] list_F[0]=((26-list_F[0])%26) key=num_dict[list_F[0]].upper() Keyword1.append(key)
S1_list=[]
for character in z_list[value1]:
number = ord(character) - 97 number = ((number - list_F[0])%26) S1_list.append(number)
a2_list=[]
for j in S1_list: a2_list.append(num_dict[j])
z_list[value1]=a2_list
value1+=1
print ('Vigenere Encryption Keyword:',''.join(Keyword1) ) value2=0
variable1=0
plaintext=[]
val1=int(len(ciphertext)/key_1)
while variable1<val1:
while value2<key_1: plaintext.append(z_list[value2][variable1]) value2+=1
variable1+=1
value2=0 value2=0
while value2<(len(ciphertext)%key_1):
    plaintext.append(z_list[value2][variable1])
value2+=1
print ('\n'+'Plain Text after decryption:') 
print (''.join(str(elm) for elm in plaintext)) 
i+=1