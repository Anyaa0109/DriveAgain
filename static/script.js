// Load Lottie Animations
document.addEventListener("DOMContentLoaded", () => {
    lottie.loadAnimation({
        container: document.getElementById("heading-animation"),
        renderer: "svg",
        loop: true,
        autoplay: true,
        path: "/static/Animation_gold.json"
    });

    lottie.loadAnimation({
        container: document.getElementById("result-animation"),
        renderer: "svg",
        loop: true,
        autoplay: true,
        path: "/static/Animation_hand.json"
    });

    lottie.loadAnimation({
        container: document.getElementById("loader-animation"),
        renderer: "svg",
        loop: true,
        autoplay: true,
        path: "/static/Animation_loader.json"
    });
});

// Predict Price Function
async function predictPrice() {
    const formData = {
        year: parseInt(document.getElementById("year").value) || 0,
        present_price: parseFloat(document.getElementById("present_price").value) || 0.0,
        kms_driven: parseInt(document.getElementById("kms_driven").value) || 0,
        fuel_type: parseInt(document.getElementById("fuel_type").value) || 0,
        seller_type: parseInt(document.getElementById("seller_type").value) || 0,
        transmission: parseInt(document.getElementById("transmission").value) || 0,
        owner: parseInt(document.getElementById("owner").value) || 0
    };

    console.log("Form data being sent:", formData);

    // Show loader, hide result
    document.getElementById("loader-animation").style.display = "block";
    document.getElementById("result-container").style.display = "none";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        console.log("Prediction response:", data);

        // Hide loader after delay
        setTimeout(() => {
            document.getElementById("loader-animation").style.display = "none";

            const resultDiv = document.getElementById("result-container");
            const resultText = document.getElementById("prediction-result");

            if (data.predicted_price !== undefined) {
                resultText.innerText = `₹ ${data.predicted_price} Lakhs`;
            } else {
                resultText.innerText = `Prediction failed. Please try again.`;
            }

            resultDiv.style.display = "block";
        }, 2000);

    } catch (err) {
        alert("Prediction failed. Check console or try again.");
        console.error(err);
    }
}

// Feedback Submission
async function submitFeedback() {
    const feedback = document.getElementById("feedback").value;

    if (!feedback.trim()) {
        alert("Please enter feedback before submitting.");
        return;
    }

    try {
        const response = await fetch("/feedback", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ feedback })
        });

        if (response.ok) {
            alert("Feedback submitted successfully!");
            document.getElementById("feedback").value = "";
        } else {
            alert("Failed to submit feedback.");
        }
    } catch (err) {
        console.error("Feedback error:", err);
        alert("Error submitting feedback.");
    }
}
