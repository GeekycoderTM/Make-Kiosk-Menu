
#0. choice_main 함수 만들기
def choice_main():
    print('\n')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ == CNU 버거(ver.01) ==')
    print('■■ CNU 버거에 방문해주셔서 감사합니다.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 0.메인 메뉴')
    print('□■ 1.햄버거 세트')  # 햄버거, 사이드, 음료
    print('□■ 2.햄버거 단품')  # 햄버거
    print('□■ 3.사이드 메뉴')  # 사이드
    print('□■ 4.음료')  # 음료
    print('□■ 5.종료')  # 종료
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    while True:
        choice_num4 = int(input('>> 번호: '))
        if 1 <= choice_num4 <= 4:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num4


# 1.햄버거 세부 메뉴 선택하는 함수
def choice_burger():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  BURGER MENU')
    print('□■  1.치즈버거: 3,500원')
    print('□■  2.불고기버거: 3,000원')
    print('□■  3.새우버거: 2,500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>> 번호: '))
        if 1 <= choice_num <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num


# 2.사이드 세부 메뉴 선택하는 함수
def choice_side():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  SIDE MENU')
    print('□■  1.프렌치프라이: 1,500원')
    print('□■  2.치킨너겟: 2,000원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    while True:
        choice_num2 = int(input('>> 번호: '))
        if 1 <= choice_num2 <= 2:
            break
        else:
            print('# MSG: 1~2의 번호만 입력해주세요 :)')
    return choice_num2


# 3.음료 세부 메뉴 선택하는 함수
def choice_drink():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■  DRINK MENU')
    print('□■  1.코카콜라: 1,000원')
    print('□■  2.커피: 1,200원')
    print('□■  3.주스: 1,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    while True:
        choice_num3 = int(input('>> 번호: '))
        if 1 <= choice_num3 <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num3
