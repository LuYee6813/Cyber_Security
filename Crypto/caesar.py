#加密過的文字
message = 'slfrfwi{kdkdkd}'
#使用到的符號表
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz' 
#位移key
key=3

translated = ''             #字串清空
for symbol in message:      #將加密文字單獨抓出至symbol
    if symbol in SYMBOLS:    #如果symbol有在SYMBOLS裡就執行解密
        symbolIndex = SYMBOLS.find(symbol) #抓取symbol在SYMBOLS的游標位置
        translatedIndex = symbolIndex - key #當前轉換游標為游標位置-密鑰
        if translatedIndex < 0: #如果減完key變負的話從最後開始
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
print(translated)
#ANS:This is my secret message.
