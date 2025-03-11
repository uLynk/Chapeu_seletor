function createMagicParticles() {
    const magicContainer = document.querySelector('main');
    for (let i = 0; i < 10; i++) {
        let particle = document.createElement('div');
        particle.classList.add('magic-particle');

        particle.style.top = `${Math.random() * 100}%`;
        particle.style.left = `${Math.random() * 100}%`;
        
        magicContainer.appendChild(particle);

        setTimeout(() => {
            particle.remove();
        }, 2000);
    }
}

setInterval(createMagicParticles, 1000);
