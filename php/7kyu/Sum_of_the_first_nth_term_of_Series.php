<?php
function series_sum($n) {
  echo $n;
  echo "\n";
  if ($n == 0)
    return "0.00";
  $sum = 1;
  $add = 1;
  for ($i=2;$i<=$n;$i++) {
    $add += 3;
    $sum += 1/$add;
    #echo $add;
    #echo $sum;
    #echo " \n";
  }
  #echo $sum;
  return number_format((float)$sum, 2, '.', '');
}
?>
