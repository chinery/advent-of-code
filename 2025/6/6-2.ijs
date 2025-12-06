filename =: '6.txt'
input =: toJ 1!:1 < filename 

data =: [;._2 input
isMult =: '*' = , > cut , _1 {. data
operands =: <;._1 (_1, (_1 ". |: _1 }. data))

sum =: +/ > +/ each (-. isMult) # operands
mult =: +/ > */ each isMult # operands

echo +/ mult, sum
