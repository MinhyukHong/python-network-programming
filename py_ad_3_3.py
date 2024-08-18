"""
Section 3
Concurrency, CPU Bound vs I/O Bound - Multiprocessing vs Threading vs AsyncIO
Keyword - CPU Bound, I/O Bound, AsyncIO

"""
"""

CPU Bound vs I/O Bound

    CPU Bound
    - 프로세스 진행 -> CPU 속도에 의해 제한(결정) -> 행렬 곱, 고속 연산, 압축 파일, 집합 연산 등
    - CPU 연산 위주 작업
    
    I/O Bound
    - 파일쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 작업에 의해서 병목(수행시간)이 결정
    - CPU 성능 지표가 수행시간 단축으로 크게 영향을 끼치지 않음.
    
메모리 바인딩, 캐시바운딩

작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요

최종 비교

- Multiprocessing : Multiple processes, 고가용성(CPU) Utilization -> CPU-Bound -> 10개 부엌, 10명 요리사, 10개 요리
- Threading : Single(Multi) process, Multiple threads, OS decides task switching -> Fast I/O Bound -> 1개 부엌, 10명 요리사, 10개 요리
- AsyncIO : Single process, single thread, cooperative multitasking, tasks cooperatively decide switching -> Slow I/O Bound -> 1개 부엌, 1명 요리사, 10개 요리

"""