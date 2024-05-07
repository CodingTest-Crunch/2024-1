// https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=javascript

function solution(numbers, target) {
    let count = 0; // 타겟 넘버를 만들 수 있는 방법의 수를 저장할 변수
  
    // 재귀 함수 정의
    function dfs(index, sum) {
      // 모든 숫자를 사용했을 때 (기저 조건)
      if (index === numbers.length) {
        // 현재 합이 타겟 넘버와 같다면 경우의 수 증가
        if (sum === target) {
          count++;
        }
        return;
      }
      
      // 현재 숫자를 더하는 경우
      dfs(index + 1, sum + numbers[index]);
      // 현재 숫자를 빼는 경우
      dfs(index + 1, sum - numbers[index]);
    }
    
    // 재귀 함수 최초 호출
    dfs(0, 0);
  
    return count;
  }
  