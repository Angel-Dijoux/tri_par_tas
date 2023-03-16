<?php

namespace php;

class Headsort
{
    private array $liste;
    public function __construct(array $liste)
    {
        $this->liste = $liste;
    }

    public function gauche(int $i): int
    {
        return $i * 2 + 1;
    }

    public function droite(int $i): int
    {
        return $i * 2 + 2;
    }

    public function sizeOfListe(): int
    {
        return count($this->liste);
    }

    public function estTas(): bool
    {
        for ($i = 1; $i < ($this->sizeOfListe() - 2) / 2; $i++) {
            if ($this->liste[$this->gauche($i)] > $this->liste[$i]) {
                return false;
            }
            if ($this->droite($i) < count($this->liste) && $this->liste[$this->droite($i)] > $this->liste[$i]) {
                return false;
            }
        }
        return true;
    }
}