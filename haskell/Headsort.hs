module Headsort (
    Headsort(..),
    droite,
) where

data Headsort = Headsort { liste :: [Int] }

gauche :: Int -> Int
gauche i = i * 2 + 1

droite :: Int -> Int
droite i = i * 2 + 2

pere :: Int -> Int
pere i = (i - 1) `div` 2