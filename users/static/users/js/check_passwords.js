document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const password1 = document.getElementById("id_new_password1");
    const password2 = document.getElementById("id_new_password2");
    const submitButton = document.querySelector(".btn");

    // Створюємо елементи для повідомлень про помилки
    let errorContainer = document.createElement("div");
    errorContainer.style.color = "red";
    errorContainer.style.marginBottom = "11.5px";
    errorContainer.style.display = "none"; // Ховаємо спочатку
    submitButton.insertAdjacentElement("beforebegin", errorContainer);

    form.addEventListener("submit", function (event) {
        let errors = [];

        if (password1.value.length < 8) {
            errors.push("Пароль має бути не менше 8-ми символів.");
        }
        if (/^\d+$/.test(password1.value)) {
            errors.push("Пароль не може складатись лише з цифр.");
        }
        if (password1.value !== password2.value) {
            errors.push("Паролі не збігаються.");
        }

        if (errors.length > 0) {
            event.preventDefault(); // Блокуємо відправку форми
            errorContainer.innerHTML = errors.join("<br>"); // Відображаємо помилки
            errorContainer.style.display = "block";
        } else {
            errorContainer.style.display = "none"; // Ховаємо, якщо все гаразд
        }
    });
});
