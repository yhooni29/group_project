class SubwayLine9:
    def __init__(self,line_9):
        self.line_9 = line_9

normal_9 = [
        "개화", "김포공항", "공항시장", "신방화", "마곡나루", "양천향교",
        "가양", "증미", "등촌", "염창", "신목동", "선유도", "당산",
        "국회의사당", "여의도", "샛강", "노량진", "노들", "흑석", "동작",
        "구반포", "신반포", "고속터미널", "사평", "신논현", "언주", "선정릉",
        "삼성중앙", "봉은사", "종합운동장", "삼전", "석촌고분", "석촌",
        "송파나루", "한성백제", "올림픽공원", "둔촌오륜", "중앙보훈병원"]
express_9 = [
        "김포공항", "가양", "염창", "당산", "여의도",
        "노량진", "동작", "고속터미널", "신논현",
        "선정릉", "봉은사", "종합운동장", "석촌",
        "올림픽공원", "중앙보훈병원"] 

class Normal_9(SubwayLine9):
    def __init__(self,line_9,normal):
        SubwayLine9.__init__(self,line_9)
        self.normal = normal

    def normal_station(self):             #일반 9호선역 출력 함수
        print(normal_9)
    
    def normol_where(self,location):         #현재역 기준으로 앞뒤 역 출력 함수
        if location in normal_9:
            now_station = normal_9.index(location)
            next_station = normal_9[now_station+1]
            back_station = normal_9[now_station-1]
            print(f'{back_station} - {location} - {next_station}')
        else:
            print('9호선에 존재하지 않는 역입니다.')

    def normal_destination(self,location,destination):    #도착역까지 얼마나 걸리는지 알려주는 함수
        if destination in normal_9:
            if location in normal_9:
                now_station = normal_9.index(location)
                destination_station = normal_9.index(destination)
                distinct = (destination_station - now_station)*2
                if distinct>=0:
                    print('남은 역은 ')
                    for i in range(now_station,destination_station+1):
                        print(normal_9[i],end='-')
                    print(f'입니다.\n 총 소요시간은 {distinct}분 입니다.')
                else:
                    normal_9.reverse()
                    a=','.join(map(str,normal_9))
                    renormal_9 = a.split(',')
                    now_station = renormal_9.index(location)
                    destination_station = renormal_9.index(destination)
                    print('남은 역은', end=' ')
                    for i in range(now_station,destination_station+1):
                        print(renormal_9[i],end='-')                   
                    print(f'입니다.\n 총 소요시간은 {abs(distinct)}분 입니다.')
            else: 
                print('출발지가 9호선에 존재하지 않는 역입니다.')
        else:
            print('도착지가 9호선에 존재하지 않는 역입니다.')

class Express_9(SubwayLine9):
    def __init__(self, line_9,express):
        SubwayLine9.__init__(self,line_9)
        self.express = express

    def express_station(self):             #9호선 급행역 출력  
        print(express_9)

    def express_where(self,location):         #현재역 기준으로 앞뒤 역 출력 함수
        if location in express_9:
            now_station = express_9.index(location)
            next_station = express_9[now_station+1]
            back_station = express_9[now_station-1]
            print(f'{back_station} - {location} - {next_station}')
        else:
            print('9호선에 존재하지 않는 역입니다.')

    def express_destination(self,location,destination):    #도착역까지 얼마나 걸리는지 알려주는 함수
        if destination in express_9:
            if location in express_9:
                now_station = express_9.index(location)
                destination_station = express_9.index(destination)
                distinct = abs(destination_station - now_station)*3
                if distinct>=0:
                    print('남은 역은 ')
                    for i in range(now_station,destination_station+1):
                        print(express_9[i],end='-')
                    print(f'입니다.\n 총 소요시간은 {distinct}분 입니다.')
                else:
                    express_9.reverse()
                    a=','.join(map(str,express_9))
                    reexpress_9 = a.split(',')
                    now_station = reexpress_9.index(location)
                    destination_station = reexpress_9.index(destination)
                    print('남은 역은 ',end=' ')
                    for i in range(now_station,destination_station+1):
                        print(reexpress_9[i],end='-')                   
                    print(f'입니다.\n 총 소요시간은 {abs(distinct)}분 입니다.')
            else: 
                print('출발지가 9호선급행에 존재하지 않는 역입니다.')
        else:
            print('도착지가 9호선급행에 존재하지 않는 역입니다.')
def subwaynavigate():   
    while True:
        q= input('9호선 안내 서비스입니다. 원하는 정보를 선택하세요.\n'
    '1. 일반열차 정보 \n2. 급행열차 정보')
        p= Normal_9('line_9','normal')
        ep = Express_9('line_9','express')  
        if q == '1':
            a=input('9호선 일반열차 안내 서비스입니다. 원하는 정보를 선택하세요.\n'
                '1.노선도\n'\
                '2.목적지까지 걸리는 시간 및 남은 정류장\n'\
                '3.현재역 기준 앞뒤 역 안내')
            if  a== '1':
                 p.normal_station()
                 break
            elif a=='2':
                i= input('현재역과 도착역을 적어주세요.(현재역,도착역)')
                si=i.split(',')
                location=si[0]
                destination=si[1]
                p.normal_destination(location,destination)
                break
            elif a=='3':
                i=input('현재역을 입력하세요')
                location=i
                p.normol_where(location)
                break  
            else:
                 print('다시입력하세요')
        if q=='2':
            a=input('9호선 급행열차 안내 서비스입니다. 원하는 정보를 선택하세요.\n'
                '1.노선도\n' \
               '2.목적지까지 걸리는 시간 및 남은 정류장\n'\
               '3.현재역 기준 앞뒤 역 안내')
            if  a== '1':
                ep.express_station()
                break
            elif a=='2':
               i= input('현재역과 도착역을 적어주세요.(현재역,도착역)')
               si=i.split(',')
               location=si[0]
               destination=si[1]
               ep.express_destination(location,destination)
               break
            elif a=='3':
               i=input('현재역을 입력하세요')
               location=i
               ep.express_where(location)
               break  
            else:
                print('다시입력하세요')
        else:
            print('다시입력하세요')

