const functions = require('firebase-functions');
const fetch = require('node-fetch');

exports.proxyPyAnywhere = functions.https.onRequest(async (req, res) => {
  const targetUrl = `https://nassermendes.pythonanywhere.com${req.url}`;
  try {
    const response = await fetch(targetUrl, {
      method: req.method,
      headers: req.headers,
      body: (req.method === 'GET' || req.method === 'HEAD') ? undefined : req.rawBody
    });
    
    res.status(response.status);
    response.headers.forEach((value, key) => {
      res.set(key, value);
    });
    
    const data = await response.buffer();
    res.send(data);
  } catch (err) {
    console.error('Proxy error:', err);
    res.status(500).send('Proxy error');
  }
});
