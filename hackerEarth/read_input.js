function main(input) {
    //Enter your code here
    var processed_input = input.split('\n'),
        num = processed_input[0],
        str = processed_input[1];
    process.stdout.write(num * 2 + '\n' + str);
    //process.stdout.write("Hello World!");
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.on("end", function () {
   main(stdin_input);
});
