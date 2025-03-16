document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".toggle-password").forEach(button => {
        button.addEventListener("click", function () {
            let passwordInput = this.previousElementSibling;
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
