# dict

player = {
  'name': 'reno', 
  'age': 12, 
  'alive': True,
  'fav_food': ["π","π"]
         }
# print(player.get('age'))
# λμλλ¦¬λ ν€-κ°μ΄ μμΌλ‘ μ΄λ£¨μ΄μ Έμλ€.
# ν€ : name, age, alive
# κ° : reno, 12, True

# print(player.get('fav_food'))
# print(player['fav_food'])

### μ«μ λͺ©λ‘, ν¬λ λ¦¬μ€νΈ λ± μ΄λ€ λͺ©λ‘μ΄ μλ€λ©΄ : λ¦¬μ€νΈλ νν.
### λ§μ μμ±λ€μ κ°μ§κ³  μλ λ°μ΄ν°λ₯Ό λ§λ€ λ : λμλλ¦¬

# print(player.pop('age')) # λ°μ΄ν° μ§μ°κΈ°

print(player)
player['xp'] = 1500 # λ°μ΄ν° μΆκ°
print(player)

# λ°μ΄ν° λ΄ λ¦¬μ€νΈ μΆκ°
player['fav_food'].append("π±")
print(player.get('fav_food'))
print(player['fav_food'])

# ''λ "" κ°λ₯.
# κ°μΌλ‘λ string, number, boolean, list μ΄λ€ κ²μ΄λ  κ°λ₯.
