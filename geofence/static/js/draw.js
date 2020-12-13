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
    start_point[i] = [startPosition.x, startPosition.y];
    end_point[i] = [lineCoordinates.x, lineCoordinates.y];
    //console.log(start_point);
    context.beginPath();
    context.moveTo(startPosition.x, startPosition.y);
    context.lineTo(lineCoordinates.x, lineCoordinates.y);
    context.stroke();
    console.log(start_point);
    console.log(end_point);
    i++;
}


canvasEle.addEventListener('mousedown', mouseDownListener);
canvasEle.addEventListener('mouseup', mouseUpListener);
