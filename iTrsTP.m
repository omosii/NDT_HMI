function M = iTrsTP(TP)
    %输入由向量截为两半构成的TP矩阵。还原出行向量。
    if size(TP,1)==150
        M = TP(:,1)';
    else
        % col1 = flip(TP(:,1))';
        % raw1 = TP(1,2:end);
        % M = [col1 raw1];
        
        % col1 = (TP(:,1))';
        % raw1 = TP(1,2:end);
        % M = [col1 raw1];

%         C = spdiags(TP);                                     %提取稿疏矩阵非零元素重排，按照正对角线重排，缺少的元素衿0;
        C = spdiags(TP,[0:-1:1-size(TP,1),1:(size(TP,2)-1)]);
        H_mean = sum(C)./sum(C~=0);
        H_mean(isnan(H_mean)) = 0;                          %计算矩阵每列非零元素的列均忿
        M = H_mean;
    end
end

% function M = iTrsTP(TP)  
%     % 假设TP的第一列是原始向量的后半部分，第一行的剩余部分是前半部分  
%     if size(TP, 1) > 1 && size(TP, 2) > 1  
%         % 提取前半部分和后半部分  
%         first_half = TP(:, 1);
%         second_half = TP(1, 2:end)';  
%           
%           
%         % 合并两部分以还原原始向量  
%         M = [first_half; second_half]';  
%     else  
%         % 如果TP不符合预期的结构，返回一个错误或警告  
%         error('TP矩阵的结构不符合预期，无法还原原始向量。');  
%     end  
% end