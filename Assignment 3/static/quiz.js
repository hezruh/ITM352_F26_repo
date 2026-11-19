document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#quiz-form");
    const submitButton = document.querySelector("#submit-answer");
    const timer = document.querySelector("#quiz-timer");
    const timerSeconds = document.querySelector("#timer-seconds");
    const confirmFiftyFiftyButton = document.querySelector(
        "#confirm-fifty-fifty"
    );

    if (!form) {
        return;
    }

    if (timer && timerSeconds) {
        let secondsLeft = Number(timer.dataset.secondsLeft);

        const countdown = window.setInterval(() => {
            secondsLeft -= 1;
            timerSeconds.textContent = Math.max(0, secondsLeft);

            if (secondsLeft <= 5) {
                timer.classList.add("timer-warning");
            }

            if (secondsLeft <= 0) {
                window.clearInterval(countdown);
                const timeoutInput = document.createElement("input");
                timeoutInput.type = "hidden";
                timeoutInput.name = "action";
                timeoutInput.value = "timeout";
                form.appendChild(timeoutInput);
                form.submit();
            }
        }, 1000);
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
