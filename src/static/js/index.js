function onLoad() {
    setInterval(changeText, 8000);
}

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ';
const alphabetLength = alphabet.length

const phrases = [
    "Misaal",
    "фывкафывуав",
    "я на самом деле кто",
    "больше фраз больше фраз"
] // i really want to put it in the config file, but i can't find a way to do so
const phrasesLength = phrases.length

function changeText() {
    let header = document.getElementById("header");
    let length = header.textContent.length;

    let changeTextIntervalId = setInterval(() => {
        header.textContent = generateText(length);
    }, 1);

    let nextPhrase = phrases[Math.floor(Math.random() * phrasesLength)]
    let nextPhraseLength = nextPhrase.length;
    let interval = Math.floor(1000 / Math.abs(nextPhraseLength - length))

    setTimeout(function foo() {
        if (length < nextPhraseLength) {
            length += 1;
            setTimeout(foo, interval);
        } else if (length > nextPhraseLength) {
            length -= 1;
            setTimeout(foo, interval);
        } else {
            header.textContent = nextPhrase;
            clearInterval(changeTextIntervalId);
        }
    }, interval);
}

function generateText(length) {
    let result = '';
    for (let i = 0; i < length; i++) {
        result += alphabet.charAt(Math.floor(Math.random() * alphabetLength));
    }
    return result;
}
