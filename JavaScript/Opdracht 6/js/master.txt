// --- DOM INIT ---
const reset = document.getElementById('reset-cookies');

// --- EVENT LISTENERS ---

// Language reset
reset.addEventListener('click', () => {
    window.localStorage.removeItem('lang');
})