Dongjak_station = ["달마사", "중앙빌리지.동부센트레빌", "은로초등학교",
    "중대부속초등학교", "중앙대병원후문.흑석시장", "중앙대병원", "중앙대정문",
    "중앙대중문", "중앙대후문", "이화약국", "동작상도국주도서관", "상도터널상도동",
    "상도역.하나은행", "상도노빌리티아파트", "건영아파트", "우성아파트",
    "강남교회.오거리", "노량진한국법학교육원", "노량진역", "노량진수산시장.CTS기독교TV",       #동작01 노선도
    "현대아파트.유한양행", "대방역2번출구앞", "현대아파트", "노량진수산시장.CTS기독교TV",
    "노량진역", "노량진신한은행", "강남교회.오거리", "우성아파트", "신동아리버파크",
    "상도노빌리티아파트", "상도역", "중대후문입구", "중앙대후문", "중앙대중문",
    "중앙대정문", "중앙대병원", "중앙대병원후문.흑석시장", "중대부속초등학교",
    "은로초등학교", "중앙빌리지.동부센트레빌","유앤미아파트"]

def destionation():
    from openai import OpenAI
                                                                                      #목적지까지 걸리는 시간 및 남은 정류장
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<OPEN ROUTER KEY>",
    )

    messages = [
        {
            "role": "system",
            "content": (
                "대한민국, 서울 동작구의 마을 버스인 동작 01의 노선과 정류장을 파악해서\
                사용자가 출발지와 목적지를 알려주면 도착까지 시간이 얼마나 걸리는지, 앞으로 몇 정류장 남았는지 한국어로 알려주세요."
            )
        }
    ]

    while True:
        start = input('출발지: ').strip()
        destination = input('목적지: ').strip()
        messages.append({
            "role": "user",
            "content": f"출발지는 {start}이고, 목적지는 {destination}입니다."
        })

        completion = client.chat.completions.create(
            model="meta-llama/llama-3.3-8b-instruct:free",
            messages=messages
        )
        print(completion.choices[0].message.content)
        break

def time():
    from openai import OpenAI
                                                                                      #첫차 및 막차 시간
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<OPEN ROUTER KEY>"
    )

    messages = [
        {
            "role": "system",
            "content": (
                "대한민국, 서울 동작구의 마을 버스인 동작 01의 정류장마다의 첫차 및 막차 시간을 파악해서\
                사용자가 출발지를 알려주면 첫차 및 막차시간이 언제인지를 한국어로 알려주세요."
            )
        }
    ]

    while True:
        start = input('출발지: ').strip()
        messages.append({
            "role": "user",
            "content": f"출발지는 {start}입니다."
        })

        completion = client.chat.completions.create(
            model="meta-llama/llama-3.3-8b-instruct:free",
            messages=messages
        )
        print(completion.choices[0].message.content)
        break

def transfer():
    from openai import OpenAI
                                                                                      #지하철로 환승가능한 정류장
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<OPEN ROUTER KEY>",
    )

    messages = [
        {
            "role": "system",
            "content": (
                "대한민국, 서울 동작구의 마을 버스인 동작 01의 정류장 주변 지하철 역을 파악해서\
                사용자가 원하는 호선을 알려주면 그 호선의 지하철로 환승가능한 정류장이 어디인지를 한국어로 알려주세요."
            )
        }
    ]

    while True:
        line = int(input('원하는 지하철 호선을 숫자만 입력해주세요: '))
        messages.append({
            "role": "user",
            "content": f"{line}호선 지하철로 환승가능한 정류장을 알고싶습니다."
        })

        completion = client.chat.completions.create(
            model="meta-llama/llama-3.3-8b-instruct:free",
            messages=messages
        )
        print(completion.choices[0].message.content)
        break
    
def busnavigate():      
    while True:
       question = int(input('동작 01 안내 서비스입니다. 원하는 정보의 번호를 선택하세요.\n1.동작01 노선도\n2.목적지까지 걸리는 시간 및 남은 정류장 \n3.첫차 및 막차 시간\n4.지하철로 환승가능한 정류장'))
       if question == 1:
          print('-'.join(Dongjak_station))
       elif question == 2:
           destionation()
       elif question == 3:
           time()        
       elif question == 4:
           transfer()
       break


while True:
    first_q = input('원하는 대중교통 안내를 선택하세요.\n' \
'1.9호선 지하철\n' \
'2.동작01 버스')
    if first_q == '1':
        subwaynavigate()
        break
    elif first_q == '2':
        busnavigate()
        break
    else:
        print('다시입력하세요') 

       
    

    