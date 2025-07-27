# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  list = []
  for i in range(N):
    if C[i] == 'A':
      list.append('B')
    else:
      list.append('A')
    
  return ''.join(list)


N = 3
C = 'ABA'

print(getWrongAnswers(N, C))