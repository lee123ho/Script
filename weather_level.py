# -*- coding: utf-8 -*-

import urllib.request
import xml.etree.ElementTree as ET


areaNo = None

def Asthma():
    url = "http://newsky2.kma.go.kr/iros/RetrieveWhoIndexService2/getAsthmaWhoList?"
    key = "serviceKey=G0ggqSF4z2N5hBVSDJu9WW5KknYmrBgA4rjnlOGWp32SYNBIvM55VGV%2FoikjOSONkX8TmT6CkncrTZJDm5QVcw%3D%3D"
    area = "&areaNo=" + "1100000000"
    time = "&time=" + "2018052706"
    api_url = url + key + area + time

    data = urllib.request.urlopen(api_url).read()

    filename = "sample2.xml"
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
    area = "&areaNo=" + "1100000000"
    time = "&time=" + "2018052706"
    api_url = url + key + area + time

    data = urllib.request.urlopen(api_url).read()

    filename = "sample2.xml"
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
    area = "&areaNo=" + "1100000000"
    time = "&time=" + "2018052706"
    api_url = url + key + area + time

    data = urllib.request.urlopen(api_url).read()

    filename = "sample2.xml"
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
    Asthma()
    Brain()
    Skin()