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

naturalGasPrices = 0:10:4000;
elecPrices = 0:10:500;
elecPrices = elecPrices/1000;

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

ammoniaPriceWithoutNG = ammoniaPrice - (naturalGasReq * naturalGasPrice + elecReq * elecPrice) / ammoniaProduced; % USD2019 per ton
ammoniaPriceWithoutNG = ammoniaPriceWithoutNG*c; 

prices = [];
for i = 1:length(naturalGasPrices)
    for j = 1:length(elecPrices)
        prices(end + 1, :) = [naturalGasPrices(i) elecPrices(j)];
    end
end
prices(:,3) = (ammoniaPriceWithoutNG + (prices(:,1).* naturalGasReq +...
    prices(:,2) * elecReq) ./ ammoniaProduced);

% % Green process
% fileName = 'Ammonia/Green ammonia - 2019.xlsx';
% 
% gAmmoniaPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C26:C26') * 1000; % USD2019 per ton
% gAmmoniaProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C25:C25') / 1000; % amount of ammonia produced in ton/hr
% hydrogenPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E6:E6'); % in ton/hr
% hydrogenReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D6:D6'); % in ton/hr
% elecReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D12:D12'); % in kWh/hr
% 
% gAmmoniaPartial = gAmmoniaPrice - (hydrogenReq * hydrogenPrice + elecReq * elecPrice) / gAmmoniaProduced; % USD2019 per ton
% gAmmoniaPartial = gAmmoniaPartial*c;
% 
% gAmmoniaPriceWithoutH = gAmmoniaPartial + (elecPrices * elecReq)/gAmmoniaProduced;
% 
% windLCOHFuture = readmatrix('Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'B2:B4')'*1000; 
% solarLCOHFuture = readmatrix('Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'C2:C4')'*1000; 
% 
% gWindAmmoniaPrices = gAmmoniaPriceWithoutH + windLCOHFuture.*hydrogenReq/ gAmmoniaProduced;
% gSolarAmmoniaPrices = gAmmoniaPriceWithoutH + solarLCOHFuture.*hydrogenReq/gAmmoniaProduced;

%% Methanol sensitivity
% BAU process (data from Plant to Planet Methanol)
naturalGasReq = (0.6518*36.6 + 6.93)/47.1; % ton NG per ton methanol
elecReq = 0.074*1000; % kWh per ton methanol
methanolPriceWithoutNG = 84.8*CEPCI2019/CEPCI2015; % in USD2019 per ton methanol
methanolPriceWithoutNG = methanolPriceWithoutNG*c; % in USD2022 per ton

prices(:,4) = methanolPriceWithoutNG + prices(:,1) .* naturalGasReq + prices(:,2) .* elecReq; 
writematrix(prices, 'Prices sensitivity future.xlsx', 'Sheet', 'random', 'Range', 'A2')

% % DAC process (data from Daniel et al. 2021)
% gMethanolPrice = 1380; % USD2015 per ton
% CO2Req = 1.45; % ton carbon dioxide per ton methanol
% H2Req = 0.19; % ton hydrogen per ton methanol
% CO2Price = 160; % USD2015 per ton
% H2Price = 5240; % USD2015 per ton
% elecReq = 0.3*1000; % kWh per ton methanol
% elecPrice = 104.61/1000; % USD2015 per kWh
% gMethanolPartial = gMethanolPrice - CO2Req * CO2Price - H2Price * H2Req - elecReq * elecPrice;
% gMethanolPartial = gMethanolPartial * CEPCI2019 / CEPCI2015;
% gMethanolPartial = gMethanolPartial*c;
% 
% CO2DAC = readmatrix('Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'D2:D4')'*1000;
% gMethanolPriceWithoutHElec = gMethanolPartial + CO2Req .* CO2DAC;
% gMethanolPriceWithoutH = gMethanolPriceWithoutHElec + (elecPrices * elecReq);
% gWindMethanolPrices = gMethanolPriceWithoutH + windLCOHFuture .* H2Req;
% gSolarMehtanolPrices = gMethanolPriceWithoutH + solarLCOHFuture .* H2Req;

% writematrix(naturalGasPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'BAU', 'Range', 'A2')
% writematrix(ammoniaPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'BAU', 'Range', 'B2')
% writematrix(methanolPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'BAU', 'Range', 'C2')

% writematrix(gWindAmmoniaPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'E2')
% writematrix(gSolarAmmoniaPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'F2')
% writematrix(gWindMethanolPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'G2')
% writematrix(gSolarMehtanolPrices', 'Prices sensitivity future.xlsx', 'Sheet', 'Green', 'Range', 'H2')