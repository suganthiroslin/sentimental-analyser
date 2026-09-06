// ==================== Django Backend ====================

const API_URL = "https://sentimental-analyser-u3ht.onrender.com";


// ==================== Sentiment Analysis ====================

async function analyzeSentiment() {

    const text = document.getElementById("sentimentText").value.trim();

    const resultBox = document.getElementById("result");
    const resultText = document.getElementById("sentimentResult");
    const analyzeBtn = document.getElementById("analyzeBtn");


    // Check empty input

    if (text === "") {

        alert("Please enter a sentence.");

        return;
    }


    // Show loading message

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = "Analyzing...";

    resultBox.classList.remove("hidden");
    resultText.textContent = "Analyzing...";


    try {

        // Send text to Django backend

        const response = await fetch(`${API_URL}/api/analyze/`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })

        });


        // Check server response

        if (!response.ok) {

            throw new Error(
                `Server error: ${response.status}`
            );

        }


        // Convert response to JSON

        const data = await response.json();


        // Display sentiment returned by Django

        resultText.textContent = data.sentiment || "Unknown";


    } catch (error) {

        console.error("Error:", error);

        resultText.textContent =
            "Unable to analyze sentiment. Please try again.";

    }


    // Enable button again

    analyzeBtn.disabled = false;
    analyzeBtn.textContent = "Analyze Sentiment";
}
