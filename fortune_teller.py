import random

print("🔮 Welcome to Abhay Gupta's Fortune Teller (21JE0011) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Abhay! Keep smiling.",
        "Happiness attracts happiness. Keep spreading the joy!"
    ],
    "sad": [
        "Storms don't last forever. Better days are coming.",
        "Even the darkest night ends with sunrise."
    ],
    "neutral": [
        "Peaceful days bring the best clarity.",
        "A calm mind is a powerful one."
    ],
    "stressed": [
        "Take a deep breath, Abhay. You're doing great.",
        "Even chaos has its purpose. Trust the process."
    ]
}

if mood in fortunes:
    print("✨ Your fortune: " + random.choice(fortunes[mood]) + " ✨")
else:
    print("🤔 I couldn't understand that mood. Try happy, sad, neutral, or stressed.")
