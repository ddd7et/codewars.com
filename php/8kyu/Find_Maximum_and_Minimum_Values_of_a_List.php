<?php
//https://www.codewars.com/kata/577a98a6ae28071780000989/train/php
//Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

function maximum($array) {

  $max_elem = $array[0];
  for ($i=0; $i < sizeof($array); ++$i)
  {
    if ($array[$i] > $max_elem) {
      $max_elem = $array[$i];
      }
  }
  return $max_elem;

}
function minimum($array) {

  $max_elem = $array[0];
  //echo "max=$max_elem ";
  for ($i=0; $i < sizeof($array); ++$i)
  {
    if ($array[$i] < $max_elem)
      $max_elem = $array[$i];
  }
  //echo "max=$max_elem";
  return $max_elem;

}
?>
