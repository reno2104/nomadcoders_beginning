### List
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

days_of_week.clear()  #데이터 삭제.
days_of_week.reverse()  #순서정반대로

days_of_week.append("Sat")  #추가
days_of_week.append("Sun")  #추가
print(days_of_week)

days_of_week.remove("Fri")  #항목제거
print(days_of_week)

print(days_of_week[2])  #순서는 1이 아닌 0부터 셈.



### Tuples
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
# 리스트와의 차이 ? 리스트는 내용 변경이 가능하지만, 튜플은 불변성을 띈다.
# 그러므로 튜플은 내용을 바꿀수 없다.

print(days[0])

# 튜플, 리스트 모두 적용되는 것.
print(days[-1])
# 0 뿐만 아니라 -n도 값이 불러올 수 있다.
