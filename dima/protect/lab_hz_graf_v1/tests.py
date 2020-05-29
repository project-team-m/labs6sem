
from random import randint // вроде библиотека не импортируется
var n = 1000000;

var p = 0;
double x, y;
for (var i = 0; i < n; ++i){
    x = rand.Next(1001) / 1000;
    y = rand.Next(1001) / 1000;
    if x * x + y * y < 1{
        p++;
    }
}

Console.WriteLine(p / n * 4);