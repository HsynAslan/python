
# Grup 21 OTOMATA PROJE ÖDEVİ
# ---------------------------------
# GRUP ÜYELERİ:
# - İBRAHİM CAN SARISAKAL - 394820 => TAKIM LİDERİ
# - HÜSEYİN ASLAN - 394788
# - BARIŞ KOÇ - 394812
# - MUHAMMET EMİN GÜNDOĞAR - 407596
# - OMAR SHOBAT - 410740

import tkinter as tk
import re
import turtle

errors = {
    'recursive': [],
    'turtle': []
}


def turtle_draw():
    runFlag = True
    if runFlag:
        pen = turtle.Turtle()
        pen.speed(150)
        pen.shape('classic')     # kalem simgesi
        pen.color('red', 'grey')

    commandDefinitions = {
        'F': lambda x: pen.forward(x),
        'R': lambda x: pen.right(x),
        'L': lambda x, y: loopFunction(x, y),
        'COLOR': lambda x: pen.color(x),
        'PEN': lambda x: pen.width(x)
    }

    colors = {
        'K': 'red',
        'Y': 'green',
        'S': 'black',
        'M': 'blue',
    }

    def recursive(commandText):
        if commandText.count("[") != commandText.count("]"):
            runFlag = False
            tk.messagebox.showerror(
                title="Kritik Hata", message="TXT dosyanızda [ veya ] karakterleri eksik veya fazla var. Lütfen tekrar deneyiniz. Program Kapatılıyor.")
            exit()
        finalDict = {}
        defaultRegexPatternWithBracketsAndCommands = '(\[.*\])|(\w\d+)'
        defaultRegexPatternWithoutBrackets = '(?:[LFR]\d+)'
        defaultRegexPatternWithoutCommands = '(\[.*\])'

        arrayReBrute = re.findall(
            defaultRegexPatternWithBracketsAndCommands, commandText)
        arrayReBrute = list(map(lambda x: ''.join(x).split()[0], arrayReBrute))
        missionFlag = 0
        for reItem in arrayReBrute:
            missionFlag += 1
            if re.match(defaultRegexPatternWithoutBrackets, reItem) != None:
                finalDict['startCommand' if missionFlag ==
                          1 else 'endCommand'] = reItem[0]
                finalDict['startCount' if missionFlag ==
                          1 else 'endCount'] = (reItem[1:])
                if finalDict['startCommand' if missionFlag ==
                             1 else 'endCommand'] == 'F' and int(finalDict['startCount' if missionFlag ==
                                                                           1 else 'endCount']) > 150:
                    finalDict['startCount' if missionFlag ==
                              1 else 'endCount'] = 150
                    tk.messagebox.showwarning(
                        title="Kod Okuma Uyarısı", message="F değeri 150'den büyük olamaz.Değer Geçerli Değer Olan 150ye Ayarlanmıştır.")
                if finalDict['startCommand' if missionFlag ==
                             1 else 'endCommand'] == 'R' and int(finalDict['startCount' if missionFlag ==
                                                                           1 else 'endCount']) > 360:
                    finalDict['startCount' if missionFlag ==
                              1 else 'endCount'] = int(
                        finalDict['startCount' if missionFlag ==
                                  1 else 'endCount']) % 360
                    tk.messagebox.showwarning(
                        title="Kod Okuma Uyarısı", message="R değeri 360'dan büyük olamaz.Değeriniz 360'a modlanarak ayarlanmıştır.")

                missionFlag += 1
            elif re.match(defaultRegexPatternWithoutCommands, reItem) != None:
                finalDict['nextStep'] = reItem
                finalDict['nextDict'] = recursive(reItem[1:-1])
        return finalDict

    def loopFunction(loopDict):
        defaultRegexPatternCOLOR = '(COLOR\w)'
        defaultRegexPatternPEN = '(PEN\d+)'
        try:
            if loopDict['startCommand'] == 'F':
                pen.forward(int(loopDict['startCount']))
            elif loopDict['startCommand'] == 'R':
                pen.right(int(loopDict['startCount']))
            elif loopDict['startCommand'] == 'PEN':
                pen.width(int(loopDict['startCount']))
            elif loopDict['startCommand'] == 'COLOR':
                pen.color(loopDict['startCount'])
            elif loopDict['startCommand'] == 'L':
                for i in range(int(loopDict['startCount'])):
                    if loopDict['nextDict'] != None:
                        if re.findall(defaultRegexPatternCOLOR, loopDict['nextStep']) != []:
                            try:
                                pen.color(colors[(re.findall(defaultRegexPatternCOLOR,
                                                             loopDict['nextStep'])[0][-1])])
                            except turtle.TurtleGraphicsError:
                                pass
                            except:
                                tk.messagebox.showwarning(
                                    title="Şekil Çizme Uyarısı", message="COLOR Değişkeni Hatalı Lütfen Düzenleyiniz. Program Kapatılıyor.")
                                turtle.bye()
                                return None
                        if re.findall(defaultRegexPatternPEN, loopDict['nextStep']) != []:
                            try:
                                pen.width(int(re.findall(defaultRegexPatternPEN,
                                                         loopDict['nextStep'])[0][3:]))
                            except turtle.TurtleGraphicsError:
                                pass
                            except turtle.Terminator:
                                pass
                            except:
                                tk.messagebox.showwarning(
                                    title="Şekil Çizme Uyarısı", message="PEN değişkeni hatalı lütfen geçerli bir değer giriniz. Program Kapatılıyor.")
                                turtle.bye()
                                return None
                        loopFunction(loopDict['nextDict'])

        except KeyError:
            tk.messagebox.showerror(
                title="Kod Okuma Hatası", message="Grammeriniz doğru formatta değildir. Program Durduruluyor.")
            exit()
        try:
            if loopDict['endCommand'] != None:
                if loopDict['endCommand'] == 'F':
                    pen.forward(int(loopDict['endCount']))
                elif loopDict['endCommand'] == 'R':
                    pen.right(int(loopDict['endCount']))
                elif loopDict['endCommand'] == 'PEN':
                    pen.width(int(loopDict['endCount']))
                elif loopDict['endCommand'] == 'COLOR':
                    pen.color(int(loopDict['endCount']))
                else:
                    tk.messagebox.showerror(
                        title="Kritik Hata", message="TXT dosyanızdaki komutlama geçersizdir. Lütfen tekrar deneyiniz. Program Kapatılıyor.")
                    exit()
        except:
            pass

    dosya = open("./21-commands.txt", "r")

    for teksatir in dosya:
        text = teksatir
    text = text.replace(" ", "").upper()

    finalCommandDict = recursive(text)

    loopFunction(finalCommandDict) if runFlag else None
    turtle.done()


def recursive_errors(recErrors):
    if len(errors['recursive']) != 0:
        for error in errors['recursive']:
            recErrors.insert(tk.END, error)


def allInOne(recErrors):
    turtle_draw()
    recursive_errors(recErrors)


pencere = tk.Tk()

pencere.title("Otomata Projesi  Grup-(21)")
pencere.geometry("1000x400")
pencere.resizable(False, False)
box1 = tk.Canvas(bg="white", width=500, height=500)

dosya = open("./21-commands.txt", "r")

for teksatir in dosya:
    text = teksatir
girilen_txt = tk.Label(text="Girilen Komutlar",
                       font="Verdana 18 bold underline")
girilen_txt.place(x=0, y=0)
yüklenenprogram = tk.Label(text=text.upper(), font="25")
dosya.close()
yüklenenprogram.place(x=10, y=170)

box1.place(x=0, y=0)


box2 = tk.Canvas(bg="white", width=500, height=500)

recErrors = tk.Listbox()
tk.Button(text="Şekli Çiz", command=lambda: allInOne(recErrors), border=3,
          background="lightblue", font='sans 12 bold').place(x=700, y=160, width=100, height=50)
box2.place(x=500, y=0)
pencere.mainloop()
