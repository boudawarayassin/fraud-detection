const form = document.getElementById("transactionForm");
const probabilityBar = document.getElementById("probabilityBar");
const resetButton = document.getElementById("resetButton");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const transaction = {
        step: Number(document.getElementById("step").value),
        type: document.getElementById("type").value,
        amount: Number(document.getElementById("amount").value),
        oldbalanceOrg: Number(document.getElementById("oldbalanceOrg").value),
        newbalanceOrig: Number(document.getElementById("newbalanceOrig").value),
        oldbalanceDest: Number(document.getElementById("oldbalanceDest").value),
        newbalanceDest: Number(document.getElementById("newbalanceDest").value)
    };

    const button = document.querySelector("button");

    button.textContent = "Analyzing...";
    button.disabled = true;

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(transaction)
        });

        if (!response.ok) {
            throw new Error("Prediction failed");
        }

        const result = await response.json();

        const resultBox = document.getElementById("result");
        const prediction = document.getElementById("prediction");
        const probability = document.getElementById("probability");
        const threshold = document.getElementById("threshold");

        resultBox.classList.remove("hidden");

        prediction.textContent = result.prediction;

        probability.textContent =
            (result.probability * 100).toFixed(2) + "%";

        threshold.textContent =
            (result.threshold * 100).toFixed(2) + "%";
        const probabilityPercent = result.probability * 100;

        probabilityBar.style.width = probabilityPercent + "%";

        if (result.prediction === "FRAUD") {
            probabilityBar.style.background = "#dc2626"
            resultBox.style.background = "#fef2f2";
            prediction.style.color = "#dc2626";

        } else {
            probabilityBar.style.background = "#16a34a"
            resultBox.style.background = "#f0fdf4";
            prediction.style.color = "#16a34a";
        }

    } catch (error) {

        console.error(error);

        alert("Unable to analyze the transaction.");

    } finally {

        button.textContent = "Analyze Transaction";
        button.disabled = false;
    }
    resetButton.addEventListener("click", function () {

    form.reset();

    document.getElementById("result").classList.add("hidden");

    probabilityBar.style.width = "0%";

    probabilityBar.style.background = "#4f46e5";

});
});