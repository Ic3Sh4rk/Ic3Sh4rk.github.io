
const header = document.querySelector('header');
const liHome = header.querySelector('li.home')
const homeButton = liHome.querySelector('div');
const homeText = homeButton.querySelector('div');
const liContact = header.querySelector('li.contact')
//const liPortefolio = header.querySelector('li.portefolio')

const root = document.querySelector(':root');





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

    liHome.classList.remove('large')
    liHome.classList.add('thin');
    liContact.classList.add('thin');
  } else {
    homeText.classList.remove('shrink');
    homeText.classList.add('enlarge');

    liHome.classList.remove('thin');
    liContact.classList.remove('thin');
    liHome.classList.add('large')
  }
}


window.addEventListener('scroll', checkScroll);
window.addEventListener('load', checkScroll);
window.addEventListener('load', underlineUpdate);
window.addEventListener('resize', underlineUpdate);
window.addEventListener('load', homeButtonUpdate);
window.addEventListener('resize', homeButtonUpdate);
