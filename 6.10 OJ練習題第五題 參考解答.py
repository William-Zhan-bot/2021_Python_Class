# 帳戶產生器
# 設計一個帳戶產生器 可輸入五位數字做帳戶 並產生一組通行碼

# 輸入不為0的任意五位數數字 以空格分開
# 輸出為兩組 一組為完整帳戶 另一組為通行碼
# 完整帳戶: 一組八位數字 為原先輸入的帳戶前方空格補0 
# 通行碼:
# 將輸入五位數字的頭a 尾b 取下 中間變成一組數字
# 中間數字除以(a+b)得到c 並將a*b為字串加在c的後面 打印成通行碼
# ex.輸入1 2 3 4 5 
# 輸出:00012345 395


# 帳戶產生器
s = input() # 輸入任意個數字 以空格分開
s = s.split(" ") # 將數字整理成字串
s1 = "".join(s) # 重新合併成不含空格的字串
word = "000" + s1 # 字串的合併 使的字串前方多上三位數字 000012345
print(word)

# 將五位數字的頭a 尾b 取下 中間變成一組數字
final = int(s[len(s)-1]) # 取下結尾
first = int(s[0]) # 取下開頭
s.pop() # 刪除結尾的字串
s.pop(0) # 刪除開頭的字串
num = "".join(s) # 將中間的字串合併
num = int(num) # 轉成整數

# 依題目指定的進行運算
# 中間數字除以a+b 並將a*b加在商的後面 打印成通行碼
key_part1 = int(num/(final + first)) 
key_part2 = final*first
key = str(key_part1) + str(key_part2) # 字串合併
print(key)