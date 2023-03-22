<?php
namespace php;

require_once 'Headsort.php';

function generateRandomIntList(int $size): array
{
    $randomNumbers = array();
    for ($i = 0; $i < $size; $i++) {
        array_push($randomNumbers, rand(0, 100));
    }
    return $randomNumbers;
}

$liste = generateRandomIntList(15);
$obj = new Headsort($liste);


print(implode(',', $obj->trierParTas()));