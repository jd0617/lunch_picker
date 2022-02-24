import numpy as np
import random

# 프로그램명 : MLPA Lunch Picker
# 제작자 : 정진원
# 제작 및 배포일 : 2022/01/05 (Wed)
# 버전정보 : Version 1.3
# Copyright ⓒ 2022 아신 정진원 All Rights Reserved

#단국대 주변, 식당 리스트
restaurant_all = ["학식", "옹고집", "김치짜글이", "손가네", "한솥", "칼제비", "맛의 전쟁", "꾸이한끼", "해피덮", "알촌",
                   "홍춘", "홍콩반점", "중국식당(2층)", "천향", "스부",
                   "겐코", "호식당", "우메다", "아리가또", "역전우동",
                   "일미", "브라더 양식당", "맘스터치",
                   "베트남 노상", "도스마스", "인도네팔", "투고박스"]
restaurant_korean = ["학식", "옹고집", "김치짜글이", "손가네", "한솥", "칼제비", "맛의 전쟁", "꾸이한끼", "해피덮", "알촌"]
restaurant_china = ["홍춘", "홍콩반점", "중국식당(2층)", "천향", "스부"]
restaurant_japan = ["겐코", "호식당", "우메다", "아리가또", "역전우동"]
restaurant_western = ["일미", "브라더 양식당", "맘스터치"]
restaurant_etc = ["베트남 노상", "도스마스", "인도네팔", "투고박스"]


#가중치는 1~5점 만점
restaurant_weight = {"학식":3, "옹고집":1, "김치짜글이":2, "손가네":3, "한솥":2, "꾸이한끼":2, "칼제비":2, "맛의 전쟁":3, "해피덮":3, "알촌":3,
                   "홍춘":1, "홍콩반점":2, "중국식당(2층)":3, "천향":4, "스부":3,
                   "겐코":2, "호식당":3, "우메다":3, "아리가또":2, "역전우동":4,
                   "일미":4, "브라더 양식당":4, "맘스터치":1,
                   "베트남 노상":1, "도스마스":1, "인도네팔":2, "투고박스":2}


def making_basket(category):
    choice_list = []

    if category == 1:
        for res_name in restaurant_all:
            for repeat in range(restaurant_weight[res_name]):
                choice_list.append(res_name)

    elif category == 2:
        for res_name in restaurant_korean:
            for repeat in range(restaurant_weight[res_name]):
                choice_list.append(res_name)

    elif category == 3:
        for res_name in restaurant_china:
            for repeat in range(restaurant_weight[res_name]):
                choice_list.append(res_name)

    elif category == 4:
        for res_name in restaurant_japan:
            for repeat in range(restaurant_weight[res_name]):
                choice_list.append(res_name)

    elif category == 5:
        for res_name in restaurant_western:
            for repeat in range(restaurant_weight[res_name]):
                choice_list.append(res_name)

    else:
        for res_name in restaurant_etc:
            for repeat in range(restaurant_weight[res_name]):
                choice_list.append(res_name)

    return random.choice(choice_list)



print("1: 전체 랜덤, 2:한식, 3:중식:, 4:일식:, 5:양식, 6:기타")
select = int(input("번호를 선택하세요: "))


print(making_basket(select))
