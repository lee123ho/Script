# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import font
import urllib.request
import xml.etree.ElementTree as ET
import tkinter.messagebox

com = None
areaNo = str()
timeNo = str()
DustTime = str()
WeatherData = []
WeatherView = []
DustData = []
DustView = []


def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375+315, y=5)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=35, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=315, y=0)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')


def InitMedicalInputLabel():
    global officeLabel, dayLabel, TempFont

    tiltetext = Label(window, font = TempFont, text = '[기상 지수]')
    tiltetext.pack()
    tiltetext.place(x=110, y=150)

    officeNum = Label(window, font = TempFont, text = '지점명')
    officeNum.pack()
    officeNum.place(x = 10, y = 220)
    officeLabel = Entry(window, font = TempFont, width = 26, borderwidth=5, relief = 'ridge')
    officeLabel.pack()
    officeLabel.place(x=10, y=250)

    dayNum = Label(window, font=TempFont, text='날짜(년월일시 ex)2018052706)')
    dayNum.pack()
    dayNum.place(x=10, y=310)

    dayNum1 = Label(window, font=TempFont, text='06, 18시만 가능')
    dayNum1.pack()
    dayNum1.place(x=10, y=375)
    dayLabel = Entry(window, font=TempFont, width=26, borderwidth=5, relief='ridge')
    dayLabel.pack()
    dayLabel.place(x=10, y=340)

def MedicalWeather():
    global imageLabel, button

    window.geometry("1100x500")
    InitRenderText()
    InitMedicalInputLabel()

    button = Button(window, font=TempFont, width=26, text='검색', command=ButtonAction)
    button.pack()
    button.place(x=10, y=440)

    imageLabel.place(x=100, y=20)


def ButtonAction():
    global areaNo, timeNo, DustTime, canvas, mapphoto
    RenderText.configure(state='normal')
    #RenderText.delete(0.0, END)

    if officeLabel.get() == "서울":
        areaNo = "1100000000"
    elif officeLabel.get() == "인천":
        areaNo = "2800000000"
    elif officeLabel.get() == "부산":
        areaNo = "2600000000"
    elif officeLabel.get() == "대전":
        areaNo = "3000000000"
    elif officeLabel.get() == "울산":
        areaNo = "3100000000"
    elif officeLabel.get() == "광주":
        areaNo = "2900000000"
    elif officeLabel.get() == "대구":
        areaNo = "2700000000"
    elif officeLabel.get() == "제주":
        areaNo = "5000000000"
    elif officeLabel.get() == "경기도":
        areaNo = "4100000000"
    elif officeLabel.get() == "강원도":
        areaNo = "4200000000"
    elif officeLabel.get() == "충청북도":
        areaNo = "4300000000"
    elif officeLabel.get() == "충청남도":
        areaNo = "4400000000"
    elif officeLabel.get() == "전라북도":
        areaNo = "4500000000"
    elif officeLabel.get() == "전라남도":
        areaNo = "4600000000"
    elif officeLabel.get() == "경상북도":
        areaNo = "4700000000"
    elif officeLabel.get() == "경상남도":
        areaNo = "4800000000"

    timeNo = dayLabel.get()
    DustTime = timeNo[0:8]
    print(timeNo)
    print(DustTime)

    canvas.delete("all")
    canvas.pack()
    canvas.place(x=700)
    canvas.create_text(80, 20, text="[전국 미세먼지]", font=TempFont)
    canvas.create_image(200, 250, image=mapphoto)
    canvas.create_text(50, 60, text=DustTime, font=TempFont)

    canvas.create_oval(320, 400, 330, 410, fill='white')
    canvas.create_oval(320, 430, 330, 440, fill='yellow')
    canvas.create_oval(320, 460, 330, 470, fill='red')

    canvas.create_text(355, 405, text='낮음', font=TempFont)
    canvas.create_text(355, 435, text='보통', font=TempFont)
    canvas.create_text(355, 465, text='높음', font=TempFont)

    Search()

    RenderText.configure(state='disabled')

