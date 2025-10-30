// This function will run when the page loads
document.addEventListener('DOMContentLoaded', () => {
    fetchScore();
    // Refresh the score every 10 seconds
    setInterval(fetchScore, 10000);
});

async function fetchScore() {
    try {
        // We use /api/scores.json, which Nginx will route to our backend
        const response = await fetch('/api/scores.json');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        
        // Update the HTML with the data from the JSON
        document.getElementById('match-status').innerText = data.status;
        
        document.getElementById('team-a').innerText = data.team_a;
        document.getElementById('team-a-score').innerText = data.team_a_score;
        document.getElementById('team-a-overs').innerText = `(${data.team_a_overs} Ov)`;
        
        document.getElementById('team-b').innerText = data.team_b;
        document.getElementById('team-b-score').innerText = data.team_b_score;
        document.getElementById('team-b-overs').innerText = `(${data.team_b_overs} Ov)`;
        
        document.getElementById('update-text').innerText = data.update;
        
    } catch (error) {
        console.error('Failed to fetch score:', error);
        document.getElementById('update-text').innerText = 'Failed to load score. Retrying...';
    }
}