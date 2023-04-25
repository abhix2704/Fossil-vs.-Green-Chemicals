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
NGLHV1 = 13.1; % in MWh per ton
NGLHV2 = 36.6 / 3600; % in MWh per m3
NGDensity = NGLHV2 / NGLHV1; % ton per m3
a = CEPCI2020/CEPCI2019;
b = CEPCI2021/CEPCI2019;
c = CEPCI2022/CEPCI2019;

%% Ammonia sensitivity

% BAU process
fileName = 'Methanol/BAU - 2015 - Methanol.xlsx';

matReq = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'B3:B10'); % unit/kg methanol
matPrices = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C3:C10'); % $/kg methanol

for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices * CEPCI2019/CEPCI2015;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2015;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2015;
    else
        prices = matPrices * CEPCI2022/CEPCI2015;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);

writematrix(totalPrices, 'Methanol breakdown.xlsx', 'Sheet', 'BAU breakdown', 'Range', 'B2')
writematrix(totalSum, 'Methanol breakdown.xlsx', 'Sheet', 'BAU breakdown', 'Range', 'J2')


% Green process
fileName = 'Methanol/Green Methanol - 2015.xlsx';

matReq = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'B3:B10'); % unit/kg methanol
matPrices = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C3:C10'); % $/kg methanol
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

CO2DACt = 164.2;
CO2DAC = [CO2DACt CO2DACt*a CO2DACt*b CO2DACt*c]./1000;
CO2DACLowt = 94.7;
CO2DACLow = [CO2DACLowt CO2DACLowt*a CO2DACLowt*b CO2DACLowt*c]./1000;
CO2DACHight = 233.7;
CO2DACHigh = [CO2DACHight CO2DACHight*a CO2DACHight*b CO2DACHight*c]./1000;

NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGPriceDAC = 3.5 * 47.1 * CEPCI2019 / CEPCI2018; % refer Keith 2018
NGPriceDAC = [NGPriceDAC NGPriceDAC*a NGPriceDAC*b NGPriceDAC*c]./1000;