def Search():
    global WeatherData, com, top
    WeatherData.clear()
    WeatherView.clear()
    DustData.clear()
    DustView.clear()
    try:
        Asthma()
        Brain()
        Skin()
    except:
        RenderText.delete(0.0, END)
        RenderText.insert(INSERT, "지점명 or 날짜 오류입니다. 다시 입력해주세요.")
    else:
        if com == 1:
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "==============================================")
            RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "지점명 - " + officeLabel.get())
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "검색 날짜 - " + dayLabel.get())
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "====================")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "기관질병 발생 위험도")
        RenderText.insert(INSERT, "\n\n")
        print(WeatherData)
        for x in range(9):
            if len(WeatherData[x]) == 3:
                WeatherView.append("측정하지 않음")
            elif WeatherData[x][3] == '0':
                WeatherView.append("낮음")
            elif WeatherData[x][3] == '1':
                WeatherView.append("보통")
            elif WeatherData[x][3] == '2':
                WeatherView.append("높음")
            elif WeatherData[x][3] == '3':
                WeatherView.append("매우 높음")
        RenderText.insert(INSERT, "오늘 - " + WeatherView[0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "내일 - " + WeatherView[1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "모레 - " + WeatherView[2])
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "====================")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "뇌졸증 발생 위험도")
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "오늘 - " + WeatherView[3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "내일 - " + WeatherView[4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "모레 - " + WeatherView[5])
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "====================")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "피부질환 발생 위험도")
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, "오늘 - " + WeatherView[6])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "내일 - " + WeatherView[7])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "모레 - " + WeatherView[8])
        com = 1

    try:
        Dust()
    except:
        canvas.create_text(70, 80, text="불러오기 오류", font=TempFont)

    try:
        if '2' <= WeatherData[0][3] <= '3':
            top = Toplevel(window, bd=2)
            top.title("기관지 주의")
            label = Label(top, text="기관지 질병 주의! 마스크 착용바람", bg='red',fg='white')
            label.pack()
    except:
        pass

    try:
        if '2' <= WeatherData[3][3] <= '3':
            top = Toplevel(window, bd=2)
            top.title("뇌졸증 주의")
            label = Label(top, text="뇌졸증 질환 주의!", bg='red',fg='white')
            label.pack()
    except:
        pass

    try:
        if '2' <= WeatherData[6][3] <= '3':
            top = Toplevel(window, bd=2)
            top.title("피부 질환 주의")
            label = Label(top, text="피부 질환 주의! 선크림 휴대 요망",bg='red',fg='white')
            label.pack()
    except:
        pass


def Asthma():
    global WeatherData

    url = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getAsthmaWhoList?"
    key = "serviceKey=G0ggqSF4z2N5hBVSDJu9WW5KknYmrBgA4rjnlOGWp32SYNBIvM55VGV%2FoikjOSONkX8TmT6CkncrTZJDm5QVcw%3D%3D"
    area = "&areaNo=" + areaNo
    time = "&time=" + timeNo
    api_url = url + key + area + time

    data = urllib.request.urlopen(api_url).read()

    filename = "Asthma.xml"
    f = open(filename, "wb")
    f.write(data)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("Body").findall("IndexModel"):
        WeatherData = ["오늘 " + a.findtext('today'), "내일 " + a.findtext('tomorrow'),
                       "모레 " + a.findtext('theDayAfterTomorrow')]


def Brain():
    global WeatherData

    url = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getBrainWhoList?"
    key = "serviceKey=G0ggqSF4z2N5hBVSDJu9WW5KknYmrBgA4rjnlOGWp32SYNBIvM55VGV%2FoikjOSONkX8TmT6CkncrTZJDm5QVcw%3D%3D"
    area = "&areaNo=" + areaNo
    time = "&time=" + timeNo
    api_url = url + key + area + time

    data = urllib.request.urlopen(api_url).read()

    filename = "Brain.xml"
    f = open(filename, "wb")
    f.write(data)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("Body").findall("IndexModel"):
        WeatherData.append("오늘 " + a.findtext('today'))
        WeatherData.append("내일 " + a.findtext('tomorrow'))
        WeatherData.append("모레 " + a.findtext('theDayAfterTomorrow'))


def Skin():
    global WeatherData

    url = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getSkinWhoList?"
    key = "serviceKey=G0ggqSF4z2N5hBVSDJu9WW5KknYmrBgA4rjnlOGWp32SYNBIvM55VGV%2FoikjOSONkX8TmT6CkncrTZJDm5QVcw%3D%3D"
    area = "&areaNo=" + areaNo
    time = "&time=" + timeNo
    api_url = url + key + area + time

    data = urllib.request.urlopen(api_url).read()

    filename = "Skin.xml"
    f = open(filename, "wb")
    f.write(data)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("Body").findall("IndexModel"):
        WeatherData.append("오늘 " + a.findtext('today'))
        WeatherData.append("내일 " + a.findtext('tomorrow'))
        WeatherData.append("모레 " + a.findtext('theDayAfterTomorrow'))

