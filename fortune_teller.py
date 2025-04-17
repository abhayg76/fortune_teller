print("🔮 Welcome to Abhay Gupta's Fortune Teller (21JE0011) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Abhay! Keep smiling. ✨")
elif mood == "sad":
    print("🌧️ Your fortune: Storms don't last forever. Better days are coming. 🌈")
elif mood == "neutral":
    print("🌀 Your fortune: A calm mind is a powerful one.")
else:
    print("🤔 I couldn't understand that mood. Try happy, sad, or neutral.")
