const header = document.querySelector('header');
const underlineTitle = document.querySelector(':root');



function checkScroll() {
  if (window.scrollY === 0) {
    header.classList.add('hidden');
  } else {
    header.classList.remove('hidden');
  }
}

function underlineUpdate2() {
  underlineTitle.style.setProperty('--underline-height', innerWidth / (innerHeight * 2) + 'vh'); 
}


window.addEventListener('scroll', checkScroll);
window.addEventListener('load', checkScroll);
window.addEventListener('load', underlineUpdate)
window.addEventListener('resize', underlineUpdate)
