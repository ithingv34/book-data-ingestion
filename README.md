# book-data-ingestion


### Usage

1. 깃허브 저장소를 clone 합니다.
```bash
$ git clone https://github.com/ithingv34/book-data-ingestion.git
```

2. 가상환경을 생성하고 활성화합니다.
```bash
$ cd book-data-ingestion
$ python -m venv [myenv]
$ source myenv/bin/activate
```

3. 의존성을 설치합니다.
```bash
$ pip install -r requirements.txt
```

4. selenium driver를 사용할 경우 시스템에 chrome을 설치해야 합니다.
- 이 스크립트는 ubuntu, debian에서 chrome을 설치하는 스크립트 입니다.
```bash
# Download the latest Gooogle Chrome Debian package on your system.
$ wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 

# execute the following commands to install Google Chrome from the locally downloaded file.
$ sudo apt update 
$ sudo apt install -f ./google-chrome-stable_current_amd64.deb
``` 

5. 스크립트를 실행합니다.
```bash
$ python src/main.py
```
