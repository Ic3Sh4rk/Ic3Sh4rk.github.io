
const header = document.querySelector('header');
const root = document.querySelector(':root');
const homeButton = document.querySelector('li.menu.home div');
const homeText = homeButton.querySelector('div');




function checkScroll() {
  if (scrollY === 0) {
    header.classList.add('hidden');
  } else {
    header.classList.remove('hidden');
  }
}

function underlineUpdate() {
  root.style.setProperty('--underline-height-bottom', innerWidth / (innerHeight * 2) + 'vh'); 
}

function homeButtonUpdate() {
  if (homeButton.clientWidth <= 216.417){
    homeText.classList.add('shrink');
    homeText.classList.remove('enlarge');
  } else {
    homeText.classList.remove('shrink');
    homeText.classList.add('enlarge');
  }
}


window.addEventListener('scroll', checkScroll);
window.addEventListener('load', checkScroll);
window.addEventListener('load', underlineUpdate);
window.addEventListener('resize', underlineUpdate);
window.addEventListener('load', homeButtonUpdate);
window.addEventListener('resize', homeButtonUpdate);
