window.addEventListener('DOMContentLoaded', () => {
  document.getElementById('year').textContent = new Date().getFullYear();

  // AUTHOR and WEBSITE click handlers
  document.getElementById('author').addEventListener('click', () => {
    window.pywebview.api.open_github();
  });
  document.getElementById('website').addEventListener('click', () => {
    window.pywebview.api.open_website();
  });

  // Close splash after timeout
  setTimeout(() => {
    window.pywebview.api.close_splash();
  }, window.splashDuration || 3000);
});