<?php
#Complete the solution so that it reverses the string passed into it.
#'world'  =>  'dlrow'
  function solution($str) {
  $new_s = "";

  for ($i=strlen($str)-1;$i>=0;$i--)
    $new_s = $new_s.$str[$i];

  return $new_s;
  }

?>
