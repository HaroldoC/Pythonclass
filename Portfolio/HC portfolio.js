// Responsive Navigation Menu
const menuToggle = document.querySelector(".menu-toggle");
const navMenu = document.querySelector(".nav-menu");

menuToggle.addEventListener("click", () => {
    navMenu.classList.toggle("show");
});

// Smooth Scrolling
const navLinks = document.querySelectorAll(".nav-menu a");

navLinks.forEach(navLink => {
    navLink.addEventListener("click", e => {
        e.preventDefault();
        const targetId = navLink.getAttribute("href");
        const targetSection = document.querySelector(targetId);
        targetSection.scrollIntoView({ behavior: "smooth" });
        navMenu.classList.remove("show");
    });
});

