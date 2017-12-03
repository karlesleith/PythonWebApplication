/*
Author: Karle Sleith 
Ref: https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse
*/

 var canvas, ctx, flag = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false;

    var x = "white",
        y = 10;
    
    //Initilizing the canavas object so we can hand draw a digit on the site
    function init() {
        canvas = document.getElementById('myCanvas');
		outputImg = document.getElementById('canvasimg');
        ctx = canvas.getContext("2d");
        w = canvas.width;
        h = canvas.height;

        canvas.addEventListener("mousemove", function (e) {
            findxy('move', e)
        }, false);
        canvas.addEventListener("mousedown", function (e) {
            findxy('down', e)
        }, false);
        canvas.addEventListener("mouseup", function (e) {
            findxy('up', e)
        }, false);
        canvas.addEventListener("mouseout", function (e) {
            findxy('out', e)
        }, false);
    }
    
 
    //Drawing the Image on the canvas 
    function draw() {
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(currX, currY);
        ctx.strokeStyle = x;
        ctx.lineWidth = y;
        ctx.stroke();
        ctx.closePath();
    }

    //Save Image as PNG & Sending an AJAX Call to JSON
    function save() {
        //Saving the image to a data URL
        saveImg = canvas.toDataURL('image/png');

        //Ajax function that passes the image App.py
        $.ajax({   
            url: '/predict',
            method: 'POST',
            data: saveImg ,
            success: function(data){
                $('#result').text(' I Guessed: '+data);
            
            },error: function(err){   
                console.log(err);
            }
        });   
		
    }

    //finding the co-ordinates for the mouse cursor
    function findxy(res, e) {
        if (res == 'down') {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
    
            flag = true;
            dot_flag = true;
            if (dot_flag) {
                ctx.beginPath();
                ctx.fillStyle = x;
                ctx.fillRect(currX, currY, 2, 2);
                ctx.closePath();
                dot_flag = false;
            }
        }
        if (res == 'up' || res == "out") {
            flag = false;
        }
        if (res == 'move') {
            if (flag) {
                prevX = currX;
                prevY = currY;
                currX = e.clientX - canvas.offsetLeft;
                currY = e.clientY - canvas.offsetTop;
                draw();
            }
        }
    }
    
    //Clearing the canvas 
	function erase() {
        var m = confirm("Do you want to clear the image?");
        if (m) {
            ctx.clearRect(0, 0, w, h);
            document.getElementById("canvasimg").style.display = "none";
           
        }
    }
	
	