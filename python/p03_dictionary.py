
# 중괄호와 : 을 사용하여 정의한다
d1 = {
  "hello": 10, "world": 20.5
}

print('-- Key 가 hello 인 항목의 value 는? --')
print(d1["hello"])

# 세 개의 key 에 대하여 그 값을 알아보자 가능한가?
keys = [ "hello", "are_you_there", "world" ]
for key in keys:
  print('-- Key:', key)
  print('--- Value:', d1[key])


