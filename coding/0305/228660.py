import sys
input = sys.stdin.readline


#graph를 만든다음에 query문에 대해서 dfs search를 하고 
#찾은 file에 대해서 dictionary에 filename, 개수를 저장하기


#graph를 표현하기 위해서는 adjacency list 혹은 adjacency matrix
#하지만 이 문제는 tree로 구현해야 함..


class tree():
   
    #해당 값


    #tuple로 type까지 넣어주기
    def add(A, B, type):
        
        

    
#input 받기
file, folder = map(int,input().split())
for i in range(file+folder):
    A, B, type = map(str, input().split())
    tree.add(A, B, type)


#query 받기