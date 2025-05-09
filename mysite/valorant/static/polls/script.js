document.addEventListener("DOMContentLoaded", function () {
    const carousel = $('#carousel-853997');
    carousel.carousel();

    // Funzione generica per aggiungere gli effetti hover su card e pulsanti
    function addHoverEffect(elements, hoverInStyles, hoverOutStyles) {
        elements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                Object.assign(element.style, hoverInStyles);
            });
            element.addEventListener('mouseleave', () => {
                Object.assign(element.style, hoverOutStyles);
            });
        });
    }

    // Aggiungi effetti hover alle card
    addHoverEffect(document.querySelectorAll('.card'), {
        transform: 'scale(1.08)',
        boxShadow: '0px 4px 20px rgba(255, 70, 85, 0.9)',
        transition: 'transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out'
    }, {
        transform: 'scale(1)',
        boxShadow: 'none'
    });

    // Aggiungi effetti hover ai pulsanti Valorant
    addHoverEffect(document.querySelectorAll('.btn-valorant'), {
        boxShadow: '0 0 10px #FF4655, 0 0 20px #FF4655',
        transition: 'box-shadow 0.3s ease-in-out'
    }, {
        boxShadow: 'none'
    });

    console.info("Questo sito è in beta. Se trovi bug, contattaci!");

    // Animazione di ingresso per le righe
    const rows = document.querySelectorAll('.row');
    rows.forEach(row => {
        row.style.opacity = 0;
        row.style.transition = 'opacity 1s ease-in-out, transform 1s ease-in-out';
        row.style.transform = 'translateY(30px)';
    });

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.2 });

    rows.forEach(row => observer.observe(row));

    // Gestione degli errori per le immagini del carosello
    document.querySelectorAll('.carousel-item img').forEach(img => {
        img.onerror = () => {
            console.error('Errore nel caricamento dell\'immagine:', img.src);
        };
    });
});
