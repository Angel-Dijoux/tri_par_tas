module Headsort
  ( Headsort (..),
    trierParTas,
    trierListe,
    maximune,
    entasser,
  )
where

import Control.Concurrent.STM (check)
import Text.XHtml (lime)

newtype Headsort = Headsort {liste :: [Int]}

gauche :: Int -> Int
gauche i = i * 2 + 1

droite :: Int -> Int
droite i = i * 2 + 2

pere :: Int -> Int
pere i = (i - 1) `div` 2

estTas :: Headsort -> Bool
estTas hs = all (\i -> liste hs !! gauche i <= liste hs !! i && (droite i >= length (liste hs) || liste hs !! droite i <= liste hs !! i)) [0 .. ((length (liste hs) - 2) `div` 2)]

maximune :: Headsort -> Int -> Int -> Maybe Int
maximune hs i lim
  | g < lim && liste hs !! g > liste hs !! maxi = Just g
  | d < lim && liste hs !! d > liste hs !! maxi = Just d
  | otherwise = Nothing
  where
    maxi = i
    g = gauche i
    d = droite i

entasser :: Headsort -> Int -> Int -> Headsort
entasser hs i lim
  | maxi /= i = entasser (Headsort new_liste) maxi lim
  | otherwise = hs
  where
    Just maxi = maximune hs i lim
    temp = liste hs !! i
    new_liste = take i (liste hs) ++ [liste hs !! maxi] ++ drop (i + 1) (take len (liste hs)) ++ [temp] ++ drop (lim + 1) (liste hs)
    len = length (liste hs)

buildheap :: Headsort -> Headsort
buildheap hs = foldr (\i acc -> entasser acc i (length (liste hs))) hs [length (liste hs) - 1, length (liste hs) - 2 .. 0]

trierParTas :: Headsort -> [Int]
trierParTas hs = buildheap hs' `seq` foldr (\i acc -> let new_hs = entasser (Headsort (liste hs)) 0 i in new_hs `seq` acc ++ [head (liste new_hs)]) [] [(length (liste hs') - 1), (length (liste hs') - 2) .. 1]
  where
    hs' = Headsort (reverse (liste hs))

trierListe :: [Int] -> [Int]
trierListe xs = trierParTas hs
  where
    hs = Headsort xs