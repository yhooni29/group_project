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
    def line(self):
        pass
        
print('hello')
print('')