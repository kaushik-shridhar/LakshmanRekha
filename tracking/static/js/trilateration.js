const canvas = document.getElementById('liveMonitor');
const ctx = canvas.getContext('2d');
// console.log(tp);

// console.log(tp);

class point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class circle {
    constructor(point, radius) {
        this.center = point;
        this.radius = radius;
    }
}

function getTwoPointsDistance(p1, p2) {
    dx = p1.x - p2.x;
    dy = p1.y - p2.y;
    d = Math.sqrt((dy*dy) + (dx*dx));
    return d;
}

function getTwoCirclesIntersectingPoints(c1, c2) {
    p1 = c1.center;
    p2 = c2.center;
    r1 = c1.radius;
    r2 = c2.radius;

    d = getTwoPointsDistance(p1, p2);

    /* Check for solvability. */
    if (d > (r1 + r2)) {
        /* no solution. circles do not intersect. */
        return false;
    }
    if (d < Math.abs(r1 - r2)) {
        /* no solution. one circle is contained in the other */
        return false;
    }

    a = (Math.pow(r1, 2) - Math.pow(r2, 2) + Math.pow(d, 2)) / (2*d);
    h = Math.sqrt(Math.pow(r1, 2) - Math.pow(a, 2));
    x0 = p1.x + a*(p2.x - p1.x)/d
    y0 = p1.y + a*(p2.y - p1.y)/d
    rx = -(p2.y - p1.y) * (h/d)
    ry = -(p2.x - p1.x) * (h / d)
    return [new point(x0+rx, y0-ry), new point(x0-rx, y0+ry)]
}

function getAllInterSectingPoints(circles) {
    var points = [];
    num = circles.length;
    for (i=0;i<num;i++) {
        j = i+1;
        for (k=j;k<num;k++) {
            res = getTwoCirclesIntersectingPoints(circles[i], circles[k]);
            if (res) {
                points.push(res);
            }
        }
    }
    return points;
}

function createCircle(x, y, r) {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, 2*Math.PI);
    ctx.stroke();
}

function createPoint(x, y) {
    var pointSize = 2;
    ctx.beginPath();
    ctx.arc(x, y, pointSize, 0, 2*Math.PI);
    ctx.strokeStyle = '#ff0000';
    ctx.stroke();
}

function isContainedInCircles(point, circles) {
    for (i=0;i<circles.length;i++) {
        if (getTwoPointsDistance(point, circles[i].center) > (circles[i].radius)) {
            return false;
        }
    }
    return true;
}

function getPolygonCenter(points) {
    var center = new point(0, 0);
    var num = points.length;
    for (i=0;i<num;i++) {
        center.x += points[i].x;
        center.y += points[i].y;
    }
    center.x /= num;
    center.y /= num;
    return center;
}

let p1 = new point(100, 100);
let p2 = new point(200, 200);
let p3 = new point(200, 100);

let c1 = new circle(p1, 100);
let c2 = new circle(p2, 100);
let c3 = new circle(p3, 100);

createCircle(p1.x, p1.y, c1.radius);
createCircle(p2.x, p2.y, c2.radius);
createCircle(p3.x, p3.y, c3.radius);

var circle_list = [c1, c2, c3];

var inner_points = [];

var p = getAllInterSectingPoints(circle_list);
console.log(p.length);

var intersecting_points = [];

// for (i=0;i<p.length;i++) {
//     for (j=0;j<2;j++) {
//         createPoint(p[i][j].x, p[i][j].y);
//         intersecting_points.push(p[i][j]);
//     }
// }

//console.log(intersecting_points);

// for (i=0;i<intersecting_points.length;i++) {
//     if (isContainedInCircles(intersecting_points[i], circle_list)) {
//         console.log(intersecting_points[i]);
//     }
// }

//console.log(inner_points);