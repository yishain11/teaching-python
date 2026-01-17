# אם מחלקים ב־0 – החזר None + סטטוס מתאים במקום קריסה
def safe_div(a, b):
    return a / b


print(safe_div(10, 0))


# אם האינדקס מחוץ לטווח – החזר את האיבר האחרון, ואם הרשימה ריקה החזר None
def get_item(items, i):
    return items[i]


print(get_item([5, 6, 7], 10))


# אם הקלט אינו מחרוזת – החזר "Unknown" במקום קריסה
def normalize_name(name):
    return name.strip().title()


print(normalize_name(None))


# אם אחד המפתחות חסר – התייחס אליו כ־0 והמשך לחשב ציון
def calc_score(stats):
    return stats["kills"] * 10 + stats["assists"] * 5 - stats["deaths"] * 3


print(calc_score({"kills": 2, "deaths": 1}))


# אם הפורמט אינו "מספר:מספר" – נסה לפצל לפי "-" ואם לא מצליח החזר 0
def area(spec):
    w, h = spec.split(":")
    return int(w) * int(h)


print(area("10-5"))


# אם הביטים מכילים תווים לא חוקיים – נסה לנקות אותם, ואם לא מצליח החזר None
def binary_to_int(bits):
    return int(bits, 2)


print(binary_to_int("10 01"))


# חשב ממוצע רק לערכים שניתן להמיר ל־float. אם אין – החזר None
def avg(nums):
    return sum(nums) / len(nums)


print(avg([10, "20", None, 30]))


# אם חסר מידע במבנה המקונן – החזר "NO_CITY" במקום קריסה
def get_city(user):
    return user["profile"]["address"]["city"].upper()


print(get_city({"profile": {"address": {}}}))


# אם הסכום אינו מספר או גדול מהיתרה – החזר את היתרה המקורית
def withdraw(balance, amount_text):
    amount = int(amount_text)
    return balance - amount


print(withdraw(100, "fifty"))


# אם האינדקס מחוץ לטווח – בחר איבר בצורה מחזורית. אם הרשימה ריקה – החזר None
def pick_code(codes, idx):
    return codes[idx]


print(pick_code(["A1", "B2", "C3"], 5))
