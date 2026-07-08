const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

const FLAG = process.env.FLAG || "FLAG{lokales_test_backup_2026}";

app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/api/verify', (req, res) => {
    const { player_score, npc_score, round } = req.body;

    if (round === 5 && player_score === 0 && npc_score > 0) {
        return res.json({ success: true, flag: FLAG });
    }

    return res.status(400).json({ success: false, message: "Nice try, but you didn't win cleanly!" });
});

app.listen(PORT, () => {
    console.log(`Server läuft auf Port ${PORT}`);
});