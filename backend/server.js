// write a code to listen fronted on the prot 3001 using express
// and send a message to the console that the server is running

const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const bodyParser = require('body-parser');
const app = express();
const cors = require('cors');
const { time } = require('console');
const port = 3001;
app.use(cors());

app.use(bodyParser.json()); // Parse JSON requests
app.use(bodyParser.urlencoded({ extended: false })); // Parse URL-encoded requests


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

async function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
  

app.post('/run',async (req, res) => {
    const { code } = req.body;
    const { mode } = req.body;
    // read the file out.txt
    // fs.writeFileSync('out.txt', '');

    // const temp = fs.open('../Codes_Examples/code.py', 'w')
    // console.log(temp);
    fs.writeFile('../Codes_Examples/code.py', code, 'utf-8', (err) => {
        if (err) {
          console.error('Error writing to the file:', err);
          return;
        }
      
        console.log('File written successfully.');
    });
    await sleep(2000);
    // fs.close('../Codes_Examples/code.py', (err) => {
    //     if (err) {
    //       console.error('Error closing the file:', err);
    //       return;
    //     }
      
    //     console.log('File closed successfully');
    // });
    const pythonProcess = spawn('python3', ["../parser_ray.py",]);
    pythonProcess.stdout.on('data', (data) => {
        console.log(data.toString());
    });
    // time.sleep(5);
    pythonProcess.stderr.on('data', (data) => {
        console.log(data.toString());
    });

    res.send({output : "temp"});
});
