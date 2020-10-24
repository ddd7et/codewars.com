<?php

function in_asc_order($arr) {

  $pred = $arr[0];
  foreach($arr as $item)
  {
    if ($pred > $item)
      return false;

    $pred = $item;
  }
  return true;
}

?>
