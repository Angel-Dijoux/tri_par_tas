import Headsort

main :: IO ()
main =
  do
    let hs = Headsort [3, 4, 6, 1, 5, 6, 7, 7]
    print (maximune hs 0 7)
