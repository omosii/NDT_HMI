clc;close all ;clear;
%% 待填充向量生成
S_r = [1 2 3 0 5 6 7 8 0 10];

% S_r = rand(1,8); S_r(2) = 0; S_r(6) = 0;
%% toeplitz变换
S_toep = toeplitz(S_r(1:5),S_r(6:10))
maxv = max(max(abs(S_toep)));
%% toeplitz变换后矩阵 SVD分解
P = (S_toep ~= 0);
% [U,S,V]=svd(S_toep*size(S_toep,1)*size(S_toep,2)/sum(P(:)),'econ');
% figure; plot( (1:length(diag(S)))/length(diag(S)) ,...
%             diag(S)/sum(diag(S)) ,"Color","r","Marker",".");


%% MC算法（矩阵填充算法）
% d = 0:0.01:10;
% S_r_4_value = zeros(1,length(d));
% for i = 1:length(d)
[X,A,B]=MC_MAX_pgm(S_toep./maxv,P,5,1,0.001,300);%S_toep,P,5,2.09,0.94,300
% X = TSPN_ADMM(S_toep./maxv,P);
X = X.*maxv
S_itoep = iTrsTP(X);
% S_r_4_value(i) = S_itoep(2);
% end
% plot(S_r_4_value);