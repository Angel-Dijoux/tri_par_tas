import Headsort

main :: IO()
main = do
    let myObj = Headsort { liste = [3,4,6,1] }
    let droite2 = test 2
    print droite2 