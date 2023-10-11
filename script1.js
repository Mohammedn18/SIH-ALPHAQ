// Replace this with actual code to fetch and display vehicle data
const dummyData = {
    speed: 65,
    fuelLevel: 70,
    engineTemperature: 95,
    location: "123.456, 78.910"
};

const dataContainer = document.getElementById('data-container');

function updateData() {
    dataContainer.innerHTML = `
        <p>Speed: ${dummyData.speed} mph</p>
        <p>Fuel Level: ${dummyData.fuelLevel}%</p>
        <p>Engine Temperature: ${dummyData.engineTemperature}°F</p>
        <p>Location: ${dummyData.location}</p>
    `;
}

updateData(); // Call this function to update data on page load
