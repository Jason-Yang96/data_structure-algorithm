# 체인법으로 해시 함수 구현
from __future__ import annotations
from typing import Any, Type
import hashlib

"""노드 클래스 만들기"""
class Node:
    '''해시를 구성하는 노드'''


    def __init__(self, key: Any, value: Any, next: Node) -> None: #자기 참조형 노드(자신과 같은 자료형인 인스턴스를 참조)
        """초기화"""
        self.key = key #키
        self.value = value #값
        self.next = next #뒷쪽 노드

"""체인법으로 해시 클래스 구현"""
class ChainedHash:

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity # 해시 테이블 크기 지정
        self.tabel = [None] * self.capacity # 해시 테이블(리스트) 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        """주어진 key 값이 int인지 확인, 아니라면 변형 필요"""
        if isinstance(key, int):
            return key % self.capacity
        """key 값이 int가 아닌 경우 변형"""
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key) # 검색하고자 하는 키의 해시값
        p = self.table[hash] # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 뒤쪽 노드를 주목

        return None # 검색 실패
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 해시 테이블에 추가"""
        hash = self.hash_value(key) # 추가하는 key의 해시값
        p = self.table[hash] # 노드를 주목, 대체 이게 뭔 소리일까...

        while p is not None:
            if p.key == key:
                return False # 추가 실패. 있던 키
            p = p.next # 뒤쪽 노드를 주목
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp  # 노드를 추가
        return True #추가 성공
    
    def remove(self, key:Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key) # 삭제할 key의 해시값
        p = self.table[hash] # 노드를 주목, p가 노트 리스트를 주목시키는 것이 아닐까...
        pp = None # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key : # key를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            
