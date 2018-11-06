function main(input) {
    //Enter your code here
    var output = '';
    for (ch in input) {
        if (input[ch] == input[ch].toUpperCase()) {
            output += input.charAt(ch).toLowerCase();
        }
        else {
            output += input.charAt(ch).toUpperCase();
        }
    }
    process.stdout.write(output);
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
    main(stdin_input);
    process.exit();
});

process.on("SIGINT", function () {
   process.exit();
});

