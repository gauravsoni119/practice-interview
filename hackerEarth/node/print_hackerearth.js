process.stdin.resume();

var i = 0, t = 0, len = 0, str = '', hackCount = 0, min = 10000000;
var hackerEarth = {
	h: 0,
	a: 0,
	c: 0,
	k: 0,
	e: 0,
	r: 0,
	t: 0
};

process.stdin.on('data', function (n) {
    if (t == 0) {
       len = n;
    } else {
        str = n.toString('utf8');
		hackCount = getHackerEarthCount(str);
		process.stdout.write(hackCount);
		process.exit();
    }
	t++;
});

function getHackerEarthCount (str) {
	for(c in str) {
		if(hackerEarth.hasOwnProperty(str[c])) {
			hackerEarth[str[c]] = hackerEarth[str[c]] + 1;
		}
	}
	hackerEarth['h'] = hackerEarth['h'] / 2;
	hackerEarth['a'] = hackerEarth['a'] / 2;
	hackerEarth['e'] = hackerEarth['e'] / 2;
	hackerEarth['r'] = hackerEarth['r'] / 2;
	for(c in hackerEarth) {
		if(hackerEarth[c] < min) {
			min = hackerEarth[c]
		}
	}
    return min.toString();
}