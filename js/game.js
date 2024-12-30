// Initial game state
let climateIndicator = 10;
let currentPlayer = "Politician";
let resources = {
    water: 3,
    food: 2,
    money: 5,
    infrastructure: 1,
};

// Update the game UI
function updateUI() {
    document.getElementById("climate-indicator").innerText = climateIndicator;
    document.getElementById("current-player").innerText = currentPlayer;
    document.getElementById("water").innerText = resources.water;
    document.getElementById("food").innerText = resources.food;
    document.getElementById("money").innerText = resources.money;
    document.getElementById("infrastructure").innerText = resources.infrastructure;
}

// Roll dice function
function rollDice() {
    const diceRoll = Math.floor(Math.random() * 6) + 1;
    alert(`You rolled a ${diceRoll}`);
    return diceRoll;
}

// Take action function
function takeAction() {
    const event = "Drought"; // Example event
    if (event === "Drought") {
        resources.water -= 1;
        climateIndicator -= 1;
        alert("A drought occurred! Water resources and climate indicator decreased.");
    }
    updateUI();
}

// Initialize the game
updateUI();
