function [ X,iterations,error ] = SVT_myx(M,P,T,delta,itermax,tol)
%奇异值阈值算法 Single value thresholding algorithm，SVT
%                  min  ||X||*
%               s.t. P(X-M) = 0
% 输出
% X: 恢复矩阵
% iterations: 迭代次数
% error: 误差
% 输入 M P不能省
% M: 观测矩阵
% P: 采样矩阵
% T: 参数tao
% delta: 步长
% itermax: 最大迭代次数
% tol: 终止规则 误差小于tol终止

% initialization
% Y = zeros(size(M));

 Y = M;
iterations = 0;

if nargin < 3
    T =  sqrt(n1*n2);
end
if nargin < 4
    delta = 1;
end
if nargin < 5 
    itermax = 50 ;
end
if nargin < 6
    tol = 1e-9;
end
%初始化
% Y = k0*delta*P.*M; % kicking by k0 steps
incre = 1;
r=0;
for ii = 1:itermax
    ii;
%     s = r+1;
    [U, S, V] = svd(Y, 'econ') ;
    S = sign(S) .* max(abs(S) - T, 0) ;
    save('s.mat','S');
    X = U*S*V' ;
    Y = Y + delta* P.* (M-X);
    % 误差计算
    error= norm( P.* (M-X),'fro' )/norm( P.* M,'fro' );
    if error<tol
        break;
    end
    % update iterations
    iterations = ii ;
end
end
