# Week 6 Code Along 3
while True: 
    file_name = input("enter a file name")
    try:
        fhandle = open(file_name, "w+")

        while True: 
            text = input("What do yoy want to write out?")
            if text.lower() == "done":
                break
        
        fhandle.write(text + "/n")
    except Exception as ex:
        print(ex)
    else:
        break

    