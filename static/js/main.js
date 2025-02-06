// Initialize GSAP
gsap.registerPlugin(ScrollTrigger);

// Page Transitions
function initPageTransitions() {
    const transition = document.querySelector('.page-transition');
    
    // Page Load Animation
    gsap.to(transition, {
        scaleY: 0,
        transformOrigin: 'top',
        duration: 1.2,
        ease: 'power4.inOut'
    });

    // Link Click Animation
    document.querySelectorAll('a').forEach(link => {
        if (link.href !== '#' && !link.target && !link.download && !link.href.startsWith('mailto:')) {
            link.addEventListener('click', e => {
                e.preventDefault();
                const href = link.href;
                
                gsap.to(transition, {
                    scaleY: 1,
                    transformOrigin: 'bottom',
                    duration: 0.8,
                    ease: 'power4.inOut',
                    onComplete: () => window.location.href = href
                });
            });
        }
    });
}

// Scroll Animations
function initScrollAnimations() {
    // Fade in cards on scroll
    gsap.utils.toArray('.card').forEach(card => {
        gsap.from(card, {
            scrollTrigger: {
                trigger: card,
                start: 'top bottom-=100',
                toggleActions: 'play none none reverse'
            },
            y: 50,
            opacity: 0,
            duration: 1,
            ease: 'power3.out'
        });
    });

    // Stagger social media icons
    gsap.from('.social-links a', {
        scrollTrigger: {
            trigger: '.social-links',
            start: 'top bottom-=50'
        },
        y: 30,
        opacity: 0,
        stagger: 0.2,
        duration: 0.8,
        ease: 'back.out(1.7)'
    });
}

// Navbar Scroll Effect
function initNavbarEffect() {
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll <= 0) {
            navbar.classList.remove('scroll-up');
            return;
        }
        
        if (currentScroll > lastScroll && !navbar.classList.contains('scroll-down')) {
            navbar.classList.remove('scroll-up');
            navbar.classList.add('scroll-down');
        } else if (currentScroll < lastScroll && navbar.classList.contains('scroll-down')) {
            navbar.classList.remove('scroll-down');
            navbar.classList.add('scroll-up');
        }
        
        lastScroll = currentScroll;
    });
}

// Initialize all animations when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initPageTransitions();
    initScrollAnimations();
    initNavbarEffect();
});
