
print("Добро пожаловать в калькулятор")
sum = input("Какой счёт в итоге? $")
percents = input("Какой процент оставить официанту? ")
amount_ppl = input("На скольких людей разделить счёт? ")

result = float(sum) / float(amount_ppl) + (float(sum) / 100 * float(percents)) / float(amount_ppl)


result = (float(sum) + (float(sum) / 100 * float(percents))) / float(amount_ppl)
print(f"Каждому надо заплатить: ${round(result, 2)}")