def Dust():
    global canvas, DustData
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?"
    key = "&serviceKey=G0ggqSF4z2N5hBVSDJu9WW5KknYmrBgA4rjnlOGWp32SYNBIvM55VGV%2FoikjOSONkX8TmT6CkncrTZJDm5QVcw%3D%3D"
    itemcode = "&itemCode=" + "PM10"
    gubun = "&dataGubun=" + "DAILY"
    condition = "&searchCondition=" + "MONTH"
    page = "&pageNo=" + "1"
    rows = "&numOfRows=" + "30"
    api_url = url + itemcode + gubun + condition + page + rows + key

    data = urllib.request.urlopen(api_url).read()

    filename = "Dust.xml"
    f = open(filename, "wb")
    f.write(data)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("body").find("items").findall("item"):
        if a.findtext('dataTime') == DustTime[0:4] + '-' + DustTime[4:6] + '-' + DustTime[6:8]:
            DustData = [a.findtext('seoul')]                #0
            DustData.append(a.findtext('busan'))
            DustData.append(a.findtext('incheon'))
            DustData.append(a.findtext('gwangju'))
            DustData.append(a.findtext('daejeon'))
            DustData.append(a.findtext('daegu'))            #5
            DustData.append(a.findtext('ulsan'))
            DustData.append(a.findtext('gyeonggi'))
            DustData.append(a.findtext('gangwon'))
            DustData.append(a.findtext('chungbuk'))
            DustData.append(a.findtext('chungnam'))         #10
            DustData.append(a.findtext('jeonbuk'))
            DustData.append(a.findtext('jeonnam'))
            DustData.append(a.findtext('gyeongbuk'))
            DustData.append(a.findtext('gyeongnam'))
            DustData.append(a.findtext('jeju'))             #15
    print(DustData)

    for y in range(16):
        if '0' <= DustData[y] < '33':
            DustView.append('white')
        elif '33' <= DustData[y] < '66':
            DustView.append('yellow')
        elif '66' <= DustData[y] < '101':
            DustView.append('red')

    # 서울
    canvas.create_oval(170, 105, 180, 115, fill=DustView[0])
    # 인천
    canvas.create_oval(145, 115, 135, 125, fill=DustView[2])
    # 경기
    canvas.create_oval(190, 135, 200, 145, fill=DustView[7])
    # 강원
    canvas.create_oval(260, 90, 270, 100, fill=DustView[8])
    # 대전
    canvas.create_oval(200, 205, 210, 215, fill=DustView[4])
    # 충북
    canvas.create_oval(220, 165, 230, 175, fill=DustView[11])
    # 충남
    canvas.create_oval(160, 190, 170, 200, fill=DustView[12])
    # 경북
    canvas.create_oval(290, 195, 300, 205, fill=DustView[13])
    # 대구
    canvas.create_oval(280, 245, 290, 255, fill=DustView[5])
    # 경남
    canvas.create_oval(260, 295, 270, 305, fill=DustView[14])
    # 부산
    canvas.create_oval(315, 295, 325, 305, fill=DustView[1])
    # 울산
    canvas.create_oval(325, 280, 335, 270, fill=DustView[6])
    # 전북
    canvas.create_oval(170, 255, 180, 265, fill=DustView[9])
    # 광주
    canvas.create_oval(162, 303, 172, 313, fill=DustView[3])
    # 전남
    canvas.create_oval(160, 345, 170, 355, fill=DustView[10])
    # 제주
    canvas.create_oval(140, 450, 150, 460, fill=DustView[15])


window = Tk()
window.geometry("350x200")
TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')

photo = PhotoImage(file="sun.png")  # 디폴트 이미지 파일
mapphoto = PhotoImage(file='map.png')

canvas = Canvas(window, width=800, height=800)
canvas.pack()
canvas.place(x=700)
canvas.create_text(133, 20, text="[전국 미세먼지](범위 한달)", font=TempFont)
canvas.create_image(200, 250, image=mapphoto)
canvas.create_text(50, 60, text=DustTime, font=TempFont)

canvas.create_oval(320, 400, 330, 410, fill='white')
canvas.create_oval(320, 430, 330, 440, fill='yellow')
canvas.create_oval(320, 460, 330, 470, fill='red')

canvas.create_text(355, 405, text='낮음', font=TempFont)
canvas.create_text(355, 435, text='보통', font=TempFont)
canvas.create_text(355, 465, text='높음', font=TempFont)

menubar = Menu(window)
tapmenu = Menu(menubar, tearoff=0)
tapmenu.add_command(label='보건 기상 지수', command=MedicalWeather)
menubar.add_cascade(label='메뉴', menu=tapmenu)

imageLabel = Label(window, image=photo)
imageLabel.pack(side = 'top')

window.config(menu=menubar)
window.mainloop()
