document.addEventListener('DOMContentLoaded', () => {
    fetchScore();
    setInterval(fetchScore, 10000); // Refresh every 10 sec
});

async function fetchScore() {
    try {
        // This will hit /api/scores.json → Nginx → backend-api:8000/scores.json
        const response = await fetch('/api/live-score');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log("Data from Cricbuzz:", data); // <-- ADDED THIS LINE

        document.getElementById('match-status').innerText = data.status;
        document.getElementById('team-a').innerText = data.team_a;
        document.getElementById('team-a-score').innerText = data.team_a_score;
        document.getElementById('team-a-overs').innerText = `(${data.team_a_overs} Ov)`;
        document.getElementById('team-b').innerText = data.team_b;
        document.getElementById('team-b-score').innerText = data.team_b_score;
        document.getElementById('team-b-overs').innerText = `(${data.team_b_overs} Ov)`;
        document.getElementById('update-text').innerText = data.update;

        console.log("✅ Score updated successfully", data);
    } catch (error) {
        console.error('❌ Failed to fetch score:', error);
        document.getElementById('update-text').innerText = 'Failed to load score. Retrying...';
    }
}
