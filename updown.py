"""
"Up & Down 게임"

술자리 게임중에 소주병뚜껑에 있는 숫자맞추기 게임이랑 똑같습니다.

1~100 사이의 숫자를 맞춰야합니다. 정답이 내가 말한숫자보다 크면 Up, 정답이 내가 말한숫자보다 작으면 Down.

도전횟수: 6번 (도전횟수가 0이 되면 종료)

1. 컴퓨터는 1~100 사이의 숫자 한 개를 저장 -> A

2. 유저는 1~100 사이의 숫자를 입력 -> B
   예외처리1: 숫자 이외의 값을 입력했을 때 예외처리
   예외처리2: 1~100 범위가 아닌 숫자를 입력했을 때 예외처리

3. 컴퓨터가 생각한 숫자와 유저가 입력한 숫자를 비교
   case1: A=B 이면 정답이라고 출력
   case2: A>B 이면 Up 이라고 출력, 남은 도전 횟수 출력
   case3: A<B 이면 Down 이라고 출력, 남은 도전 횟수 출력

4. 정답을 맞추거나 남은 횟수가 0 이 되면 도전 종료

5. 도전 종료 후 "재도전 하시겠습니까?(y/n)" 출력
   case1: y 입력하면 게임 재도전
   case2: n 입력하면 게임 종료
   case3: y,n 이외의 값을 입력했을 때 "다시 입력해주세요" 출력
"""