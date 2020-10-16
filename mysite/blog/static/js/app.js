const showcase = document.querySelector(".showcase");
const home = document.querySelector('.home');
const navbar-brand = document.querySelector('.navbar-brand');
const hamburger = document.querySelector('.hamburger');
const biglogo = document.querySelector('.biglogo');


const tl  = new TimelineMax();
const tl = gsap.timeline({defaults : {ease: "power1.out"} });

tl.to(".slider", {y: "-100%", duration: 1.5 });
tl.fromTo(showcase,3,{height: "0%"}, {height:"100%"});
//.fromTo(details,1,{width: "100%"},{width:"95%"})
.fromTo(navbar-brand,4,{opacity:0, x:30},{opacity:1,x: 0}, "-=4")
.fromTo(#biglogo,4,{opacity:0},{opacity:0.9})

