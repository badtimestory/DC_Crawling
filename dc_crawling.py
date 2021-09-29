# ------------------------------
# 실전주식투자 갤러리 크롤링
# ------------------------------
import logging
import datetime


# 로깅 환경 설정
testLogger = logging.getLogger('test')
testLogger.setLevel(logging.INFO)  # 로깅 수준 지정

# 날짜 레벨 [파일명:라인넘버] 메시지 형태로 출력
logging.basicConfig(
    format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d %I:%M:%S')


# ------------------------------
# 사용자에게 입력받아야할 정보 : 크롤링할 게시글의 날짜를 지정, 출력파일의 저장 경로
# ------------------------------
# 크롤링할 게시글의 날짜를 사용자가 지정
while True:
    input_user_date = input("날짜를 입력해주세요(yyyy-mm-dd): ")
    try:
        year, month, day = map(int, input_user_date.split('-'))
        testLogger.info("년: {}".format(year))
        testLogger.info("월: {}".format(month))
        testLogger.info("일: {}".format(day))

        input_user_date = datetime.date(year, month, day)
        testLogger.info(input_user_date)
        testLogger.info(type(input_user_date))
        break

    except:
        print("날짜 형식이 맞지않습니다.")


# 사용자에게 입력받아야할 정보 : 출력파일의 저장 경로


# ------------------------------
# 크롤링 프로그램 동작 : 글 URL, 글 제목, 글쓴이, 본문, 본문 이미지, 댓글 작성자, 댓글 내용 수집
# ------------------------------


# BeautifulSoup를 통해 html parse로 원하는 정보 수집


# ------------------------------
# 크롤링 출력 : json 확장자로 파일을 저장, 상위 폴더를 생성하고 이름은 입력받은 날짜로 지정하고 이미지는 별도로 저장
# ------------------------------
