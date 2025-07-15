// 연결 찾기
const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

const getSafeCount = (n, map, threshold) => {
  let count = 0;
  const m = map.map((row) => row.slice());

  const dirs = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  const search = ([y, x]) => {
    if (y < 0 || x < 0 || y >= n || x >= n || m[y][x] <= threshold) return;

    m[y][x] = threshold;
    for (const [dy, dx] of dirs) search([dy + y, dx + x]);
  };

  for (let i = 0; i < m.length; i++)
    for (let j = 0; j < m.length; j++) {
      if (m[i][j] > threshold) {
        search([i, j]);
        count++;
      }
    }

  return count;
};

rl.on("line", (line) => input.push(line)).on("close", function () {
  const n = +input[0];
  let max = 0;
  let min = 100;
  const map = input.slice(1).map((l) =>
    l.split(" ").map((v) => {
      max = Math.max(max, +v);
      min = Math.min(min, +v);
      return +v;
    })
  );

  let res = 0;
  for (let i = min - 1; i <= max; i++) {
    res = Math.max(res, getSafeCount(n, map, i));
  }

  console.log(res);
});
