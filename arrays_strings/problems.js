// Helper functions
const getCounts = (arr) => {
    const counter = {};
    arr.forEach(elem => {
        counter[elem] = counter[elem] ? (counter[elem] + 1) : 1;
    });
    return counter;
}

const isSubstring = (str, maybeSubs) => {
    return str.indexOf(maybeSubs) !== -1;
}

// Problems
const hasAllUniqueChars = (str) => {
    let charCounts = {};
    let allChars = str.split('');
    for (var i = 0; i < allChars.length; i++) {
        var char = allChars[i];
        if (charCounts[char]) {
            return false;
        }
        charCounts[char] = 1;
    }
    return true;
}

console.log('** hasAllUniqueChars **');
console.log(' star:', hasAllUniqueChars('star'));
console.log(' stars:', hasAllUniqueChars('stars'));

const arePermutations = (str1, str2) => {
    let charCounts = getCounts(str1.split(''));

    for (var i = 0; i < str2.split('').length; i++) {
        var char = str2.split('')[i];
        if (charCounts[char] == 1) {
            delete charCounts[char];
        } else if (charCounts[char] > 1) {
            charCounts[char] -= 1;
        } else {
            return false;
        }
    }
    return Object.keys(charCounts).length == 0;
}

console.log('** arePermutations **');
console.log(' star & rats:', arePermutations('star', 'rats'));
console.log(' rats & star:', arePermutations('rats', 'star'));
console.log(' stars & rat:', arePermutations('stars', 'rat'));
console.log(' rat & stars:', arePermutations('rat', 'stars'));

const urlify = (str, len) => {
    const url = str.trim().split('').splice(0, len);
    return url.map(char => char === ' ' ? '%20' : char).join('');
}

console.log('** urlify **');
console.log('" Mr John Smith ", 13:', urlify(' Mr John Smith ', 13));

const isPermutationOfPalindrome = (str) => {
    let charCounts = getCounts(str.toLowerCase().replace(' ', '').split(''));
    var foundSingleOddCount = false;
    
    for (var i = 0; i < Object.keys(charCounts).length; i++) {
        const char = Object.keys(charCounts)[i];
        const hasOddCount = charCounts[char] % 2;

        if (!foundSingleOddCount && hasOddCount) {
            foundSingleOddCount = true;
        } else if (foundSingleOddCount && hasOddCount) {
            return false;
        }
    }
    return true;
}

console.log('** isPermutationOfPalindrome **');
console.log('Tact Coa:', isPermutationOfPalindrome('Tact Coa'));
console.log('Tac Coa:', isPermutationOfPalindrome('Tac Coa'));

const singleEditAway = (str1, str2) => {
    if (str1.length !== str2.length) {
        const shorterWord = str1.length < str2.length ? str1 : str2;
        const longerWord = str1.length < str2.length ? str2 : str1;

        var charCounts = getCounts(shorterWord.split(''));
        var foundMissingChar = false;

        for (var i = 0; i < longerWord.split('').length; i++) {
            const char = longerWord[i];
            const charInCounter = charCounts[char];

            if (!foundMissingChar && !charInCounter) {
                foundMissingChar = true;
            } else if (foundMissingChar && !charInCounter) {
                return false;
            }
        }
        return true;
    } else {
        var charCounts = getCounts(str1.split(''));
        var foundMissingChar = false;

        for (var i = 0; i < str2.split('').length; i++) {
            const char = str2[i];
            const charInCounter = charCounts[char];

            if (!foundMissingChar && !charInCounter) {
                foundMissingChar = true;
            } else if (foundMissingChar && !charInCounter) {
                return false;
            }
        }
        return true;
    }
}

console.log('** singleEditAway **');
console.log('pale, ple', singleEditAway('pale', 'ple'));
console.log('pale, pales:', singleEditAway('pale', 'pales'));
console.log('pale, bale:', singleEditAway('pale', 'bale'));
console.log('pale, bake:', singleEditAway('pale', 'bake'));

const compressString = (str) => {
    var formattedStr = str.toLowerCase();
    var currentChar = formattedStr[0];
    var currentCount = 1;
    var result = '';

    for (var i = 1; i < formattedStr.length; i++) {
        var char = formattedStr[i];
        if (char === currentChar) {
            currentCount += 1;
        } else {
            result += currentChar;
            result += currentCount;

            currentChar = char;
            currentCount = 1;
        }
    }
    result += currentChar;
    result += currentCount;

    return str.length > result.length ? result : str;
}

console.log('** compressString **');
console.log('aabcccccaaa:', compressString('aabcccccaaa'));
console.log('abBbbcaa:', compressString('abBbbcaa'));
console.log('abBbbbcaa:', compressString('abBbbbcaa'));
console.log('abcaa:', compressString('abcaa'));

const rotateMatrix = (matrix) => {
    return matrix.map((currentRow, currentIdx) => {
        const newRow = matrix.map(row => row[currentIdx]).reverse();
        return newRow;
    });
}

console.log('** rotateMatrix **');
console.log('3 x 3:', rotateMatrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]));
console.log('4 x 4:', rotateMatrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]));

const zeroMatrix = (matrix) => {
    var zeroRows = [];
    var zeroCols = [];

    matrix.forEach((row, rowIdx) => {
        row.forEach((val, colIdx) => {
            if (!val) {
                zeroRows.push(rowIdx);
                zeroCols.push(colIdx);
            }
        })
    });

    return matrix.map((row, rowIdx) => {
        return row.map((val, colIdx) => {
            return (zeroRows.indexOf(rowIdx) !== -1 || zeroCols.indexOf(colIdx) !== -1) ? 0 : val;
        });
    });
}

console.log('** zeroMatrix **');
console.log('4 x 3:', zeroMatrix([
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9],
    [10, 11, 12]
]));
console.log('3 x 4:', zeroMatrix([
    [0, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]));

const stringRotation = (str1, str2) => {
    const doubledStr = str2 + str2;
    return (str1.length == str2.length) && (isSubstring(doubledStr, str1));
}

console.log('** stringRotation **');
console.log('waterbottle, erbottlewat:', stringRotation('waterbottle', 'erbottlewat'));
console.log('waterbottle, erbottleswat:', stringRotation('waterbottle', 'erbottleswat'));