print("1. Schedule")
print("2. Run bot")
app = int(input("Run bot or schedule?: "))

if app == 1:
    import schedule
elif app == 2:
    import post
else:
    print("Invalid input")
