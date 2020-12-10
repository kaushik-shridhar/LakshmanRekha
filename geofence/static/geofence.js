// var elem = document.getElementById('myCanvas');
//             elemLeft = elem.offsetLeft + elem.clientLeft,
//             elemTop = elem.offsetTop + elem.clientTop,
//             context = elem.getContext('2d'),
//             elements = [];

// // Add event listener for `click` events.
// elem.addEventListener('click', function(event) {
//     var x = event.pageX - elemLeft,
//         y = event.pageY - elemTop;

//         console.log(x);
//         console.log(y);

//         var ctx = elem.getContext("2d");
//         ctx.moveTo(0,0);
//         ctx.lineTo(x, y);
//         ctx.stroke();

//     // Collision detection between clicked offset and element.
//     elements.forEach(function(element) {
//         if (y > element.top && y < element.top + element.height 
//             && x > element.left && x < element.left + element.width) {
//             alert('clicked an element');
//         }
//     });

// }, false);

// // Add element.
// elements.push({
//     colour: '#05EFFF',
//     width: 150,
//     height: 100,
//     top: 20,
//     left: 15
// });

// // Render elements.
// elements.forEach(function(element) {
//     context.fillStyle = element.colour;
//     context.fillRect(element.left, element.top, element.width, element.height);
// })

const canvasEle = document.getElementById('myCanvas');
const context = canvasEle.getContext('2d');
let startPosition = {x: 0, y: 0};
let lineCoordinates = {x: 0, y: 0};

const getClientOffset = (event) => {
    const {pageX, pageY} = event.touches ? event.touches[0] : event;
    const x = pageX - canvasEle.offsetLeft;
    const y = pageY - canvasEle.offsetTop;

    return {
       x,
       y
    } 
}

const mouseDownListener = (event) => {
    startPosition = getClientOffset(event);
}

const mouseUpListener = (event) => {
    lineCoordinates = getClientOffset(event);
    console.log(lineCoordinates.x, lineCoordinates.y);
    context.beginPath();
   context.moveTo(startPosition.x, startPosition.y);
   context.lineTo(lineCoordinates.x, lineCoordinates.y);
   context.stroke();
}

canvasEle.addEventListener('mousedown', mouseDownListener);
canvasEle.addEventListener('mouseup', mouseUpListener);