# -*- coding: utf-8 -*-

import urllib.request
import xml.etree.ElementTree as ET


areaNo = None
timeNo = None

def Asthma():
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

    #파싱하기
    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("Body").findall("IndexModel"):
        print('천식 폐질환 가능 지수')
        print("오늘 " + a.findtext('today'))
        print("내일 " + a.findtext('tomorrow'))
        print("모레 " + a.findtext('theDayAfterTomorrow'))
        print('----------------------')


def Brain():
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

    # 파싱하기
    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("Body").findall("IndexModel"):
        print('뇌졸증 가능 지수')
        print("오늘 " + a.findtext('today'))
        print("내일 " + a.findtext('tomorrow'))
        print("모레 " + a.findtext('theDayAfterTomorrow'))
        print('----------------------')


def Skin():
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

    # 파싱하기
    tree = ET.parse(filename)
    root = tree.getroot()

    for a in root.find("Body").findall("IndexModel"):
        print('피부 질환 가능 지수')
        print("오늘 " + a.findtext('today'))
        print("내일 " + a.findtext('tomorrow'))
        print("모레 " + a.findtext('theDayAfterTomorrow'))
        print('----------------------')


if __name__ == "__main__":
    areaNo = input('지점 번호 : ')
    print("측정 시간은 06, 18 ex)2018052706 2018년5월27일6시")
    timeNo = input("시간 : ")
    print("0 - 낮음 1 - 보통 2 - 높음 3 - 매우높음")
    Asthma()
    Brain()
    Skin()