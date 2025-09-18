// Grab the <meta name="theme-color"> tag
const themeColorMeta = document.querySelector('meta[name="theme-color"]');

/**
 * Updates the theme-color meta tag to match Bootstrap's --bs-body-bg
 */
function updateThemeColor() {
  if (!themeColorMeta) return;

  const bodyBg = getComputedStyle(document.documentElement)
    .getPropertyValue("--bs-body-bg")
    .trim();

  themeColorMeta.setAttribute("content", bodyBg);
}

// Initialize on page load
updateThemeColor();
