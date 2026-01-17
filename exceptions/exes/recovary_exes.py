# Type 2: אם b == 0 → במקום קריסה להחזיר (None, "used_default") או (0, "used_default"), אחרת (result, "ok")
def safe_div(a, b):
    return a / b


print(safe_div(10, 0))


# Type 2: אם האינדקס מחוץ לטווח → להחזיר את האיבר האחרון; אם הרשימה ריקה → להחזיר None
def get_item(items, i):
    return items[i]


print(get_item([5, 6, 7], 10))


# Type 2: אם name לא מחרוזת (למשל None/מספר) → להחזיר "Unknown" במקום קריסה
def normalize_name(name):
    return name.strip().title()


print(normalize_name(None))


# Type 2: אם חסר מפתח במילון → להתייחס אליו כ־0 (kills/assists/deaths) ולהחזיר ציון ללא קריסה
def calc_score(stats):
    return stats["kills"] * 10 + stats["assists"] * 5 - stats["deaths"] * 3


print(calc_score({"kills": 2, "deaths": 1}))


# Type 2: אם אין ":" אבל יש "-" → לפצל לפי "-" ולהמשיך; אם עדיין לא תקין → להחזיר 0
def area(spec):
    w, h = spec.split(":")
    return int(w) * int(h)


print(area("10-5"))


# Type 2: אם יש תווים לא חוקיים בבינארי (כמו רווחים) → להסיר רווחים ולנסות שוב; אם עדיין לא חוקי → להחזיר None
def binary_to_int(bits):
    return int(bits, 2)


print(binary_to_int("10 01"))


# Type 2: לחשב ממוצע רק לערכים שניתנים להמרה ל-float; אם אחרי סינון אין מספרים → להחזיר None
def avg(nums):
    return sum(nums) / len(nums)


print(avg([10, "20", None, 30]))


# Type 2: אם חסר מידע במבנה המקונן → להחזיר "NO_CITY"
def get_city(user):
    return user["profile"]["address"]["city"].upper()


print(get_city({"profile": {"address": {}}}))


# Type 2: אם amount_text לא מספר או גדול מהיתרה → להחזיר balance, אחרת יתרה חדשה
def withdraw(balance, amount_text):
    amount = int(amount_text)
    return balance - amount


print(withdraw(100, "fifty"))


# Type 2: אם idx מחוץ לטווח → להשתמש באינדקס מחזורי; אם הרשימה ריקה → להחזיר None
def pick_code(codes, idx):
    return codes[idx]


print(pick_code(["A1", "B2", "C3"], 5))
