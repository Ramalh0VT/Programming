while True:
    print("\n=== File utility Tool ===")
    print("1 - Organize Folder")
    print("2 - Bulk rename files")
    print("3 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Organizer selected")

    elif choice == "2":
        print("Renamer selected")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
