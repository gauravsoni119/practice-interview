/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let count = 2;
	let countSay = ['1'];
	countSay.push('11');
	if (n <= 2) return countSay[n - 1];
	while(count !== n) {
		let str = countSay[count - 1];
		let res = '';
        let i = 0;
        while(i < str.length) {
			let j = str[i];
			let occurence = 0;
			while(str[i] === j) {
				occurence++;
				j = str[occurence + i];
			}
			res = res.concat(occurence, str[i]);
			i += occurence;
		}
		countSay.push(res);
		count++;

	}
	return countSay[n - 1];
};
