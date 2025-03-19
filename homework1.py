#題目:猜數字遊戲
#說明：
#程式會隨機生成一個 1 到 100 之間的整數。
#使用者需要輸入數字來猜測這個隨機數。
#每次猜測後，程式會提示「太大了」、「太小了」或「猜對了」。
#直到使用者猜中數字後，程式才會結束，並顯示總共猜了多少次。

import random

while True:
    num = random.randint(1, 100)
    attempts = 0
    print("\n 猜猜看數字 1~100")

    while True:
        try:
            checknum = int(input("請輸入你的猜測: "))
            attempts += 1

            if checknum < 1 or checknum > 100:
                print("⚠ 請輸入 1 到 100 之間的數字！")
            elif checknum > num:
                print("數字太大了，再猜一次")
            elif checknum < num:
                print("數字太小了，再猜一次")
            else:
                print(f" 恭喜猜對! 你總共猜了 {attempts} 次 ")
                break
        except ValueError:
            print("⚠ 請輸入有效的數字！")

    # 讓使用者選擇是否再玩一次
    play_again = input("要再玩一次嗎？(輸入 'y' 繼續，其他鍵結束) ")
    if play_again.lower() != 'y':
        print("感謝遊玩，再見！")
        break
