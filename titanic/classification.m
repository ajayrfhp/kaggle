x=load('ex4x.dat');
y=load('ex4y.dat');
x=[ones(length(x),1),x];
m=length(x);
n=size(x,2);
O=[zeros(n,1)];

function ans=sigmoid(z)
m=size(z,1);
n=size(z,2);
for j=1:m,
for k=1:n, 
ans(j,k)=1/(1+exp(-z(j,k)));
endfor
endfor
endfunction

function j=cost(x,y,O)
m=size(x,1);
n=size(x,2);
g=sigmoid(x*O);
j=(1/m)*sum(-y'*(log(g))-((1-y)'*log(1-g)));
endfunction

function plot()
pos=find(y);
neg=find(y==0);
plot(x(pos,2),x(pos,3),'+')
hold on
plot(x(neg,2),x(neg,3),'o')
endfunction




function ans=enum(x,y,O)
m=size(x,1);
n=size(x,2);
g=sigmoid(x*O);
ans=x'*(g-y);

endfunction

function solve(x,y,O)
m=size(x,1);
n=size(x,2);
r=1;
for i=1:1500,
	
O=O-r*(1/m)*(enum(x,y,O));
endfor
disp(O);
endfunction

disp(cost(x,y,O));
solve(x,y,O);