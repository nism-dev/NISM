var prmpt = require('prompt-sync')();

// Global variables
var lenC = Number(prmpt("> Length of coordinate :: "))

var nxy = Math.abs(cred[0][0] - cred[1][0]) + abs(cred[0][1] - cred[1][1]);
var startCoord = cred()
var origData = Number(prmpt("Enter data to send :: "));
var dList = splitData(origData * 1000000);
var d1 = Number(dList[0]);
var d2 = Number(dList[1]);
var d3 = Number(dList[2]);

// Premodel

function splitData(k) {
    var a = getRandom(1, Math.floor(k/2));
    var b = getRandom(1, Math.floor(k/2));
    var c = k - (a + b);
    return [a, b, c];
}

function getRandom(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generatePrime(min, max) {
    var k = false;
    var c = 0;
    while (k === false) {
        c = getRandom(min, max);
        for (var i = 2; i < Math.floor(Math.sqrt(c)+1); i++) {
            if (c % i === 0) {
                k = true;
            }
        }
        if (k === true) {
            k = false;
        }
        else {
            return c;
        }
    }
}

function checkPrime(j) {
    var k = false;
    while (k === false) {
        for (var i = 2; i < Math.floor(Math.sqrt(j)+1); i++) {
            if (j % i === 0) {
                k = true;
            } 
        }
        if (k === true) {
            return false;
        }
        else {
            return true;
        }
    }
}

function fac(k) {
    var l = []
    for (var i = 2; i < Math.ceil(Math.sqrt(k)+1); i++) {
        l.push(i);
    }
    return l;
}

function phi(n) {
    var k = fac(n);
    var r = n;
    for (var i = 0; i < k.length; i++) {
        r *= 1 - (1/k[i]);
    }
    return r;
}

function gcd(m, n) {
    var ml = fac(m);
    var nl = fac(n);
    var g = 1;
    for (var i = 0; i < ml.length; i++) {
        for (var j = 0; j < nl.length; j++) {
            if (ml[i] === nl[j]) {
                g *= nl[j];
            }
        }
    }
    return g;
}


// RSA

function createKey(min, max) {
    var p = generatePrime(min, max);
    var q = generatePrime(min, max);
    e = 0;
    d = 0;
    for (var i = 2; i < Math.floor(phi(p*q)+1); i++) {
        if (gcd(i, phi(p*q)) == gcd(i, p*q) && gcd(i, p*q) == 1) {
            e = i;
        }
    }
    for (var j = 0; j < Math.floor(phi(p*q)+1); j++) {
        if ((e*j) % phi(p*q) == 1) {
            d = j;
        }
    }
    return [[e, p*q], [d, p*q]];
}

function encrypt(e, pq, s) {
    return ((s ** e) % pq);
}

function decrypt(d, pq, k) {
    return ((k ** d) % pq);
}

// Model4 (N) Python

// 
function nodeFn(nodeList) {
    var index = len(list(nodeList)) +1;
    var keyList = createKey();
    var e = keyList[0][0];
    var d = keyList[1][0];
    var pq = keyList[0][1];
    var newNode = [index, e, d, pq];
    nodeList.push(newNode);
    return nodeList;
}

function setNodeList(nodeList, len) {
    for(var i = 0; i < len; i++) {
        nodeList = nodeFn(nodeList);
    }
    return nodeList;
}

function createCoord(coordList, lenC) {
    var indexList = [];
    for(var i = 0; i < (lenC ** 2 + 1); i++) {
        indexList.push(i);
    }
    for(var i = 0; i < lenC; i++) {
        var tempList = [];
        for(var j = 0; j < lenC; i++) {
            tempList.push(indexList[i * lenC + j]);
        }
        coordList.push(tempList);
    }
    return coordList;
}

function currentCoord(passedRoutelist, currentPosR) {
    console.log(`> Current Position:: ${currentCoord}`);
    passedRoutelist += currentPosR;
    return passedRoutelist;
}

function isRoutePassed(coord, passedRouteListR) {
    var iRPcv = false;
    for(var i = 0; i < passedRouteListR.length; i++) {
        if(coord === passedRouteListR[i]) {
            iRPcv = true;
        }
    }
    return iRPcv;
}

function moveR1(currentPosR, xy, d, passedRouteR) {
    if(xy === 'x') {
        currentPosR[0] += Number(d);
    } else if (xy === 'y') {
        currentPosR[1] += Number(d);
    } else {
        console.log("> ERR: Fuck you, second parameter can only be x or y.");
    }
    passedRouteR += currentPosR;
    console.log(`> Current Position:: ${currentPosR}`);
}

function setCoord() {
    var coordList = [];
    coordList = createCoord(coordList, lenC);
    var nodeList = [];
    nodeList = setNodeList(nodeList, lenC ** 2);

    for(var i = 0; i < coordList.length; i++) {
        var tempNodeList = [];
        for(var j = 0; j < lenC; j++) {
            tempNodeList.push(NodeList[i * lenC + j]);
        }
        console.log(`  ${coordList}`);
    }
    var senderIndex = Number(prmpt("> Index of sender :: "));
    var recieverIndex = Number(prmpt("> Index of reciever :: "));
    var sCred = [];
    var rCred = [];
    for(var x = 0; x < lenC; x++) {
        for(var y = 0; y < lenC; y++) {
            if((lenC * y + x + 1) === senderIndex) {
                sCred = [x+1, y+1];
            }
            if((lenC * y + x + 1) === recieverIndex) {
                rCred = [x+1, y+1];
            }
        }
    }
    var cred = [sCred, rCred];
    var credR1 = cred[0];
    var credR12 = cred[1];
}

// Route II
function r2() {
    console.log("\n\n>Starting Route 2 Calculation... ");
    var passedRoute = [];
    var currentPos = cred[0];
    var recb = (nxy + (nxy % 2))/2 + d1;
    var nx, ny;
    while (currnetPos != [cred[1][0], cred[1][1]]) {
        recb -= 1;
        passedRoute = currentCoord(passedRoute, currentPos);
        nx = currnetPos[0] - cred[1][0];
        ny = currentPos[1] - cred[1][1];
        if (nx < 0) {
            if (ny < 0) {
                if ((currentPos[0] + currentPos[1]) % 2 == 0) {
                    currentPos[1] += 1;
                }
                else if (currentPos[0] + currentPos[1] % 2 == 1) {
                    currentPos[0] += 1;
                    passedRoute = currentCoord(passedRoute, currentPos);
                    currentPos[1] += 1;
                }
            }
            else if (ny > 0) {
                if ((currentPos[0] + currentPos[1]) % 2 == 1) {
                    currentPos[1] -= 1;
                }
                else if ((currentPos[0] + currentPos[1]) % 2 == 0) {
                    currentPos[0] += 1;
                    passedRoute = currentCoord(passedRoute, currentPos);
                    currentPos[1] -= 1;
                }
            }
            else {
                currentPos[0] += 1
            }
        }
        else if (nx > 0) {
            if (ny < 0) {
                if ((currentPos[0] + currentPos[1]) % 2 == 0) {
                    currentPos[1] += 1;
                }
                else if ((currentPos[0] + currentPos[1]) % 2 == 1) {
                    currentPos[0] -= 1;
                    passedRoute = currentCoord(passedRoute, currentPos);
                    currentPos[1] += 1;
                }
            }
            else if (ny > 0) {
                if ((currentPos[0] + currentPos[1]) % 2 == 1) {
                    currentPos[1] -= 1;
                } 
                else if ((currentPos[0] + currentPos[1]) % 2 == 0) {
                    currentPos[0] -= 1;
                    passedRoute = currentCoord(passedRoute, currentPos);
                    currentPos[1] -= 1;
                }
            }
            else {
                currentPos[0] -= 1;
            }
        }
        else {
            if (ny < 0) {
                if ((currentPos[0] + currentPos[1]) % 2 == 0) {
                    currentPos[1] += 1;
                }
                else if ((currentPos[0] + currentPos[1]) % 2 == 1) {
                    currentPos[0] -= 1;
                    passedRoute = currentCoord(passedRoute, currentPos);
                    currentPos[1] += 1;
                }
            }
            else if (ny > 0) {
                if ((currentPos[0] + currentPos[1]) % 2 == 1) {
                    currentPos[1] -= 1;
                }
                else if ((currentPos[0] + currentPos[1]) % 2 == 0) {
                    currentPos[0] -= 1;
                    passedRoute = currentCoord(passedRoute, currentPos);
                    currentPos[1] -= 1;
                }
            }
            else {
                console.log(`> Current Position :: ${currentPos}`);
                passedRoute = currentCoord(passedRoute, currentPos);
            }
        }
    }
    console.log(`> Final Position :: ${currentPos}`);
    console.log(`===> Process completed for :: Route 2 (SHORTEST)`);
    passedRouteList = [];
    for (var i = 0; i < passedRoute.length; i++) {
        if (i % 2 == 0) {
            tempList = [passedRoute[i], passedRoute[i+1]];
            passedRouteList.push(tempList);
        }
    }
    passedRouteList.push(credR12);
    console.log(`\n> Passed Routes :: ${passedRouteList}`);
    console.log(`> Recieved Data :: ${recb}`);
    passedRouteList.pop(passedRouteList.length - 1);
}