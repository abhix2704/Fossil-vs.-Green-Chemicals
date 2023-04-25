clear 
close all
clc

%% CEPCI indexes
CEPCI2008 = 575.4;
CEPCI2009 = 521.9;
CEPCI2012 = 584.6;
CEPCI2015 = 556.8;
CEPCI2017 = 567.5;
CEPCI2018 = 603.1;
CEPCI2019 = 607.5;
CEPCI2020 = 596.2;
CEPCI2021 = 708.0;
CEPCI2022 = 817.5;

naturalGasPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'C2:C48');
elecPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'S2:S48')/1000;

% coalPrices = 0:50:5000;
NGLHV1 = 13.1; % in MWh per ton
NGLHV2 = 36.6 / 3600; % in MWh per m3
NGDensity = NGLHV2 / NGLHV1; % ton per m3
a = CEPCI2020/CEPCI2019;
b = CEPCI2021/CEPCI2019;
c = CEPCI2022/CEPCI2019;

%% Ammonia sensitivity

% BAU process
fileName = 'Ammonia/BAU - 2019.xlsx';

ammoniaPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C24:C24') * 1000; % USD2019 per ton
naturalGasReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D5:D5'); % in ton/hr
naturalGasReq = naturalGasReq + readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D15:D15'); % in ton/hr
naturalGasPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E5:E5') * CEPCI2019 / CEPCI2018; % in USD2019 per ton
elecReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D9:D9'); % in kWh/hr
elecPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E9:E9') * CEPCI2019 / CEPCI2018; % in USD2019 per kWh
ammoniaProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C23:C23') / 1000; % amount of ammonia produced in ton/hr
hydrogenProduced = 12.34; % ton per hour
hydrogenPrice = 1370; % USD2019 per ton

hydrogenWithoutNG = hydrogenPrice - (naturalGasReq * naturalGasPrice) / hydrogenProduced;
hydrogenWithoutNG = hydrogenWithoutNG * CEPCI2022 / CEPCI2019; % USD2022 per ton

ammoniaPriceWithoutNG = ammoniaPrice - (naturalGasReq * naturalGasPrice + elecReq * elecPrice) / ammoniaProduced; % USD2019 per ton
ammoniaPriceWithoutNG = [ammoniaPriceWithoutNG ammoniaPriceWithoutNG*a...
    ammoniaPriceWithoutNG*b ammoniaPriceWithoutNG*c]; 

j = 1;
for i = 1:length(naturalGasPrices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    elseif i > 24 && i <= 36
        j = 3;
    else
        j = 4;
    end
    ammoniaPrices(i) = (ammoniaPriceWithoutNG(j) + (naturalGasPrices(i) * naturalGasReq +...
        elecPrices(i) * elecReq) ./ ammoniaProduced);
end
prices = ammoniaPrices';
writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia MP', 'Range', 'D2')

naturalGasPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia MP', 'Range', 'F2:F48');
elecPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia MP', 'Range', 'G2:G48')/1000;

j = 1;
for i = 1:length(naturalGasPrices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    elseif i > 24 && i <= 36
        j = 3;
    else
        j = 4;
    end
    ammoniaPrices(i) = (ammoniaPriceWithoutNG(j) + (naturalGasPrices(i) * naturalGasReq +...
        elecPrices(i) * elecReq) ./ ammoniaProduced);
end
prices = ammoniaPrices';
writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia MP', 'Range', 'H2')