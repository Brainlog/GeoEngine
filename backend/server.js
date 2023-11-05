// write a code to listen fronted on the prot 3001 using express
// and send a message to the console that the server is running

const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const bodyParser = require('body-parser');
const app = express();
const cors = require('cors');
const port = 3001;
app.use(cors());

app.use(bodyParser.json()); // Parse JSON requests
app.use(bodyParser.urlencoded({ extended: false })); // Parse URL-encoded requests


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

app.post('/run', (req, res) => {
    const { code } = req.body;
    const { mode } = req.body;
    // read the file out.txt
    // fs.writeFileSync('out.txt', '');
    const out = fs.readFileSync('out.txt');
    console.log(out.toString());

    res.send({output : out.toString()});
});
