def replace24To11(pArray, idx, offset):
    pArray[idx+offset] = pArray[idx+offset].replace("ˊ", "ˇ")
    return pArray

def toneSandhi():
    p24List = []
    p555List = []

    with open("客語拼音表.txt", mode="r", encoding = "utf-8") as fr:
        for line in fr:
            p24, p11, p31, p55, p2, p5 = line.split("\t")
            p24 = p24.strip()
            p55 = p55.strip()
            p5 = p5.strip()
            if p24:
                p24List.append(p24)
            if p55:
                p555List.append(p55)
            if p5:
                p555List.append(p5)

    fw = open("三個文本-1646-變調.txt", mode="w", encoding = "utf-8")
    with open("三個文本-1646.txt", mode="r", encoding = "utf-8") as fr:
        for line in fr:
            ha, pinyin = line.split("\t")
            pArray = pinyin.split(" ")
            p24Count = 0
            print(ha)
            for idx, item in enumerate(pArray):
                if item.strip() in p24List:
                    p24Count += 1
                elif item.strip() in p555List:
                    if p24Count == 1:
                        pArray = replace24To11(pArray, idx, -1)
                    elif p24Count == 2:
                        pArray = replace24To11(pArray, idx, -1)
                        pArray = replace24To11(pArray, idx, -2)
                    p24Count = 0
                else:
                    if p24Count == 2:
                        pArray = replace24To11(pArray, idx, -2)
                    elif p24Count == 3:
                        pArray = replace24To11(pArray, idx, -2)
                        pArray = replace24To11(pArray, idx, -3)
                    p24Count = 0

                if idx+1 == len(pArray):
                    if p24Count == 2:
                        pArray = replace24To11(pArray, idx, -1)
                    elif p24Count == 3:
                        pArray = replace24To11(pArray, idx, -1)
                        pArray = replace24To11(pArray, idx, -2)
                    p24Count = 0

                if p24Count == 3:
                    pArray = replace24To11(pArray, idx, -1)
                    pArray = replace24To11(pArray, idx, -2)
                    p24Count = 0

            fw.write(ha+"\t"+" ".join(pArray))
    fw.close()

toneSandhi()