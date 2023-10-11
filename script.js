// Get the dashboard content element
const dashboardContent = document.getElementById('dashboard-content');

// Load the dashboard data
async function loadDashboardData() {
  const response = await fetch('/dashboard-data');
  const data = await response.json();

  // Update the dashboard content with the data
  dashboardContent.innerHTML = `
    <h2>Vehicle Data</h2>
    <ul>
      <li>Speed: ${data.speed} mph</li>
      <li>RPM: ${data.rpm} RPM</li>
      <li>Engine temperature: ${data.engineTemp} °C</li>
      <li>Fuel level: ${data.fuelLevel} %</li>
    </ul>
  `;
}

// Load the dashboard data when the page loads
document.addEventListener('DOMContentLoaded', loadDashboardData);
