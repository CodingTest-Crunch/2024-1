// https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=javascript#

function solution(progresses, speeds) {
  var answer = [];
  let tempArr = [];

  for (let i = 0; i < speeds.length; i++) {
    progresses[i] = Math.ceil((100 - progresses[i]) / speeds[i]);
  }

  for (let i = 0; i < progresses.length; i++) {
    if (tempArr.length == 0 || progresses[i] <= tempArr[0]) {
      tempArr.push(progresses[i]);
    } else {
      answer.push(tempArr.length);
      tempArr = [];
      tempArr.push(progresses[i]);
    }

    if (i == progresses.length - 1) {
      answer.push(tempArr.length);
    }
  }

  return answer;
}
