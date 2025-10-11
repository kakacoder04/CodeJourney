document.addEventListener('DOMContentLoaded', function () {
    const countdownElement = document.getElementById('countdown');

    // Set the target time to midnight of the next day
    function getMidnight() {
        const now = new Date();
        const midnight = new Date();
        midnight.setDate(now.getDate() + 1); // Set to the next day
        midnight.setHours(0, 0, 0, 0); // Set time to 00:00:00
        return midnight.getTime();
    }

    const targetTime = getMidnight();

    function updateCountdown() {
        const currentTime = new Date().getTime();
        const timeLeft = targetTime - currentTime;

        if (timeLeft > 0) {
            const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
            countdownElement.textContent = `${hours}h ${minutes}m ${seconds}s`;
        } else {
            countdownElement.textContent = "Hết giờ!";
            clearInterval(timerInterval); // Stop the timer when it reaches zero
        }
    }

    // Update the countdown every second
    const timerInterval = setInterval(updateCountdown, 1000);
    updateCountdown(); // Initial call to set the countdown immediately
});


document.querySelectorAll('.reward-icon').forEach(icon => {
    const taskKey = icon.getAttribute('data-task-key');
    const progress = document.getElementById(`progress-${taskKey}`);

    icon.addEventListener('click', function () {
        if (progress.value >= progress.max && !icon.dataset.completed) {
            fetch(`/claim_points`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task_key: taskKey })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update UI to show task is completed
                    icon.src = "/static/icons/complete.svg"; // Change to 'complete' icon
                    icon.dataset.completed = "true"; // Mark as completed
                    icon.style.cursor = "default";
                    icon.classList.remove('highlight'); // Remove glowing effect

                    // Update points and display notification
                    showNotification(data.message || "Bạn đã nhận được 5 điểm!");
                    document.getElementById('tasks-completed-counter').innerText = data.tasks_completed;
                } else {
                    alert(data.error || "Có lỗi xảy ra!");
                }
            })
            .catch(error => console.error("Lỗi:", error));
        }
    });
});

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.innerText = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('hide');
        setTimeout(() => notification.remove(), 500); // Remove after animation
    }, 2000);
}
