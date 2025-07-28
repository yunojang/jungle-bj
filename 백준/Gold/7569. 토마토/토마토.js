// 멀티소스
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

class Queue {
  constructor() {
    this.items = [];
    this.head = 0;
    this.tail = 0;
  }
  get length() {
    return this.tail - this.head;
  }
  en(item) {
    this.items[this.tail++] = item;
  }
  de() {
    return this.head < this.tail ? this.items[this.head++] : null;
  }
}

const solution = (m, n, h, t) => {
  const queue = new Queue();

  let zCount = 0;
  for (let i = 0; i < h; i++)
    for (let j = 0; j < n; j++)
      for (let k = 0; k < m; k++) {
        if (t[i][j][k] == 0) zCount++;
        if (t[i][j][k] == 1) queue.en([i, j, k, 0]);
      }

  let days = 0;
  const dirs = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1],
  ];

  while (queue.length > 0) {
    const [z, y, x, day] = queue.de();
    days = Math.max(days, day);

    for (const [dz, dy, dx] of dirs) {
      const nz = dz + z,
        ny = dy + y,
        nx = dx + x;

      if (
        nz < 0 ||
        ny < 0 ||
        nx < 0 ||
        nz >= h ||
        ny >= n ||
        nx >= m ||
        t[nz][ny][nx] != 0
      )
        continue;

      t[nz][ny][nx] = 1;
      zCount--;
      queue.en([nz, ny, nx, day + 1]);
    }
  }

  return zCount > 0 ? -1 : days;
};

readline
  .on("line", function (line) {
    input.push(line);
  })
  .on("close", function () {
    const [m, n, h] = input[0].split(" ").map((v) => +v);
    const lines = input.slice(1);

    const t = [];
    for (let i = 0; i < lines.length; i++) {
      const floor = Math.floor(i / n);
      t[floor] ??= [];
      t[floor].push(lines[i].split(" ").map((v) => +v));
    }

    console.log(solution(m, n, h, t));
  });
