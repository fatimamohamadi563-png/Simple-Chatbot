# Simple Chatbot

def chatbot():
    print("سلام! من یه چت‌بات ساده‌ام 🤖")
    print("می‌تونی سوالای ساده ازم بپرسی. برای خروج بنویس exit")

    while True:
        user_input = input("تو: ")

        if user_input.lower() == "exit":
            print("چت‌بات: خدافظ! 👋")
            break
        elif "اسم" in user_input:
            print("چت‌بات: من یه ربات کوچولو هستم که توی پایتون نوشته شدم.")
        elif "حال" in user_input:
            print("چت‌بات: مرسی! من خوبم، امیدوارم تو هم خوب باشی. 😊")
        elif "هوش مصنوعی" in user_input:
            print("چت‌بات: من خودم یه نمونه کوچیک از هوش مصنوعی هستم! 😎")
        else:
            print("چت‌بات: متوجه نشدم، میشه یه جور دیگه بپرسی؟")

chatbot()