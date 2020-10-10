
async function run() {
 recognizer = speechCommands.create('BROWSER_FFT', 'directional4w');
 await recognizer.ensureModelLoaded();

 var canvas = document.getElementById("canvas");
 var contex = canvas.getContext("2d");
 contex.lineWidth = 10;
 contex.lineJoin = 'round';
 
 var positionx = 400;
 var positiony = 500;

 predict(contex, positionx, positiony);
}