// https://school.programmers.co.kr/learn/courses/30/lessons/155651

function solution(book_time) {
  // 예약 시간을 분으로 변환하고, 시작과 종료 시간을 기준으로 정렬
  const times = book_time
    .map((time) => {
      const start = time[0].split(":");
      const end = time[1].split(":");
      // 시작 시간과 종료 시간(청소 시간 10분 포함)을 분으로 변환
      return [
        parseInt(start[0]) * 60 + parseInt(start[1]),
        parseInt(end[0]) * 60 + parseInt(end[1]) + 10,
      ];
    })
    .sort((a, b) => a[0] - b[0] || a[1] - b[1]);

  // 각 방의 사용 가능한 최소 종료 시간을 저장
  let rooms = [];

  times.forEach((time) => {
    let placed = false;
    // 기존 방들을 순회하며 현재 예약을 배치할 수 있는지 확인
    for (let i = 0; i < rooms.length; i++) {
      if (time[0] >= rooms[i]) {
        // 예약 시작 시간이 방의 사용 가능 시간보다 늦다면,
        rooms[i] = time[1]; // 해당 방에 예약을 배치하고, 사용 가능 시간을 업데이트
        placed = true;
        break;
      }
    }
    // 기존 방들에 배치할 수 없는 경우, 새로운 방을 추가
    if (!placed) {
      rooms.push(time[1]);
    }
  });

  return rooms.length;
}
