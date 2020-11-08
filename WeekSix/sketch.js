function preload() {
  A = loadImage("A.png");
  B = loadImage("B.png");
  C = loadImage("C.png");
  D = loadImage("D.png");
  E = loadImage("E.png");
  F = loadImage("F.png");
  G = loadImage("G.png");
  H = loadImage("H.png");
  I = loadImage("I.png");
  J = loadImage("J.png");
  K = loadImage("K.png");
  L = loadImage("L.png");
  M = loadImage("M.png");
  N = loadImage("N.png");
  O = loadImage("O.png");
  P = loadImage("P.png");
  Q = loadImage("Q.png");
  U = loadImage("U.png");
  R = loadImage("R.png");
  S = loadImage("S.png");
  T = loadImage("T.png");
  V = loadImage("V.png");
  W = loadImage("W.png");
  X = loadImage("X.png");
  Y = loadImage("Y.png");
  Z = loadImage("Z.png");
  one = loadImage("1.png");
  two = loadImage("2.png");
  three = loadImage("3.png");
  four = loadImage("4.png");
  five = loadImage("5.png");
  six = loadImage("6.png");
  seven = loadImage("7.png");
  eight = loadImage("8.png");
  nine = loadImage("9.png");
  zero = loadImage("0.png");
}

let welcome = "Learn ASL! Press any letter or number to see the sign."

function asl(img) {
  background(255);
  imageMode(CORNER);
  image(img, 0, 0, 700, 700);
}

let n=0; // moves img postition over for hello
let w=0; // and for world

function hello(img) {
  imageMode(CORNER);
  image(img, 90+n, 60, 100, 100);
  n = n + 100;
}

function world(img) {
  imageMode(CORNER);
  image(img, 90+w, 160, 100, 100);
  w = w + 100;
}

function setup() {
  createCanvas(700, 600);
  textSize(24);
  text(welcome, 60, 300, 690, 700);
  hello(H);
  hello(E);
  hello(L);
  hello(L);
  hello(O);
  world(W);
  world(O);
  world(R);
  world(L);
  world(D);
}


function draw() {
  if ((keyIsPressed == true) && ((key == 'a') || (key == 'A'))) {
    asl(A);
} else if ((keyIsPressed == true) && ((key == 'b') || (key == 'B'))) {
    asl(B);
} else if ((keyIsPressed == true) && ((key == 'c') || (key == 'C'))) {
  asl(C);
} else if ((keyIsPressed == true) && ((key == 'd') || (key == 'D'))) {
  asl(D);
} else if ((keyIsPressed == true) && ((key == 'e') || (key == 'E'))) {
  asl(E);
} else if ((keyIsPressed == true) && ((key == 'f') || (key == 'F'))) {
  asl(F);
} else if ((keyIsPressed == true) && ((key == 'g') || (key == 'G'))) {
  asl(G);
} else if ((keyIsPressed == true) && ((key == 'h') || (key == 'H'))) {
  asl(H);
} else if ((keyIsPressed == true) && ((key == 'i') || (key == 'I'))) {
  asl(I);
} else if ((keyIsPressed == true) && ((key == 'j') || (key == 'J'))) {
  asl(J);
} else if ((keyIsPressed == true) && ((key == 'k') || (key == 'K'))) {
  asl(K);
} else if ((keyIsPressed == true) && ((key == 'l') || (key == 'L'))) {
  asl(L);
} else if ((keyIsPressed == true) && ((key == 'm') || (key == 'M'))) {
  asl(M);
} else if ((keyIsPressed == true) && ((key == 'n') || (key == 'N'))) {
  asl(N);
} else if ((keyIsPressed == true) && ((key == 'o') || (key == 'O'))) {
  asl(O);
} else if ((keyIsPressed == true) && ((key == 'p') || (key == 'P'))) {
  asl(P);
} else if ((keyIsPressed == true) && ((key == 'q') || (key == 'Q'))) {
  asl(Q);
} else if ((keyIsPressed == true) && ((key == 'r') || (key == 'R'))) {
  asl(R);
} else if ((keyIsPressed == true) && ((key == 's') || (key == 'S'))) {
  asl(S);
} else if ((keyIsPressed == true) && ((key == 't') || (key == 'T'))) {
  asl(T);
} else if ((keyIsPressed == true) && ((key == 'u') || (key == 'U'))) {
  asl(U);
} else if ((keyIsPressed == true) && ((key == 'v') || (key == 'V'))) {
  asl(V);
} else if ((keyIsPressed == true) && ((key == 'w') || (key == 'W'))) {
  asl(W);
} else if ((keyIsPressed == true) && ((key == 'x') || (key == 'X'))) {
  asl(X);
} else if ((keyIsPressed == true) && ((key == 'y') || (key == 'Y'))) {
  asl(Y);
} else if ((keyIsPressed == true) && ((key == 'z') || (key == 'Z'))) {
  asl(Z);
} else if ((keyIsPressed == true) && (key == 1)) {
  asl(one);
} else if ((keyIsPressed == true) && (key == 2)) {
  asl(two);
} else if ((keyIsPressed == true) && (key == 3)) {
  asl(three);
} else if ((keyIsPressed == true) && (key == 4)) {
  asl(four);
} else if ((keyIsPressed == true) && (key == 5)) {
  asl(five);
} else if ((keyIsPressed == true) && (key == 6)) {
  asl(six);
} else if ((keyIsPressed == true) && (key == 7)) {
  asl(seven);
} else if ((keyIsPressed == true) && (key == 8)) {
  asl(eight);
} else if ((keyIsPressed == true) && (key == 9)) {
  asl(nine);
} else if ((keyIsPressed == true) && (key == 0)) {
  asl(zero);
} 


}


