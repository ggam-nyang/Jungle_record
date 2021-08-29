import sys

formula = list(sys.stdin.readline().strip())

# 숫자들을 str값으로 합쳐서 더해줄 temp 변수
temp = ''
# -가 존재한다면 index를 저장하고, 없다면 최장 길이인 51로 저장
try:
    first_minus = formula.index('-')
except:
    first_minus = 51
ans = 0

# 받은 string이 숫자이면, temp에 더해준다. ('5' '1' 받으면 '51'로 합친다.)
# 받은 string이 연산자이면, 첫번째 - 보다 앞, 뒤에 있는지를 기준으로 ans에 더해주거나 빼준다.
# 이유: - 가 한번이라도 등장하면 그 이후의 숫자들은 모두 빼는 값이 돼야한다. (-가 여러개여도 괄호에 의해 어차피 첫 - 뒤는 전부 음수값으로 변경할 수 있다.)
for i in range(len(formula)):
    s = formula[i]
    if s != '+' and s != '-':
        temp += s
    else:
        if i <= first_minus:
            ans += int(temp)
        else:
            ans -= int(temp)
        temp = ''
if first_minus == 51:
    ans += int(temp)
else:
    ans -= int(temp)
print(ans)
