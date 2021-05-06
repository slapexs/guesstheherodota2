import random
from random import randint
score = 0
lives = 3
listHeros = [{
    "str": ["Abaddon", "Alchemist", "Axe", "Beastmaster", "Brewmaster", "Bristleback", "CentaurWarrunner", "ChaosKnight", "Clockwerk", "Dawnbreaker"]
}, {
    "agi": ["AntiMage", "ArcWarden", "Bloodseeker", "BountyHunter", "Broodmother", "Clinkz", "DrowRanger", "EmberSpirit", "FacelessVoid", "Gyrocopter"]
}, {
    "int": ["AncientApparition", "Bane", "Batrider", "Chen", "CrystalMaiden", "DarkSeer", "DarkWillow", "Dazzle", "DeathProphet", "Disruptor"]
}
]


def rancate():
    return randint(0, 2)


def ranpos():
    return randint(0, 2)


def getList(dict):
    return list(dict.keys()).pop()


def shuffleword(cate):
    return random.shuffle(cate)


# ตัวแปรตำแหน่งของข้อความ
poscate = rancate()
keydict = getList(listHeros[poscate])
posword = ranpos()


def check_plaintext(ans, question, plaintext):
    for i in range(len(question)):
        if ans == question[i]:
            plaintext[i] = ans
    win = ''.join(plaintext) == question
    return win


while (len(listHeros[poscate][keydict]) > 0) and (lives > 0):
    # สุ่มลำดับคำในหมวดหมู่
    listQuestion = listHeros[poscate][keydict]
    shuffleword(listQuestion)

    # เลือกคำถามจากตัวสุกท้ายใน List
    question = listQuestion.pop()
    # แสดงหมวดหมู่ของ Hero
    print("Category is : " + keydict.upper())
    # เมื่อได้ชื่อ Hero แล้วนำมาแยกแล้วเปลี่ยนเป็น ?
    plaintext = list('?'*len(question))

    while True:
        # แสดงช่องคำตอบเป็น ?
        print(plaintext)
        # แสดงจำนวนชีวิตที่เหลือ
        print('-> Your alive: ' + ('♥ '*lives))
        # บอก User ให้หรอกคำตอบมาทีละ 1 ตัว
        ans = input('** Insert you answers: ')

        # เช็คคำตอบที่ได้รับกับชื่อ Hero
        if ans in question:
            # ส่งค่าไปเช็คในฟังก์ชัน และ รับreturn ว่าuserทายชื่อถูกหมดทุกตัวรึยัง
            win = check_plaintext(ans, question, plaintext)
            # ทายถูกต้องครบทุกตัวอักษร และ ชีวิตยังเหลือ
            if win:
                print("Wow! you won this is hero is: " + question)
                # เพิ่มคะแนน
                score = score+1
                print("Your score = " + str(score))
                break
        else:
            print("=> Wrong answers! atk you lives")
            # เมื่อทายผิดจะลดเลือด
            lives = lives - 1
            # เช็คว่าถ้าเลือดเหลือ 0 ให้จบเกม
            if lives == 0:
                print("- Game over! this word is: " + question)
                break
