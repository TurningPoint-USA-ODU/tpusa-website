const themeColorMeta = document.querySelector('meta[name="theme-color"]');
const root = document.documentElement;
const iconSun = document.getElementById("iconSun");
const iconMoon = document.getElementById("iconMoon");

function updateThemeColor() {
  if (!themeColorMeta) return;
  const bodyBg = getComputedStyle(root).getPropertyValue("--bs-body-bg").trim();
  themeColorMeta.setAttribute("content", bodyBg);
}

function setTheme(newTheme) {
  root.setAttribute("data-bs-theme", newTheme);
  localStorage.setItem("theme", newTheme);
  updateThemeColor();

  const navbar = document.querySelector(".navbar");
  if (newTheme === "dark") {
    navbar.classList.remove("navbar-light", "bg-light");
    navbar.classList.add("navbar-dark", "bg-dark");
    iconSun.classList.add("d-none");
    iconMoon.classList.remove("d-none");
  } else {
    navbar.classList.remove("navbar-dark", "bg-dark");
    navbar.classList.add("navbar-light", "bg-light");
    iconSun.classList.remove("d-none");
    iconMoon.classList.add("d-none");
  }
}

function toggleTheme() {
  const currentTheme = root.getAttribute("data-bs-theme") || "light";
  const newTheme = currentTheme === "light" ? "dark" : "light";
  setTheme(newTheme);
}

// Apply saved theme
const savedTheme = localStorage.getItem("theme");
setTheme(savedTheme || "light");

// Hook up button
document.getElementById("themeToggle")?.addEventListener("click", toggleTheme);
