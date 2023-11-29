// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S) {
    // Implement your solution here

    let result = S.split('');
        for (let i = 0; i < result.length - 1; i++) {
        // Check if adjacent digits can be replaced
        if (parseInt(result[i]) + parseInt(result[i + 1]) <= 9) {
            // Replace the two digits with their sum
            result.splice(i, 2, (parseInt(result[i]) + parseInt(result[i + 1])).toString());
            // Move the index back to check the previous pair
            i = Math.max(i - 2, -1);
        }
    }
    return result.join('');
}

function solution(S) {
    let result = S.split('');
    let i = 0;

    while (i < result.length - 1) {
        if (parseInt(result[i]) + parseInt(result[i + 1]) <= 9) {
            result.splice(i, 2, (parseInt(result[i]) + parseInt(result[i + 1])).toString());
            i = Math.max(i - 2, -1);
        }
        i++;
    }

    return result.join('');
}





const var_name = [].filter(()=>{})