j = 0;
for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices * CEPCI2019/CEPCI2015;
        j = 1;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2015;
        j = 2;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2015;
        j = 3;
    else
        prices = matPrices * CEPCI2022/CEPCI2015;
        j = 4;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
    CO2DACWithoutNG(j) = CO2DAC(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    CO2DACHighWithoutNG(j) = CO2DACHigh(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    CO2DACLowWithoutNG(j) = CO2DACLow(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    totalPrices(i,3) = matReq(3) * (CO2DACWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    CO2Low(i) = matReq(3) * (CO2DACLowWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    CO2High(i) = matReq(3) * (CO2DACHighWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    totalPrices(i,4) = matReq(4) * HWindAvg(j);
    hydrogenHigh(i) = matReq(4) * HWindHigh(j);
    hydrogenLow(i) = matReq(4) * HWindLow(j);
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);
totalSumHigh = totalSum - totalPrices(:,4) - totalPrices(:,3) + hydrogenHigh' * 1000 + CO2High' * 1000;
totalSumLow = totalSum - totalPrices(:,4)  - totalPrices(:,3) + hydrogenLow' * 1000 + CO2Low' * 1000;

writematrix(totalPrices, 'Methanol breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'B2')
writematrix(totalSum, 'Methanol breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'J2')
writematrix(totalSum - totalSumLow, 'Methanol breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'K2')
writematrix(totalSumHigh - totalSum, 'Methanol breakdown.xlsx', 'Sheet', 'Wind breakdown', 'Range', 'L2')


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

CO2DACt = 164.2;
CO2DAC = [CO2DACt CO2DACt*a CO2DACt*b CO2DACt*c]./1000;
CO2DACLowt = 94.7;
CO2DACLow = [CO2DACLowt CO2DACLowt*a CO2DACLowt*b CO2DACLowt*c]./1000;
CO2DACHight = 233.7;
CO2DACHigh = [CO2DACHight CO2DACHight*a CO2DACHight*b CO2DACHight*c]./1000;

NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGPriceDAC = 3.5 * 47.1 * CEPCI2019 / CEPCI2018; % refer Keith 2018
NGPriceDAC = [NGPriceDAC NGPriceDAC*a NGPriceDAC*b NGPriceDAC*c]./1000;


j = 0;
for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices * CEPCI2019/CEPCI2015;
        j = 1;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2015;
        j = 2;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2015;
        j = 3;
    else
        prices = matPrices * CEPCI2022/CEPCI2015;
        j = 4;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
    CO2DACWithoutNG(j) = CO2DAC(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    CO2DACHighWithoutNG(j) = CO2DACHigh(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    CO2DACLowWithoutNG(j) = CO2DACLow(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    totalPrices(i,3) = matReq(3) * (CO2DACWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    CO2Low(i) = matReq(3) * (CO2DACLowWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    CO2High(i) = matReq(3) * (CO2DACHighWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    totalPrices(i,4) = matReq(4) * HSolarAvg(j);
    hydrogenHigh(i) = matReq(4) * HSolarHigh(j);
    hydrogenLow(i) = matReq(4) * HSolarLow(j);
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);
totalSumHigh = totalSum - totalPrices(:,4) - totalPrices(:,3) + hydrogenHigh' * 1000 + CO2High' * 1000;
totalSumLow = totalSum - totalPrices(:,4)  - totalPrices(:,3) + hydrogenLow' * 1000 + CO2Low' * 1000;

writematrix(totalPrices, 'Methanol breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'B2')
writematrix(totalSum, 'Methanol breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'J2')
writematrix(totalSum - totalSumLow, 'Methanol breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'K2')
writematrix(totalSumHigh - totalSum, 'Methanol breakdown.xlsx', 'Sheet', 'Solar breakdown', 'Range', 'L2')

HSMRCCS = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'T2:T48');

CO2DACt = 164.2;
CO2DAC = [CO2DACt CO2DACt*a CO2DACt*b CO2DACt*c]./1000;
CO2DACLowt = 94.7;
CO2DACLow = [CO2DACLowt CO2DACLowt*a CO2DACLowt*b CO2DACLowt*c]./1000;
CO2DACHight = 233.7;
CO2DACHigh = [CO2DACHight CO2DACHight*a CO2DACHight*b CO2DACHight*c]./1000;

NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGPriceDAC = 3.5 * 47.1 * CEPCI2019 / CEPCI2018; % refer Keith 2018
NGPriceDAC = [NGPriceDAC NGPriceDAC*a NGPriceDAC*b NGPriceDAC*c]./1000;

j = 0;
for i = 1:length(naturalGasPrices)
    if i >= 1 && i <= 12
        prices = matPrices * CEPCI2019/CEPCI2015;
        j = 1;
    elseif i >= 13 && i <= 24
        prices = matPrices * CEPCI2020/CEPCI2015;
        j = 2;
    elseif i >= 25 && i <= 36
        prices = matPrices * CEPCI2021/CEPCI2015;
        j = 3;
    else
        prices = matPrices * CEPCI2022/CEPCI2015;
        j = 4;
    end
    totalPrices(i,1:length(matPrices)) = prices';
    totalPrices(i,1) = matReq(1) * naturalGasPrices(i) / 1000;
    totalPrices(i,5) = matReq(5) * elecPrices(i) / 1000;
    CO2DACWithoutNG(j) = CO2DAC(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    CO2DACHighWithoutNG(j) = CO2DACHigh(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    CO2DACLowWithoutNG(j) = CO2DACLow(j) - NGReqCarbonDioxide * NGPriceDAC(j);
    totalPrices(i,3) = matReq(3) * (CO2DACWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    CO2Low(i) = matReq(3) * (CO2DACLowWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    CO2High(i) = matReq(3) * (CO2DACHighWithoutNG(j) + NGReqCarbonDioxide * naturalGasPrices(i)/1000);
    totalPrices(i,4) = matReq(4) * HSMRCCS(i)/1000;
end

totalPrices = totalPrices .* 1000;
totalSum = sum(totalPrices,2);

writematrix(totalPrices, 'Methanol breakdown.xlsx', 'Sheet', 'SMR CCS breakdown', 'Range', 'B2')
writematrix(totalSum, 'Methanol breakdown.xlsx', 'Sheet', 'SMR CCS breakdown', 'Range', 'J2')
