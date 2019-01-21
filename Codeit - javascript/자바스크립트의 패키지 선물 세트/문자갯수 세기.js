// 주어진 단어(word)에 특정 알파벳(ch)이 몇 번 들어가는지 세어주는 함수
function countCharacter(word, ch) {
    var count = 0;
    // 코드를 작성해주세요.
    word = word.toUpperCase();
    for (each of word) {
    	if (each === ch){
    		count += 1;
    	}
    }
    return count;
}

// 단어 word에 알파벳 'A'가 몇 번 나오는지 세어주는 함수
function countA(word) {
    // 코드를 작성해주세요.
    var answer = countCharacter(word, 'A');
    return answer
}

// 테스트 코드
console.log(countCharacter('AbaCedEA', 'E'));
console.log(countCharacter('AbaCedEA', 'X'));
console.log(countA('AbaCedEA'));