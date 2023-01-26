# dict

player = {
  'name': 'reno', 
  'age': 12, 
  'alive': True,
  'fav_food': ["🍕","🍔"]
         }
# print(player.get('age'))
# 딕셔너리는 키-값이 쌍으로 이루어져있다.
# 키 : name, age, alive
# 값 : reno, 12, True

# print(player.get('fav_food'))
# print(player['fav_food'])

### 숫자 목록, 투두 리스트 등 어떤 목록이 있다면 : 리스트나 튜플.
### 많은 속성들을 가지고 있는 데이터를 만들 때 : 딕셔너리

# print(player.pop('age')) # 데이터 지우기

print(player)
player['xp'] = 1500 # 데이터 추가
print(player)

# 데이터 내 리스트 추가
player['fav_food'].append("🍱")
print(player.get('fav_food'))
print(player['fav_food'])

# ''나 "" 가능.
# 값으로는 string, number, boolean, list 어떤 것이든 가능.
