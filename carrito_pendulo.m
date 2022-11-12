function carrito_pendulo
% Alumna: Gabriela Hilario Acuapan
% Fecha: 11/Noviembre/2022
% Descripción: Examen corregido de Modelado de Sistemas Dinámicos

%% Parámetros
mc = 5;             % masa carrito
mp = 1;             % masa péndulo
l = 4;              % longitud varilla
g = 9.81;           % gravedad
f = 1;              % fuerza aplicada u = f

%% Resovler las ecuaciones de movimiento
%condiciones iniciales [x=0, th=45°, xdot=0, thdot=0]
ci = [0 pi/2 0 0];
[t, q] = ode45(@eq1, [0:0.02:10], ci);

%% Figuras
figure(1)
plot(t, q(:,1), LineWidth=1.5, Color='c')
legend('x(t)')
title('Posición del carrito')
xlabel('t [s]','fontsize',12); ylabel('[m]','fontsize',12);
grid on

figure(2)
plot(t, q(:,2), LineWidth=1.5, Color='m')
legend('\theta (t)')
title('Posición del péndulo')
xlabel('t [s]','fontsize',12); ylabel('[\pi]','fontsize',12);
grid on

figure(3)
plot(t, q(:,3), LineWidth=1.5, Color='b')
legend('dx(t)/dt')
title('Velocidad del carrito')
xlabel('t [s]','fontsize',12); ylabel('[m/s]','fontsize',12);
grid on

figure(4)
plot(t, q(:,4),LineWidth=1.5, Color='r')
legend('d\theta(t)/dt')
title('Velocidad del péndulo')
xlabel('t [s]','fontsize',12); ylabel('[\pi/s]','fontsize',12);
grid on

figure(5)
plot(q(:,1), q(:,3), LineWidth=1.5, Color='k')
title('Retrato fase')
xlabel('x(t)','fontsize',12); ylabel('dx(t)/dt','fontsize',12);
grid on

figure(6)
plot(q(:,2), q(:,4), LineWidth=1.5, Color='g')
title('Retrato fase')
xlabel('\theta(t)','fontsize',12); ylabel('d\theta(t)/dt','fontsize',12);
grid on

function qddot = eq1(t,q)
    %% H*qddot + C*qdot + G = B*u
    th = q(2);
    %Matriz de Inercia H(q)
    H = [(mc + mp), (mp*l*cos(th)); (mp*l*cos(th)), (mp*l^2)];
    %Matriz de Coriolis C(q,qdot)
    C = [0, -q(4)*(mp*l*sin(th)); 0, 0];
    %Vector de Gravedad
    G = [0; mp*g*l*sin(th)];
    %Fuerzas externas
    B = f*[1; 0];

    xi1 = [q(3);q(4)];
    xi2 = H\(B-C*xi1-G);

    qddot = [xi1;xi2];
end
end