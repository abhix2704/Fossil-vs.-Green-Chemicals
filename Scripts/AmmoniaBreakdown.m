clear 
close all
clc

%% CEPCI indexes
CEPCI2008 = 575.4;
CEPCI2012 = 584.6;
CEPCI2015 = 556.8;
CEPCI2017 = 567.5;
CEPCI2018 = 603.1;
CEPCI2019 = 607.5;
CEPCI2020 = 596.2;
CEPCI2021 = 708.0;
CEPCI2022 = 817.5;

naturalGasPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'C2:C48');
elecPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'S2:S48');

%% Ammonia sensitivity

% BAU process
fileName = 'Ammonia/BAU - 2019.xlsx';

matReq = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'F3:F10'); % unit/kg ammonia
matPrices = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'G3:G10'); % $/kg ammonia

for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2019;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2019;
    else
        prices = matPrices * CEPCI2022/CEPCI2019;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);

writematrix(totalPrices, 'Ammonia breakdown.xlsx', 'Sheet', 'BAU breakdown', 'Range', 'B2')
writematrix(totalSum, 'Ammonia breakdown.xlsx', 'Sheet', 'BAU breakdown', 'Range', 'J2')


% Green process
fileName = 'Ammonia/Green ammonia - 2019.xlsx';

matReq = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'F3:F10'); % unit/kg ammonia
matPrices = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'G3:G10'); % $/kg ammonia

HWind = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'LCOH', 'Range', 'B17:Q17');

j = 1;
for i = 2:length(HWind)
    if mod(i,2) == 0 && mod(i,4) ~= 0
        HWindAvg(j) = HWind(i-1);
        HWindLow(j) = HWind(i);
        HWindHigh(j) = HWind(i+1);
        j = j + 1;
    end
end

j = 0;
for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices;
        j = 1;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2019;
        j = 2;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2019;
        j = 3;
    else
        prices = matPrices * CEPCI2022/CEPCI2019;
        j = 4;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
    totalPrices(i,4) = matReq(4) * HWindAvg(j);
    hydrogenHigh(i) = matReq(4) * HWindHigh(j);
    hydrogenLow(i) = matReq(4) * HWindLow(j);
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);
totalSumHigh = totalSum - totalPrices(:,4) + hydrogenHigh' * 1000;
totalSumLow = totalSum - totalPrices(:,4) + hydrogenLow' * 1000;

writematrix(totalPrices, 'Ammonia breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'B2')
writematrix(totalSum, 'Ammonia breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'J2')
writematrix(totalSum - totalSumLow, 'Ammonia breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'K2')
writematrix(totalSumHigh - totalSum, 'Ammonia breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'L2')

HSolar = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'LCOH', 'Range', 'B18:Q18');

j = 1;
for i = 2:length(HWind)
    if mod(i,2) == 0 && mod(i,4) ~= 0
        HSolarAvg(j) = HSolar(i-1);
        HSolarLow(j) = HSolar(i);
        HSolarHigh(j) = HSolar(i+1);
        j = j + 1;
    end
end

j = 0;
for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices;
        j = 1;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2019;
        j = 2;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2019;
        j = 3;
    else
        prices = matPrices * CEPCI2022/CEPCI2019;
        j = 4;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
    totalPrices(i,4) = matReq(4) * HSolarAvg(j);
    hydrogenHigh(i) = matReq(4) * HSolarHigh(j);
    hydrogenLow(i) = matReq(4) * HSolarLow(j);
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);
totalSumHigh = totalSum - totalPrices(:,4) + hydrogenHigh' * 1000;
totalSumLow = totalSum - totalPrices(:,4) + hydrogenLow' * 1000;

writematrix(totalPrices, 'Ammonia breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'B2')
writematrix(totalSum, 'Ammonia breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'J2')
writematrix(totalSum - totalSumLow, 'Ammonia breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'K2')
writematrix(totalSumHigh - totalSum, 'Ammonia breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'L2')

HSMRCCS = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'T2:T48');

j = 0;
for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices;
        j = 1;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2019;
        j = 2;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2019;
        j = 3;
    else
        prices = matPrices * CEPCI2022/CEPCI2019;
        j = 4;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
    totalPrices(i,4) = matReq(4) * HSMRCCS(i) / 1000;
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);


writematrix(totalPrices, 'Ammonia breakdown.xlsx', 'Sheet', 'SMR CCS breakdown', 'Range', 'B2')
writematrix(totalSum, 'Ammonia breakdown.xlsx', 'Sheet', 'SMR CCS breakdown', 'Range', 'J2')
