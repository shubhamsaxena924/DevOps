<?php
$name=$_GET['t1'];
$gen=$_GET['gen'];
if($gen=='male') {
    echo "Welcome Mr. $name .";
} else {
    echo "Welcome Ms. $name .";
}
?>