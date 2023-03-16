<?php
namespace php;

require_once 'Headsort.php';

$liste = array(10, 12, 8, 7, 6, 5, 345, 3, 2, 1);
$obj = new Headsort($liste);


var_dump($obj->estTas());