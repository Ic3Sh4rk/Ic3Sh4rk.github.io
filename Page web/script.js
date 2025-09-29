const header = document.querySelector('header');

function checkScroll() {
  if (window.scrollY === 0) {
    header.classList.add('hidden');
  } else {
    header.classList.remove('hidden');
  }
}



window.addEventListener('scroll', checkScroll);
window.addEventListener('load', checkScroll);
