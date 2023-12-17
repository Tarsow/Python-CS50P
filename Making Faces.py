def Main():
    print("converted text: " + Convert(input("the text you want to convert:")))

def Convert(text):
    return text.replace(":)","🙂").replace(":(","🙁").replace("(:","🙂").replace("):","🙁")

Main()
