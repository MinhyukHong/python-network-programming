"""
Section 3
Concurrency, CPU Bound vs I/O Bound - Blocking vs Non-Blocking IO
Keyword - Blocking IO, Non-Blocking IO, Sync, Async

"""
"""

Blocking IO vs Non-blocking IO

    Blocking IO
    - 시스템 콜 요청시 -> 커널 IO 작업 완료 시까지 응답 대기
    - 제어권(IO 작업) -> 커널 소유 -> 응답(Response) 전까지 대기(Block) -> 다른 작업 수행 불가(대기)
    
    Non-Blocking IO
    - 시스템 콜 요청시 -> 커널 IO 작업 완료 여부 상관 없이 즉시 응답
    - 제어권(IO 작업) -> 유저 프로세스 -> 다른 작업 수행 가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료 여부 확인

    Async vs Sync
    
        Async : IO 작업 완료 여부에 대한 Noty는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수)
        Sync : IO 작업 완료 여부에 대한 Noty는 유저프로세스(호출하는 함수) -> 커널(호출되는 함수)
    
"""