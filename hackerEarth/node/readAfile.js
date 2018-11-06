process.stdin.resume();

var i = 0, t = 0;

process.stdin.on('data', function (n) {
    console.log(i);
    if (t == 0) {
       t = n;
    } else {
         if (i++ < t) {
             process.stdout.write(Factorial(n).toString());
             if (i == t) {
                 process.exit();
             }
         } else {
             process.exit();
         }
    }
});

function Factorial (n) {
    if (n > 1) {
        n *= Factorial(n - 1);
    }
    return n;
}