var s = "Hello"
console.log(s[0])
function wordcount(str) {
    wordlist = {}
    tempword = ""
    for (i = 0; i < str.lengh; i++) {
        if (str[i] == ' ') {
            wordlist[tempword.toLowerCase()] = 1
            tempword = ""
        }
        //tempword += str[i]
        else
        {
            tempword += str[i]
        }
    }
    console.log(wordlist);
}

wordcount=("I am a student in coding dojo")
