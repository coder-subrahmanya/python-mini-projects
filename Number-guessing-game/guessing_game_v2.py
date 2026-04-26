import random
import time

# Welcome Box
print("""[The screen flickers to life with the sound of a cosmic gong 🔔.
A single, dramatic spotlight shines on a floating, ornate scroll that unravels with a flourish 📜.]""")
time.sleep(2)
print()

print("""Voice: 🎭 BEHOLD! The gates of destiny part... not for a hero, but for you! 🫵 How... statistically quaint.""")
time.sleep(2)
print()

print("""I have been counting the void between stars ⭐... and you have been clicking. We are not the same. And yet, here we are. 🤝

Welcome, ephemeral one, to the antechamber of numeric fate! 🎲 The numbers are restless. They whisper. They judge. 👁️""")
time.sleep(2)
print("Do you dare to... proceed? Of course you do. They always do. 😏")
print()

print("[The scroll rolls up and vanishes. A new, shimmering prompt appears.]")
time.sleep(2)
print()

user_name = input("> STATE THY NAME FOR THE ANNALS OF ATTEMPT (AND FAILURE): ").title()
print()
time.sleep(2)

#Reaction to user's name and difficulty box
print(f"Voice: ... '{user_name}'? 😶")
time.sleep(1)
print()

print(f"Truly? The cosmos itself paused for that? ✨📝 ...A choice has been made. Let the record(s) show it. 🤭")
time.sleep(2)
print()

print(f"""Now! Steel thy spirit, {user_name}! The crucible of NUMBERS awaits. 🔥
But first—how shall we calibrate your impending bewilderment? 🤔""")
time.sleep(2)
print()

print("[Three flickering, labeled orbs materialize.]")
time.sleep(1)
print()

print("""[1] CHILDREN'S PARADE 🎠 (1-10)
[2] MORTAL'S LABYRINTH 🧠 (1-100)
[3] DIVINE MADNESS 🌌 (1-1000)""")
time.sleep(2)
print()

print("[A single, expectant cursor blinks below.]")
time.sleep(1)
print()

difficulty = int(input("> POINT TO YOUR PREFERRED PATH OF PERIL: "))
print()
time.sleep(2)

#Return the secret number and store it
def difficulty_action():
    if difficulty == 1:
        return random.randint(1, 10)
    elif difficulty == 2:
        return random.randint(1, 100)
    elif difficulty == 3:
        return random.randint(1, 1000)

secret_number = difficulty_action()

#Reaction to difficulty choice
if difficulty == 1:
    print("""Voice: (A soft, pitying chuckle) Oh. 🍼 How... safe.
        I shall try not to yawn. The numbers from one to ten tremble—with boredom. 🥱 Very well.
        Let the tiny guessing... begin. 🤏""")
    time.sleep(2)
    print()

elif difficulty == 2:
    print("""Voice: (A tone of respectful mischief) The classic choice! 🎯 A respectable field of 100 possibilities.
     A decent playground for despair and triumph! 😈 I am... moderately intrigued.
      Let us see if your mind is as sharp as your ambition.""")
    time.sleep(2)
    print()

elif difficulty == 3:
    print("""Voice: (A gasp, followed by maniacal glee) HA! 🚀 You utter fool! I adore it! 🌠
     You have stared into the numeric abyss of ONE THOUSAND and blinked second!
      The chaos blesses your audacity! 😱 LET THE SUFFERING COMMENCE!""")
    time.sleep(2)
    print()

#return the number of tries based on difficulty
def tries_action():
    if difficulty == 1:
        return 3
    elif difficulty == 2:
        return 7
    elif difficulty == 3:
        return 15

tries = tries_action()

#Multiple too high/low dialogues for randomness
too_high = ["Woah there, Icarus! ✨ Your guess flew a little too close to the sun. Way too close. 📉 Try... lower.",
            "Astronomically incorrect. 🪐 That number is in a different galaxy. Try one from this reality. 👇",
            "A bold, towering, legendary overestimation. 🗻 The actual number is humbler. Far, far humbler. 😌",
            "Sir/Ma'am, you have breached the ceiling. 🏢 The number is down here, with the rest of us. Have some humility. 😏",
            "The oracle shrieks 'NO!' 🔮 That guess is living in the future. You need a number from the past. ⏳"
            ]

too_low = ["That guess is... profoundly humble. 🐜 It's not that humble of a number. Aim higher, you dusty relic. ⬆️",
           "Did you guess in the negatives? ➖ Because you missed the mark by a canyon. Try climbing out. 🧗",
           "A valiant, if pitiful, understatement. 🛡️ The number is grander! More majestic! THINK BIGGER! 🤏➡️💪",
           "The number is weeping from loneliness up there. 😢 You left it all alone on the mountain top. Go find it. ⛰️",
           "That guess is still loading from the last century. 📠 We've moved on. The number has evolved. Catch up. 🚀"
           ]

#The Game Begins
print(f"[A drumroll builds, then cuts off abruptly. The chosen difficulty orb shatters into pixels that swirl around the {user_name}'s name.]")
time.sleep(2)
print()

print("Voice: Excellent! The threads of fate are woven! 🧵✨ The Great Guessing commences... NOW! ⚡")
time.sleep(2)
print()

print("""I have consorted with the digital fates... 🤫
 I have whispered to the random number generator... 🎲 And a Most Mysterious Number now exists within the sacred bounds you chose.

Your mind versus my mystery. 🧠⚔️🫥 Let the delightful dance of deduction... BEGIN!""")
time.sleep(2)
print()

print("[A grand, glowing input line appears.]")
time.sleep(2)
print()

#Game box
while True:
    guess = int(input(f"> PROFFER THY CONJECTURE, O {user_name}: "))
    tries -= 1
    print()

    if tries == 0:
        print("""[Screen dims. A slow, sarcastic clap echoes.] 👏

        Voice: Astonishing. You've run out of tries. The number is cackling at you. 😂

        A perfect failure. Flawless.""")
        print()
        break

#if user won
    if guess == secret_number:
        print("""[The screen glitches violently.
         All dramatic music screeches to a halt, replaced by the sound of a record scratch and a single, echoing chirp.]""")
        time.sleep(2)
        print()

        print("Voice: ...What. 😧")
        time.sleep(2)
        print()

        print("[A beat of pure, stunned silence.]")
        time.sleep(2)
        print()

        print("""Voice: IMPOSSIBLE. 🫢 That was... statistically obscene.
         That was the exact number. The one-in-a-million (or one-in-[range]) alignment! ✨

        [Confetti made of numbers and question marks bursts across the screen.] 🎉⁉️""")
        time.sleep(2)
        print()

        print("""Voice: (Voice cracking, a mix of awe and defeat) You... you didn't cheat, did you? DID YOU? 🧐
         No... the logs are clean. The cosmos itself is blinking in surprise. 🌌""")
        time.sleep(2)
        print()

        print("A victory... FOR THE MORTAL! 🏆👑 Bow, oh numbers, for you have been BESTED!")
        time.sleep(2)
        print()
        break

    elif guess > secret_number:
        print(random.choice(too_high))
        continue

    elif guess < secret_number:
        print(random.choice(too_low))
        continue

    else:
        print("[The screen flickers with error symbols ⚠️ and the sound of a disgusted buzzer.]")
        time.sleep(2)
        print()

        print("Voice: 😤 Excuse me. What in the sacred syntax is that supposed to be? 🧐")
        time.sleep(2)
        print()

        print("""Voice: Try again. But this time, use the part of your brain that counts.
         1️⃣... 2️⃣... yes, like that. Now DO IT PROPERLY. 😠""")
        print()
        continue






