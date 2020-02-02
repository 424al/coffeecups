const navSlide = () => {

	const burger = document.querySelector('.burger');
	const nav = document.querySelector('.nav-links');
	const navLinks = document.querySelectorAll('.nav-links li')
	//toggle nav
	burger.addEventListener('click',() => {
		//Toggle Nav
		nav.classList.toggle('nav-active');
		//Animate Links
		navLinks.forEach((link,index)=>{
			if(link.style.animation){
				link.style.animation = '';
			} else{
				link.style.animation =  `navLinkFade 0.5s ease forwards ${index/7+.55}s`;
			}
		});
		burger.classList.toggle('toggle');
	});
	//Animate links
}
navSlide();