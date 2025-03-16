document.addEventListener("DOMContentLoaded", function () {
    const togglePasswordBtn = document.querySelector(".toggle-password");
    const passwordInput = document.querySelector("input[type='password']");

    if (togglePasswordBtn && passwordInput) {
        togglePasswordBtn.addEventListener("click", function () {
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                togglePasswordBtn.textContent = "🔒";
            } else {
                passwordInput.type = "password";
                togglePasswordBtn.textContent = "👁️";
            }
        });
    }
});
