# 도커(Docker)
    컨테이너(Container) 이동을 주도하는 회사, 클라우드의 모든 애플리케이션을 처리할 수 있는 컨테이너 플랫폼 제공.

    컨테이너 : 다양한 OS에 여러 애플리케이션이 올려져 있는 것.

# 이미지 빌드
    $ docker run -d -p 80:80 docker/getting-started

   getting-started : 이미지 네임
   -d (detached) : 백그라운드 모드
   -p (port) : <호스트포트>:<컨테이너포트>

# MySQL
    다른 유저가 빌드한 이미지를 설치 없이 바로 사용할 수 있는 기능.

    도커 생성
    $ docker run --name fastapi-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

    --name : 컨테이너 이름
    -e : 환경 변수
    -d : 백그라운드 모드
    -P : port
    mysql8.0 : 이미지 이름
    --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci : 컨테이너를 실행할 때 사용하는 명령어.

    접속 방법
    $ docker exec -it fastapi-mysql mysql -uroot -p

    exec : 실행
    it : 실행시 인터렉션활성화(attach로 접속하는거와 같음)
    fastapi-mysql : 컨테이너 이름
    -uroot : u+id
    -p : password


# RDB 
    객체와 관계를 맵핑해주는 프로그램.

        main.py
        database.py : SQLAlchemy 설정
        model.py : SQLAlchemy Models
        schemas.py : Pydantic Models

    PyMySQL : MySQL연결을 위한 드라이버.


# Form
    HTML의 태그.
    미디어 타입 : application/x-www-form-urlencoded
    단, json 형식은 받을 수 없음.(미디어타입이 다르기 때문)

# 파일 처리
    1.바이트 스트림
        bytes 명시 -> 다양한 파일에 자세한 정보(확장자,이름 등)를 받을 수 없음.
    2.업로드 파일
        파일에 자세한 정보 출력을 받을 수 있음.
        파이썬과 비슷한 write, read, seek, close 같은 비동기 메소드를 지원.(await)

        await-async함수와 함께 쓰임.
        file-like_obj = file.file

# 파일 저장
    from tempfile import NamedTemporaryFile
    from typing import IO

    NamedTemporaryFile : 임의로 파일을 생성

# 에러 처리
    Exception: 모든 파이썬에 에러 상속받음.
    exception_handler(SomeError): 요청받은(requests) 에러 처리.
    요청 값은 (_)을 이용해서 생략 가능.

    HTTPException : 자동으로 에러 코드와,내용,해더를 응답해줌.
        class SomeFasta(HTTPException):
        def __init__(
            self,
            status_code: int,
            detail: Any = None,
            headers: Optional[Dict[str, Any]] = None,
            ) -> None:
            super().__init__(
                status_code, detail, headers)








