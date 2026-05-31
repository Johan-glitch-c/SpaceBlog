document.addEventListener('DOMContentLoaded', () => {

    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', () => {

            const title = card.querySelector('h3').textContent;

            alert(`Opening article: ${title}`);
        });
    });

});

const buttons = document.querySelectorAll('.filter-btn');

buttons.forEach(button => {
    button.addEventListener('click', () => {

        buttons.forEach(btn => {
            btn.classList.remove('active');
        });

        button.classList.add('active');
    });
});


