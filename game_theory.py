import random

questions = [
    "In the realm of Minecraft, who are the ancient builders responsible for the grand structures scattered across the lands?",
    "What mysterious element, once harnessed by the ancient builders, led to their ultimate downfall and extinction?",
    "Within the lore of The Elder Scrolls V: Skyrim, what event triggered the return of dragons to the realm?",
    "In the world of The Legend of Zelda, what is the significance of the Triforce and its three sacred pieces?",
    "Within the lore of Dark Souls, what role do the powerful Lords of Cinder play in the cycle of fire and darkness?",
    "In the universe of Warcraft, who are the Titans and what role did they play in shaping Azeroth?",
    "What mythical artifact serves as the ultimate prize for adventurers in the world of Dungeons & Dragons?",
    "Within the lore of World of Warcraft, what is the origin of the conflict between the Alliance and the Horde?",
    "What ancient civilization once thrived in the world of Terraria before mysteriously vanishing?",
    "In the realm of Final Fantasy VII, what is the significance of the planet's Lifestream and the threat posed by Shinra's exploitation of it?",
    "Within the lore of The Witcher series, what is the origin of the powerful Witchers and their connection to monsters?",
    "In the world of Halo, what are the Forerunners and what role did they play in the fate of the galaxy?",
    "What ancient prophecy foretells the return of the Dragonborn in the world of The Elder Scrolls V: Skyrim?",
    "In the lore of StarCraft, what event led to the rise of the powerful Zerg Swarm and their relentless pursuit of genetic perfection?",
    "Within the universe of Mass Effect, what is the significance of the mysterious Prothean artifacts scattered throughout the galaxy?",
    "What legendary hero's tragic fall from grace led to the corruption of the land in the world of Diablo?",
    "In the world of Middle-earth, what powerful artifact serves as the ultimate weapon against the dark lord Sauron?",
    "Within the lore of League of Legends, what event led to the formation of the powerful League and the end of the Rune Wars?",
    "What ancient curse plagues the land of Lordran, driving its inhabitants to madness and despair in the world of Dark Souls?",
    "In the realm of Minecraft, what is the origin of the enigmatic Endermen and their connection to the End dimension?",
    # Add more questions here...
    "Question 100"
]

answers = [
    "Ancient Builders",
    "Netherite",
    "Alduin's resurrection",
    "Ultimate power",
    "Decide the fate of the world",
    "Creators of Azeroth",
    "The Holy Grail",
    "Resource scarcity",
    "The Hallowed",
    "Energy source",
    "Altered humans",
    "Creators of the Halo rings",
    "The Prophecy of the Dragonborn",
    "The rise of the Overmind",
    "Their advanced technology",
    "Twin Blades of Azzinoth",
    "The One Ring",
    "The destruction of the Rune crystals",
    "The Darksign",
    "Teleportation accidents",
    # Add more answers here...
    "Answer to Question 100"
]

def select_question():
    return random.choice(questions)

def verify_answer(question, answer):
    correct_answer = answers[questions.index(question)]
    if answer == correct_answer:
        print("Answer verified. Correct!")
    else:
        print("Answer verified. Incorrect. The correct answer is:", correct_answer)
    print("")

print("Welcome to the Game Theory Trivia Game!")
print("Let's test your knowledge of gaming lore.")
print("")

while True:
    input("Press Enter to receive a random gaming lore question...")
    selected_question = select_question()
    print(selected_question)
    print("")
    user_answer = input("Your answer: ")
    verify_answer(selected_question, user_answer)
    play_again = input("Would you like to receive another question? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thank you for playing! Goodbye!")
        break
