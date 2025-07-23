const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const n = input[0];
  let list = input.slice(1).map((v) => v.split(" ").map((v) => +v));

  const sorted = list.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
  let count = 0;
  let lastEnd = 0;
  sorted.forEach(([s, e]) => {
    if (s >= lastEnd) {
      lastEnd = e;
      count++;
    }
  });

  console.log(count);
});
