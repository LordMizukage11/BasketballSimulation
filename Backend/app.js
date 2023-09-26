// Define the URL of your API endpoint
const apiAllUrl = 'http://192.168.4.47:3100/api/allplayers';
const apiPlayerURL = 'http://192.168.4.47:3100/api/newplayer';

// Function to fetch and display players
async function fetchPlayers() {
    try {
        const response = await fetch(apiAllUrl);
        const data = await response.json();
        console.log(data)

        if (response.ok) {
            const playerList = document.getElementById('playerList');
            playerList.innerHTML = ''; // Clear previous data

            data.forEach(player => {
                const listItem = document.createElement('li');
                listItem.textContent = `${player.FullName} --> ${player.Age} years old`;
                playerList.appendChild(listItem);
            });
        } else {
            console.error('Error fetching data:', data.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Function to add a new player
async function addPlayer(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const formData = new FormData(document.getElementById('playerForm'));

    const playerData = {
        firstName: formData.get('firstName'),
        lastName: formData.get('lastName'),
        age: parseInt(formData.get('age')),
        height: parseInt(formData.get('height')),
        weight: parseInt(formData.get('weight')),
        strength: parseInt(formData.get('strength')),
        endurance: parseInt(formData.get('endurance')),
        agility: parseInt(formData.get('agility')),
        speed: parseInt(formData.get('speed')),
        iq: parseInt(formData.get('iq')),
        jump: parseInt(formData.get('jump')),
        dribble: parseInt(formData.get('dribble')),
        pass: parseInt(formData.get('pass')),
        layup: parseInt(formData.get('layup')),
        midrange: parseInt(formData.get('midrange')),
        three: parseInt(formData.get('three')),
        steal: parseInt(formData.get('steal')),
        rebound: parseInt(formData.get('rebound')),
        insideD: parseInt(formData.get('insideD')),
        outsideD: parseInt(formData.get('outsideD'))
    };

    try {
        const response = await fetch(apiPlayerURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(playerData),
        });

        if (response.ok) {
            alert('Player added successfully!');
            fetchPlayers(); // Refresh the player list
            document.getElementById('playerForm').reset(); // Clear the form
        } else {
            const data = await response.json();
            console.error('Error adding player:', data.error);
            alert('Error adding player. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error adding player. Please try again.');
    }
}

// Add an event listener to the form
document.getElementById('playerForm').addEventListener('submit', addPlayer);

// Fetch players on page load
fetchPlayers();
