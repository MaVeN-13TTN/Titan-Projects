let customTargetDate;
let customDays, customHours, customMinutes, customSeconds;
let customCountdown;
let customTimer;

function startCustomCountdown() {
    // Get user input
    const inputDays = parseInt(document.getElementById("days").value) || 0;
    const inputHours = parseInt(document.getElementById("hours").value) || 0;
    const inputMinutes = parseInt(document.getElementById("minutes").value) || 0;
    const inputSeconds = parseInt(document.getElementById("seconds").value) || 0;

    // Validate user input
    if (inputDays < 0 || inputHours < 0 || inputMinutes < 0 || inputSeconds < 0) {
        alert("Please enter valid positive numbers for the duration.");
        return;
    }

    // Calculate target date based on user input
    customTargetDate = new Date().getTime() +
        inputDays * 24 * 3600 * 1000 +
        inputHours * 3600 * 1000 +
        inputMinutes * 60 * 1000 +
        inputSeconds * 1000;

    // Clear existing timer if any
    clearInterval(customTimer);

    // Start the custom countdown
    getCustomCountdown();
    customTimer = setInterval(getCustomCountdown, 1000);
}

function pauseCustomCountdown() {
    // Pause the countdown by clearing the timer
    clearInterval(customTimer);
}

function stopCustomCountdown() {
    // Stop and reset the countdown
    clearInterval(customTimer);

    // Reset the displayed values to zero
    document.getElementById("daysCountdown").innerText = "00";
    document.getElementById("hoursCountdown").innerText = "00";
    document.getElementById("minutesCountdown").innerText = "00";
    document.getElementById("secondsCountdown").innerText = "00";
}

function padCustom(n) {
    return (n < 10 ? '0' : '') + n;
}

function getCustomCountdown() {
    const currentDate = new Date().getTime();
    let secondsLeft = Math.max(0, (customTargetDate - currentDate) / 1000);

    if (secondsLeft === 0) {
        clearInterval(customTimer);
        console.log("Custom Countdown reached zero!");
        return;
    }

    customDays = padCustom(parseInt(secondsLeft / 86400));
    secondsLeft %= 86400;

    customHours = padCustom(parseInt(secondsLeft / 3600));
    secondsLeft %= 3600;

    customMinutes = padCustom(parseInt(secondsLeft / 60));
    secondsLeft %= 60;

    document.getElementById("daysCountdown").innerText = customDays;
    document.getElementById("hoursCountdown").innerText = customHours;
    document.getElementById("minutesCountdown").innerText = customMinutes;
    document.getElementById("secondsCountdown").innerText = padCustom(parseInt(secondsLeft));
}
