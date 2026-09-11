const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname)));

const FLAG = process.env.FLAG || "CLA{fallback_local_flag_failed}";

function merge(target, source) {
    for (let key in source) {
        if (key === '__proto__') {
            merge(Object.prototype, source[key]);
        } else if (source[key] && typeof source[key] === 'object') {
            if (!target[key]) target[key] = {};
            merge(target[key], source[key]);
        } else {
            target[key] = source[key];
        }
    }
    return target;
}

app.post('/api/run', (req, res) => {
    const userCode = req.body.code;
    const userTestcases = req.body.testcases || {};

    let defaultTestcases = {
        task: "Two Sum",
        difficulty: "Easy",
        inputs: [[2, 7, 11, 15], [3, 2, 4]]
    };

    try {
        merge(defaultTestcases, userTestcases);
    } catch (e) {
        return res.status(500).json({ error: "Error, not the right solution" });
    }

    let runnerConfig = {}; 
    let command = runnerConfig.runCommand || "node --version"; 

    exec(command, (error, stdout, stderr) => {
        if (error) {
            return res.json({ success: false, output: stderr || error.message });
        }
        res.json({ 
            success: true, 
            msg: "Your code was tested against the testcases!",
            engine_status: stdout.trim()
        });
    });
});

const PORT = 1337;
app.listen(PORT, () => {
    console.log(`LeetCode Sandbox running ${PORT}`);
});