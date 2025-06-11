
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
        api_key="<OPENROUTER KEY>",
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
        api_key="<OPENROUTER KEY>",
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
        api_key="<OPENROUTER KEY>",
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


choice = int(input('중앙대학교 근처 교통 안내 서비스입니다. 원하는 정보의 번호를 선택하세요\n1.9호선 지하철 안내\n2.동작01 버스 안내'))
if choice == 1:
# 지하철 안내하는 함수
   print('hello')                     
elif choice == 2:                                                                             # 원하는 서비스 선택
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