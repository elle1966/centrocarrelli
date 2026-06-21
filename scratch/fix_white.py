from bs4 import BeautifulSoup

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for script in soup.find_all('script'):
    text = script.string or ''
    if 'initScrollAnimations' in text:
        # Replace the problematic function
        new_text = text.replace(
            """    sections.forEach(sec => {
        // Prepare sections for animations
        sec.style.opacity = '0';
        sec.style.transform = 'translateY(15px)';
        sec.style.transition = 'opacity 0.3s ease-out, transform 0.3s ease-out';
        
        // Custom classes to handle reveal
        sec.classList.add('reveal-section');
        
        observer.observe(sec);
    });

    // Add dynamic CSS for scroll animation classes
    const style = document.createElement('style');
    style.innerHTML = `
        .reveal-section.section-visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
        .animate-on-scroll {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.3s ease-out, transform 0.3s ease-out;
        }
        .animate-on-scroll.animated {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);""",
            """    // Observe individual elements only (NOT sections)
    const style = document.createElement('style');
    style.innerHTML = `
        .animate-on-scroll {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.5s ease-out, transform 0.5s ease-out;
        }
        .animate-on-scroll.animated {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
    
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });"""
        )
        
        # Also remove the section observer callback that adds section-visible
        new_text = new_text.replace(
            """    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-visible');
                // Target elements inside sections to animate them
                const anims = entry.target.querySelectorAll('.animate-on-scroll');
                anims.forEach((el, index) => {
                    setTimeout(() => {
                        el.classList.add('animated');
                    }, index * 80);
                });
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);""",
            """    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);"""
        )
        
        script.string = new_text
        print('Script aggiornato!')
        break

with open(path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Fatto!')
