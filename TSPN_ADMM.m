function TSPN = TSPN_ADMM(mask_image,mask)
% X = mask_image; Y = X; W = X;
%%test
% clear;close all;
% image = rand(100,70)*rand(70,100);%原矩阵
% % image2 = double(imread('demo_figure.jpg'));
[m,n] = size(mask_image);
% % m=1080;
% % n=1080;
% % image = image2(:,:,1);
% m=100;n=100;
% maxValue = max(max(image))
% image = image/maxValue;%归一化
% mask = zeros(m,n);%采样矩阵
% choice=n*0.2
% for i=1: m
%          choo=randi([1,n],1,choice);
%         mask(i,choo)=1;
%        
% end
% mask(55:60,:)=0;
% mask(:,55:58)=0
% mask_image = image.*mask;
% figure;imagesc(abs(image))
% figure;imagesc(abs(mask_image))
%参数设置
maxIter = 30;
beta = 0.03;%0.03
p = 0.1;%0.05
miu = 0.05;%0.01
rou = 1.03;
r   = 5;
tol = 1e-40;
PICKS = find(mask==1);
X=mask_image;D=mask_image;W=zeros(m,n);Y=zeros(m,n);Z=zeros(m,n); %W就是文章中的γ X就是Sest

for i = 1:maxIter
    %update X
%     i
    lambda=1/(2*beta);   
    Temp = W+Z/beta;
    [U,S,V] = svd(0.5*(D+Y/beta+idct2(Temp)),'econ');
    tau = (2*lambda*(1-p))^(1/(2-p))+lambda*p*(2*lambda*(1-p))^((p-1)/(2-p));
    Sigmma=(abs(S)-lambda*p*(S^(p-1))).*max(sign(S-tau),0);
    Xtemp = X; 
    X = U*Sigmma*V';
    %update W
    XX = dct2(X)-Z/beta;
    W = (abs(XX)-miu/beta).*(sign(XX));
    %update D
%     [U1,~,V1] = svd(D); %参考TNNR_ADMM
%     A = (U1(:,2:r)).';
%     B = (V1(:,2:r)).';
%     D = X+(1/beta)*(p*A'*((A*D*B')^(p-1))*B-Y);
    D = X+(1/beta)*(-Y);
    D(PICKS) = mask_image(PICKS);
    %update Y
    Y = Y+beta*(D-X);
    %update Z
    Z = Z+beta*(W-dct2(X));
    %uodate beta
    beta = rou*beta;
    TOLL = norm(X-Xtemp,'fro')/norm(X,'fro');
    if TOLL<=tol
        break;
    end
end
% X = X*maxValue;
TSPN = X;
end
% figure;
% imagesc(abs(X));title('TSPR');

% %比较
% %SVT
% tao = sqrt(100*100); step = 1.2*0.2; 
% SVT_recon = SVT(mask_image,mask,tao,step,maxIter,tol);
% figure; imagesc(SVT_recon);title('SVT');
% % %Sp_lp
% gamma = 1; p = 0.1;
% Sp_lp_recon = Sp_lp(mask_image,mask,gamma,p,maxIter,tol);
% figure; imagesc(Sp_lp_recon);title('Sp_lp');
% %TNNR_ADMM
% beta = 1; rank_r = 1;
% TNNR_recon = TNNR_ADMM(mask_image,mask,beta,rank_r,maxIter,tol);
% figure;imagesc(TNNR_recon);