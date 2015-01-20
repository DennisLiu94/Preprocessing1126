for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
do
g=$(echo $i*0.001|bc)
echo $g
./svm-train -c 2 -g $g -q ../train.small.dat {$i}".model"
./svm-predict ../train.small.dat {$i}".model" {$i}".res"
./svm-predict ../test1.small.dat {$i}".model" {$i}".res"
#./predict ../test2.small.dat {$i}".model" {$i}"2.res"
done
