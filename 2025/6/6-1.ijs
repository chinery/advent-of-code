dbr 1
filename =: '6.txt'
input =: toJ 1!:1 < filename 

data =: <;._2 input
isMult =: {."1 '*' = > cut {. > _1 {. data
operands =: > 0 ". each _1 }. data

sum =: +/  (-. isMult) #"1 operands
mult =: */ isMult #"1 operands

echo +/ mult, sum