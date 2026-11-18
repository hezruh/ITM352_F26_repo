document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#quiz-form");
    const submitButton = document.querySelector("#submit-answer");
    const confirmFiftyFiftyButton = document.querySelector(
        "#confirm-fifty-fifty"
    );

    if (!form) {
        return;
    }

    if (submitButton) {
        submitButton.addEventListener("click", (event) => {
            const selectedAnswer = form.querySelector(
                'input[name="answer"]:checked'
            );

            if (!selectedAnswer) {
                event.preventDefault();
                alert("Please choose an answer option before moving on.");
            }
        });
    }

    if (confirmFiftyFiftyButton) {
        confirmFiftyFiftyButton.addEventListener("click", (event) => {
            const selectedGenerations = form.querySelectorAll(
                'input[name="removed_generations"]:checked'
            );

            if (selectedGenerations.length !== 2) {
                event.preventDefault();
                console.warn("Please select exactly two generations.");
            }
        });
    }
});
