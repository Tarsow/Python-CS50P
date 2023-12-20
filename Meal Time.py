def main():
    x = input("What time is it? ")
    y = convert(x)
    if 7 <= y <= 8:
        print("breakfast time")
    elif 12 <= y <= 13:
        print("lunch time")
    elif 18 <= y <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours) + int(minutes)/60)

if __name__ == "__main__":
    main()
