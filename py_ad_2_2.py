"""
Section 2
Parellelism with Multiprocessing - multiprocessing(1) - Join, is_alive
Keyword - multiprocessing, processing state

"""
from multiprocessing import Process
import time
import logging

def proc_func(name):
    print('Sub-Process {}: starting'.format(name))
    time.sleep(3)
    print('Sub-Process {}: finishing'.format(name))


def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))

    logging.info('Main-Process: before creating Process')
    
    # 프로세스
    p.start()
    
    logging.info('Main-Process: During Process')
    
    # logging.info('Main-Process: Terminated Process')
    # p.terminate() ## 강제적으로 프로세스 kill
    
    logging.info('Main-Process: Joined Process')
    p.join()
    
    # 프로세스 상태 확인
    print(f'Process p is alive: {p.is_alive()}')
    
# 메인시작
if __name__ == '__main__':
    main()