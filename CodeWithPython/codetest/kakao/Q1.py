kakao_id = str(input())
kakao_id = kakao_id.lower()
#lower the id
print(f"#1-stage {kakao_id}")
#알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
index = 0
new_ind = 0
rev_kakao = ''
while index != len(kakao_id):
    #print(index)
    if kakao_id[index].isdigit():
        rev_kakao = rev_kakao + kakao_id[index]
        
    if kakao_id[index].isalpha():
        rev_kakao = rev_kakao + kakao_id[index]
        #print(f"alpha-{index}")
    if kakao_id[index] == '-':
        rev_kakao = rev_kakao + kakao_id[index]
        
    if kakao_id[index] == '_':
        rev_kakao = rev_kakao + kakao_id[index]
        
    if kakao_id[index] == '.':
        rev_kakao = rev_kakao + kakao_id[index]
        #print(f"special-{index}")
        
    index += 1
    
    
#stage 2 - pass
print(f"#2-stage {rev_kakao}")

index = 0
cnt = 0
conv_kakao = ''
while index != len(rev_kakao):

    if rev_kakao[index] == '.':
        cnt += 1

    
    
    else:
        if cnt >= 1:
            conv_kakao = conv_kakao + '.'
            cnt = 0

        if rev_kakao[index].isdigit():
            conv_kakao = conv_kakao + rev_kakao[index]
        
        if rev_kakao[index].isalpha():
            conv_kakao = conv_kakao + rev_kakao[index]
            
        if rev_kakao[index] == '-':
            conv_kakao = conv_kakao + rev_kakao[index]
            
        if rev_kakao[index] == '_':
            conv_kakao = conv_kakao + rev_kakao[index]
        
    index += 1

if cnt > 0:
    conv_kakao = conv_kakao + '.'

#stage 3 - pass
print(f"#3-stage {conv_kakao}")

index = 0
temp = ''

if conv_kakao != '':
    if conv_kakao[0] == '.' or conv_kakao[len(conv_kakao)-1] == '.':
        if conv_kakao[0] == '.':
            temp = temp + conv_kakao[1:len(conv_kakao)]
            conv_kakao = temp
            temp = ''
        if len(conv_kakao) > 0:
            if conv_kakao[len(conv_kakao)-1] == '.':
                temp = temp + conv_kakao[0:len(conv_kakao)-1]
                conv_kakao = temp
                temp = ''
#stage 4 - pass
print(f"#4-stage {conv_kakao}")

if conv_kakao == '':
    conv_kakao = conv_kakao + 'a'

#stage 5 - pass
print(f"#5-stage {conv_kakao}")


if len(conv_kakao) >= 16:
    tmep = conv_kakao[0:16]
    conv_kakao = temp
    temp = ''
    if conv_kakao[len(conv_kakao)-1] == '.':
        temp = conv_kakao[0:len(conv_kakao)-1]
        conv_kakao = temp
        temp = ''
#stage 6 - pass
print(f"#6-stage {conv_kakao}")

temp = ''
temp = conv_kakao
while len(conv_kakao) == 3:
    if len(conv_kakao) <= 2:
        conv_kakao = conv_kakao + temp[len(temp)-1]


print(conv_kakao)




    