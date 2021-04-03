# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:41:54 2021

@author: ACER
"""

graf =  {'A':set(['Aisya','C','E']),
         'B':set(['E','D']),
         'C':set(['A','B','D']),
         'D':set(['B','F','K','I']),
         'E':set(['A','B']),
         'F':set(['D','G']),
         'G':set(['H','F','I']),
         'H':set(['G']),
         'I':set(['G','J']),
         'J':set(['I']),
         'K':set(['D','L','Risa'])}
         

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        jalur = queue.pop(0)
        state = jalur[-1]
        if state == tujuan:
            return jalur
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                queue.append(jalur_baru) 

            visited.add(state)

        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

def dfs(graf, mulai,tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:     
        jalur = stack.pop(-1)
        state = jalur[-1]
        if state == tujuan:
            return jalur
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                stack.append(jalur_baru) 

            visited.add(state)

        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
