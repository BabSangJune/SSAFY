"""
2021.07.14
SSAFY StartCamp day01
"""

student = {'강동옥':28, '김도훈':27}

student['양명균'] = 99

print(student)
print(student['김도훈'])
print(student['이상엽']) # 이렇게 쓰면 에러
print(student.get('문찬솔')) # 요건 에러 안남 