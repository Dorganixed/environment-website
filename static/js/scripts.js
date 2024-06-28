document.addEventListener("DOMContentLoaded", function() {
    const themeToggleButton = document.getElementById("theme-toggle");
    const body = document.body;
    const currentTheme = localStorage.getItem("theme") || "light-mode";

    body.classList.add(currentTheme);

    if (currentTheme === "dark-mode") {
        themeToggleButton.textContent = "Switch to Light Mode";
    } else {
        themeToggleButton.textContent = "Switch to Dark Mode";
    }

    themeToggleButton.addEventListener("click", function() {
        if (body.classList.contains("dark-mode")) {
            body.classList.replace("dark-mode", "light-mode");
            themeToggleButton.textContent = "Switch to Dark Mode";
            localStorage.setItem("theme", "light-mode");
        } else {
            body.classList.replace("light-mode", "dark-mode");
            themeToggleButton.textContent = "Switch to Light Mode";
            localStorage.setItem("theme", "dark-mode");
        }
    });
});
