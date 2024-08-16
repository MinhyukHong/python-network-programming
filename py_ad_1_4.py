"""
Section 1
Multithreading - Thread(2) - Daemon, Join
Keyword - DaemonThread, Join

"""
"""

DaemonThread(데몬스레드)
(1).백그라운드에 실행
(2).메인스레드 종료 시 즉시 종료(트러블 슈팅 관리가 필요)
(3).주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM(가비지 컬렉션), 자동 저장
(4).일반 스레드는 작업 종료 시까지 실행

"""

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    
    for i in d:
        print(i)
    
    
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인
    # Daemon : Default False
    x = threading.Thread(target=thread_func, args=('First',range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Two',range(10000)), daemon=True)
    
    
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    
    # DaemonThread 확인
    print(x.isDaemon())
    
    # 주석 전후 결과 확인
    # x.join()
    # y.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: all done")