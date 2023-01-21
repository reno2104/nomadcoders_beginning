## 커피 만드는 레시피 make some coffee
# Imagine that you are a barista ☕

def select_beans(beans="No beans"):
    return f"{beans} selected!"

def select_process(process="Whole beans"):
    return f"{process} selected!"

def select_ice(ice="No ice"):
    return f"{ice} in !"

def select_syrup(syrup="No syrup"):
    return f"{syrup} in !"

beans = select_beans("Kenya AA Washed")
process = select_process("Americano")
ice = select_ice("ice")
syrup = select_syrup()

print(f"Let's make 2 coffees!")
print(f"#1\n{beans}\n{process}\n{ice}\n{syrup}")

beans = select_beans("Colombia Supremo")
process = select_process("Espresso")
ice = select_ice("No ice")
syrup = select_syrup("1 stick of sugar")

print(f"#1\n{beans}\n{process}\n{ice}\n{syrup}")




##패스트푸드 주문하기

def make_combo(hamburger):
    return f"{hamburger}+🥤"

def add_fries(onlycola):
    return f"{onlycola}+🍟"

def add_dessert(icecream):
    return f"{icecream}+🍦"

combo = make_combo("🍔")
cola_combo = add_fries(combo)
combo_dessert = add_dessert(cola_combo)
print(combo_dessert)



## Gongcha Place


def make_juice(black_milkTea):
  return f"{black_milkTea}=hong_tea+🥛"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+70%🍬"

def add_bubble(bubble_juice):
  return f"{bubble_juice}+black_bubble * 2x"

juice = make_juice("최애 블랙밀크티")
cold_juice = add_ice(juice)
sugar_juice = add_sugar(cold_juice)
perfect_juice = add_bubble(sugar_juice)

print(perfect_juice)
