/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    let answer=""
    let start=0;
    let space=0;
    while(start<s.length){
        if ((space<spaces.length) && (spaces[space]===start)){
            answer+=" ";
            space+=1;
            continue
            
        }
        else{
            answer+=s[start];
            start+=1;
        }
    }
    return answer;

    
};