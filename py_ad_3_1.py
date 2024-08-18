"""
Section 3
Concurrency, CPU Bound vs I/O Bound - What is Concurrency
Keyword - Concurrency

"""
"""

Concurreny(동시성)

- CPU 가용성을 극대화하기 위해 Parellelism 의 단점 및 어려움을 소프트웨어(구현) 레벨에서 해결하기 위한 방법
- 싱글코어에 멀티스레드 패턴을 작업을 처리
- 동시 작업에 있어서 일정 양을 처리 후 다음 작업으로 넘기는 방식
- 즉, 제어권을 주고 받으며 작업을 처리하는 패턴, 병렬적은 아니나, 유사한 처리 방식

Concurrency(동시성) vs Parellelism(병렬성)

동시성 : 논리적, 동시 실핻ㅇ 패턴(논리적), 싱글코어, 멀티 코어에서 실행 가능, 한 개의 작업을 공유 처리, 디버깅 매우 어려움, Mutext, DeadLock
병렬성 : 물리적, 물리적으로 동시 실행, 멀티코어에서 구현 가능, 주로 별개의 작업 처리, 디버깅 어려움, OpenMP, MPI, CUDA

"""