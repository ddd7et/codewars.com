<?php
#Simple, remove the spaces from the string, then return the resultant string.
function no_space(string $s): string {
  $new_string = "";

  for ($i=0;$i<strlen($s);$i++){
   if ($s[$i] != " ")
     $new_string = $new_string.$s[$i];

  }
  return $new_string;

}

?>
