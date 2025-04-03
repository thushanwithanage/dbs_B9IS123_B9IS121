const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Dockerized Node.js app');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});