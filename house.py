while True:
    name = input("What's your name?     ")
    match name:
        case "Flex" | "Oxy" | "Demmy" | "Idris" | "Racheal" | "Kakashi":
            print("Off-Kamper")
            break
        case "Kiki" | "Marvie" | "Charles" | "Gideon" | "Daniel":
            print("Faj-Kamper")
            break
        case "Levi" | "Hamid" | "Oga mhi":
            print("ETF-Kamper")
            break
        case "Adesh":
            print("Awo-Kamper")
            break
        case "AETO" | "Delight" | "Nicholas" | "Fawas" | "Adegold":
            print("Angola-Kamper")
            break
        case _:
            continue