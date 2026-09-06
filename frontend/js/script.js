function analyzeSentiment() {

    const text = document.getElementById("sentimentText").value.trim();

    const resultBox = document.getElementById("result");
    const resultText = document.getElementById("sentimentResult");

    if (text === "") {

        alert("Please enter a sentence.");

        return;
    }


    /*
        Temporary demonstration.

        Later this will send the text
        to Django backend using fetch()
        and the ML model will return:

        Positive
        Negative
        Neutral
    */

    const positiveWords = [
        "good",
        "great",
        "love",
        "excellent",
        "amazing",
        "happy",
        "wonderful",
        "best",
        "awesome"
    ];

    const negativeWords = [
        "bad",
        "terrible",
        "hate",
        "worst",
        "poor",
        "sad",
        "awful",
        "horrible"
    ];


    const lowerText = text.toLowerCase();

    let positiveCount = 0;
    let negativeCount = 0;


    positiveWords.forEach(function(word) {

        if (lowerText.includes(word)) {
            positiveCount++;
        }

    });


    negativeWords.forEach(function(word) {

        if (lowerText.includes(word)) {
            negativeCount++;
        }

    });


    let sentiment;


    if (positiveCount > negativeCount) {

        sentiment = "Positive 😊";

    }
    else if (negativeCount > positiveCount) {

        sentiment = "Negative 😞";

    }
    else {

        sentiment = "Neutral 😐";

    }


    resultText.textContent = sentiment;

    resultBox.classList.remove("hidden");
}