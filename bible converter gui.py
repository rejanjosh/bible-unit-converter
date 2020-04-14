import easygui, sys

choices = ["shekel to grams", "grams to shekels", "cubits to grams","grams to cubits","Exit"]

while True:
    choice = easygui.indexbox("choose what bible unit you need to convert","bible converter", choices)

    if choice == 4:
        sys.exit()
    else:
        x = float(easygui.integerbox("enter your number", "bible converter"))
        try:

            if choice == 4:
                sys.exit()
            elif choice == 0:
                answer = x * 11.4
            elif choice == 1:
                answer = x / 11.4
            elif choice == 2:
                answer = x * 46
            elif choice == 3:
                answer = x / 46
            easygui.msgbox(answer, "answer")
        except:
            easygui.msgbox("error")