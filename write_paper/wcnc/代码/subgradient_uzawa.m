clc
clear all
%�ô��ݶȷ����x(1)^2+x(2)^2����Сֵ��Լ������Ϊ��2*x(1)+x(2)��������
% ���ߣ��Ϻ���ͨ��ѧ ����
lambda=0;
x0=[0 0];
for n=1:20
warning('off');
f=@(x)x(1)^2+x(2)^2+lambda*(2*x(1)+x(2)+4);
options=optimset('Gradobj','off');
x=fminunc(f,x0,options);
rho=0.8^n;
lambda=lambda+rho*(2*x(1)+x(2)+4);  
n=n+1;
end
[x,f]=fminunc(f,x0,options)