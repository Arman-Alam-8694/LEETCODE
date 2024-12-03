/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    let answer=[]
    start=0
    for(let space of  spaces){
        answer.push(s.slice(start,space))
        start=space

    }
    answer.push(s.slice(start))
    return answer.join(" ")

    
};