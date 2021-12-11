use namespace HH\Lib\{C, File, Str, Vec};

function partOne(vec<int> $numbers) {
  $count = 0;
  for ($i = 1; $i < C\count($numbers); $i++) {
    if ($numbers[$i] > $numbers[$i - 1]) {
      $count++;
    }
  }
  return $count;
}

function partTwo(vec<int> $numbers) {
  $count = 0;
  for ($i = 3; $i < C\count($numbers); $i++) {
    if ($numbers[$i] > $numbers[$i - 3]) {
      $count++;
    }
  }
  return $count;
}

<<__EntryPoint>>
async function run(): Awaitable<void> {
  $contents = await File\open_read_only("../input/01.txt")->readAllAsync();
  $numbers =
    Vec\map(Str\split($contents, "\n"), $line ==> Str\to_int(Str\trim($line)));
  echo "Part one: ", partOne($numbers), "\n";
  echo "Part two: ", partTwo($numbers), "\n";
}
