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

    $ docker run --name fastapi-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

    --name : 컨테이너 이름
    -e : 환경 변수
    -d : 백그라운드 모드
    mysql : 이미지 이름
    --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci : 컨테이너를 실행할 때 사용하는 명령어.

    접속 방법
    $ docker exec -it fastapi-mysql mysql -uroot -p

# RDB 
    객체와 관계를 맵핑해주는 프로그램.

    main.py
    database.py : SQLAlchemy 설정
    model.py : SQLAlchemy Models
    schemas.py : Pydantic Models