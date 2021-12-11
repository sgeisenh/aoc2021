<?hh //strict

$lines = explode("\n", file_get_contents("../input/01.txt"));
$numbers = array_map($line ==> (int)trim($line), $lines);

$contents = await File\open_read_only("../input/01.txt");
$numbers = Vec\map(Str\split($contents, "\n"), $line ==> Str\to_int(Str\trim($line)));

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

echo "Part one: ", partOne($numbers), "\n";
echo "Part two: ", partTwo($numbers), "\n";

?>