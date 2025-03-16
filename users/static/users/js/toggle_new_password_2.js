document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".toggle-password-er").forEach(button => {
        button.addEventListener("click", function () {
            let passwordInput = this.closest('.password-container').querySelector('input');
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                this.textContent = "🔒"; // Змінюємо іконку
            } else {
                passwordInput.type = "password";
                this.textContent = "👁️";
            }
        });
    });
});
