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

    public function maximun(int $i, int $lim): int
    {
        $maxi = $i;
        $g = $this->gauche($i);
        $d = $this->droite($i);
        if ($g < $lim && $this->liste[$g] > $this->liste[$maxi]) {
            $maxi = $g;
        }
        if ($d < $lim && $this->liste[$d] > $this->liste[$maxi]) {
            $maxi = $d;
        }
        return $maxi;
    }

    public function entasser(int $i, int $lim)
    {
        $maxi = $this->maximun($i, $lim);
        if ($maxi != $i) {
            $temp = $this->liste[$i];
            $this->liste[$i] = $this->liste[$maxi];
            $this->liste[$maxi] = $temp;
            $this->entasser($maxi, $lim);
        }
    }

    public function buildheap()
    {
        $newListe = array_reverse($this->liste);
        for ($i = count($newListe) - 1; $i >= 0; $i--) {
            $this->entasser($i, count($newListe));
        }
    }

    public function trierParTas(): array
    {
        $this->buildheap();
        for ($i = (count($this->liste) - 1); $i > 0; $i--) {
            $temp = $this->liste[0];
            $this->liste[0] = $this->liste[$i];
            $this->liste[$i] = $temp;
            $this->entasser(0, $i);
        }
        return $this->liste;
    }
}