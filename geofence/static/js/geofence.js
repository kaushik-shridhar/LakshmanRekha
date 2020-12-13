// sorting the array
var i;
for (i = 0; i < start_point.length - 1; i++){
    end_point[i] = start_point[i + 1];
}
end_point[0] = start_point[start_point.length - 1];

context.clearRect(0, 0, canvas.width, canvas.height)
for(i = 0; i < start_point.length; i++){
    context.beginPath();
    context.moveTo(start_point[i][0], start_point[i][1]);
    context.lineTo(end_point[i][0], end_point[i][1]);
    context.stroke();
}
console.log(start_point[1]);
console.log(end_point);