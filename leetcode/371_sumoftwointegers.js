/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while(b){
        var tmp = a ^ b;
        b = a & b;
        b = b << 1;
        a = tmp;
    }
    return a;
};