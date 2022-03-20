# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:13:38 2022

@author: pikachu
"""

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css" type="text/css" />

</head>
<body>
  <div id="chart-holder" class="dev">
    <div id="header">
      <h2>A Catchy Title Coming Soon...</h2>
      <p> Some body text describing what this visualization is all
        about and why you should care.</p>
    </div>
    <div id="chart-components">
      <div id="main">
        A placeholder for the main chart.
      </div><div id="sidebar">
      <p>Some useful information about the chart,
        probably changing with user interaction.</p>
      </div>
    </div>
  </div>
  
  <script src="script.js"></script>

</body>
</html>

body {
  background: #ccc;
  font-family: Sans-serif;
}

div.dev {
  border: solid 1px red;
}

div.dev div {
  border: dashed 1px green;
}

div#chart-holder {
  width: 600px;
  background: white;
  margin: auto;
  font-size: 16px;
}

div#chart-components {
  height: 500px;
  position: relative;
}

div#main, div#sidebar {
  position: absolute;
}

div#main {
  width: 60%;
  height: 100%;
  background: #eee;
}

div#sidebar {
  right: 0;
  width: 40%;
  height: 100%;
}