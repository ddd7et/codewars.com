<?php
function isIsogram($string) {
  
   for ($i=0;$i<strlen($string); $i++){
     for ($j=$i+1;$j<strlen($string); $j++){
       if (strtolower($string[$i])==strtolower($string[$j]))
        return false;
     }
   }

   return true;

}

?>
