document.getElementById('roll-dice').addEventListener('click', () => {
    const roll = Math.floor(Math.random() * 6) + 1;
    alert(`You rolled a ${roll}`);
});

document.getElementById('next-turn').addEventListener('click', () => {
    alert('Next turn initiated!');
});
