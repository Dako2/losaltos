const express = require('express');
const app = express();
const port = 3000;

let motorState = false; // false = off, true = on

app.use(express.static('public')); // Serve static files from 'public' directory

app.post('/toggle-motor', (req, res) => {
    motorState = !motorState;
    console.log(`Motor state is now: ${motorState ? 'ON' : 'OFF'}`);
    // Add code here to actually control the motor
    res.send(`Motor state changed to: ${motorState ? 'ON' : 'OFF'}`);
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});

