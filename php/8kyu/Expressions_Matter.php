<?php
#https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/php
function expressionMatter($a, $b, $c) {

  $sum1 = $a*$b*$c;
  $sum2 = ($a+$b)*$c;
  $sum3 = $a*($b+$c);
  $sum4 = $a+$b+$c;

  return max($sum1, $sum2, $sum3, $sum4);

  }
?>
