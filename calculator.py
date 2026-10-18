def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("ماشین حساب ساده")
    print("عملیات: add, subtract, multiply, divide")
    op = input("انتخاب عملیات: ").strip().lower()
    try:
        a = float(input("عدد اول: "))
        b = float(input("عدد دوم: "))
    except ValueError:
        print("ورودی عددی نامعتبر.")
        return
    try:
        if op == 'add':
            result = add(a, b)
        elif op == 'subtract':
            result = subtract(a, b)
        elif op == 'multiply':
            result = multiply(a, b)
        elif op == 'divide':
            result = divide(a, b)
        else:
            print("عملیات نامعتبر.")
            return
        print(f"نتیجه: {result}")
    except Exception as e:
        print(f"خطا: {e}")

if __name__ == "__main__":
    main()
