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
elecPrices = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Grid electricity prices', 'Range', 'B2:J48')/1000;
PPP = readmatrix('Prices regionalization.xlsx', 'Sheet', 'PPP', 'Range', 'B14:J17');
PPP = PPP./PPP(:,9); % equalize with respect to Europe

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

ammoniaPriceWithoutNGElec = ammoniaPrice - (naturalGasReq * naturalGasPrice + elecReq * elecPrice) / ammoniaProduced; % USD2019 per ton
ammoniaPriceWithoutNGElec = [ammoniaPriceWithoutNGElec ammoniaPriceWithoutNGElec*a...
    ammoniaPriceWithoutNGElec*b ammoniaPriceWithoutNGElec*c]; 
ammoniaPriceWithoutNGElec = ammoniaPriceWithoutNGElec' .* PPP;
ammoniaPricesWithoutElec = zeros(length(naturalGasPrices), length(PPP'));
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
    ammoniaPricesWithoutElec(i, :) = (ammoniaPriceWithoutNGElec(j, :) + (naturalGasPrices(i) * naturalGasReq) ./ ammoniaProduced);
end

% ammoniaPricesWithoutElec = ammoniaPricesWithoutElec';
ammoniaPrices = ammoniaPricesWithoutElec + (elecPrices .* elecReq) ./ ammoniaProduced;

prices = ammoniaPrices;
writematrix(prices, 'Prices regionalization.xlsx', 'Sheet', 'BAU ammonia', 'Range', 'C2')

% Green process
fileName = 'Ammonia/Green ammonia - 2019.xlsx';

gAmmoniaPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C26:C26') * 1000; % USD2019 per ton
gAmmoniaProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C25:C25') / 1000; % amount of ammonia produced in ton/hr
hydrogenPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E6:E6'); % in ton/hr
hydrogenReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D6:D6'); % in ton/hr
elecReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D12:D12'); % in kWh/hr

gAmmoniaPartial = gAmmoniaPrice - (hydrogenReq * hydrogenPrice + elecReq * elecPrice) / gAmmoniaProduced; % USD2019 per ton
gAmmoniaPartial = [gAmmoniaPartial gAmmoniaPartial*a...
    gAmmoniaPartial*b gAmmoniaPartial*c];
gAmmoniaPartial = gAmmoniaPartial' .* PPP;
gAmmoniaPriceWithoutHElec = zeros(length(naturalGasPrices), length(PPP'));
% green ammonia from grid electricity
for i = 1:length(elecPrices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    elseif i > 24 && i <= 36
        j = 3;
    else
        j = 4;
    end
    gAmmoniaPriceWithoutHElec(i, :) = gAmmoniaPartial(j, :);
end

gAmmoniaPriceWithoutH = gAmmoniaPriceWithoutHElec + (elecPrices .* elecReq)./gAmmoniaProduced;

WindLCOH2019 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Wind LCOH countries', 'Range', 'D3:D10')'*1000; 
WindLCOH2020 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Wind LCOH countries', 'Range', 'G3:G10')'*1000; 
WindLCOH2021 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Wind LCOH countries', 'Range', 'J3:J10')'*1000; 
WindLCOH2022 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Wind LCOH countries', 'Range', 'K3:K10')'*1000; 

SolarLCOH2019 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Solar LCOH countries', 'Range', 'D3:D9')'*1000; 
SolarLCOH2020 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Solar LCOH countries', 'Range', 'G3:G9')'*1000; 
SolarLCOH2021 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Solar LCOH countries', 'Range', 'J3:J9')'*1000; 
SolarLCOH2022 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Solar LCOH countries', 'Range', 'K3:K9')'*1000; 

windLCOH = zeros(length(elecPrices), length(elecPrices(1, :))-1);
solarLCOH = zeros(length(elecPrices), length(elecPrices(1, :))-2);

for i = 1:length(elecPrices)
    if i > 0 && i <= 12
        windLCOH(i,:) = WindLCOH2019;
        solarLCOH(i,:) = SolarLCOH2019;
    elseif i > 12 && i <= 24
        windLCOH(i,:) = WindLCOH2020;
        solarLCOH(i,:) = SolarLCOH2020;
    elseif i > 24 && i <= 36
        windLCOH(i,:) = WindLCOH2021;
        solarLCOH(i,:) = SolarLCOH2021;
    else
        windLCOH(i,:) = WindLCOH2022;
        solarLCOH(i,:) = SolarLCOH2022;
    end
end

gAmmoniaPriceWithoutHWind = gAmmoniaPriceWithoutH(:, [1 2 3 4 5 6 7 9]);
gAmmoniaPriceWithoutHSolar = gAmmoniaPriceWithoutH(:, [2 3 5 6 7 8 9]);
gWindAmmoniaPrices = gAmmoniaPriceWithoutHWind + windLCOH .* hydrogenReq ./ gAmmoniaProduced;
gSolarAmmoniaPrices = gAmmoniaPriceWithoutHSolar + solarLCOH .* hydrogenReq ./ gAmmoniaProduced;

writematrix(gWindAmmoniaPrices, 'Prices regionalization.xlsx', 'Sheet', 'Wind ammonia', 'Range', 'C2')
writematrix(gSolarAmmoniaPrices, 'Prices regionalization.xlsx', 'Sheet', 'Solar ammonia', 'Range', 'C2')


%% Methanol sensitivity

% BAU process (data from Plant to Planet Methanol)
naturalGasReq = (0.6518*36.6 + 6.93)/47.1; % ton NG per ton methanol
elecReq = 0.074*1000; % kWh per ton methanol
methanolPriceWithoutNGElec = 84.8*CEPCI2019/CEPCI2015; % in USD2019 per ton methanol
methanolPriceWithoutNGElec = [methanolPriceWithoutNGElec methanolPriceWithoutNGElec*a...
    methanolPriceWithoutNGElec*b methanolPriceWithoutNGElec*c]; % in USD2022 per ton
methanolPriceWithoutNGElec = methanolPriceWithoutNGElec' .* PPP;
methanolPricesWithoutElec = zeros(length(naturalGasPrices), length(PPP'));
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
    methanolPricesWithoutElec(i, :) = methanolPriceWithoutNGElec(j, :) + naturalGasPrices(i) * naturalGasReq; 
end

% methanolPricesWithoutElec = methanolPricesWithoutElec';
methanolPrices = methanolPricesWithoutElec + (elecPrices .* elecReq);

prices = methanolPrices;
writematrix(prices, 'Prices regionalization.xlsx', 'Sheet', 'BAU methanol', 'Range', 'C2')

% DAC process (data from Daniel et al. 2021)
gMethanolPrice = 1380; % USD2015 per ton
CO2Req = 1.45; % ton carbon dioxide per ton methanol
H2Req = 0.19; % ton hydrogen per ton methanol
CO2Price = 160; % USD2015 per ton
H2Price = 5240; % USD2015 per ton
elecReq = 0.3*1000; % kWh per ton methanol
elecPrice = 104.61/1000; % USD2015 per kWh
gMethanolPartial = gMethanolPrice - CO2Req * CO2Price - H2Price * H2Req - elecReq * elecPrice;
gMethanolPartial = gMethanolPartial * CEPCI2019 / CEPCI2015;
gMethanolPartial = [gMethanolPartial gMethanolPartial*a...
    gMethanolPartial*b gMethanolPartial*c];
gMethanolPartial = gMethanolPartial' .* PPP;

CO2DACt = 164.2;
CO2DAC = [CO2DACt CO2DACt*a CO2DACt*b CO2DACt*c];
NGLHV1 = 13.1; % in MWh per ton
NGLHV2 = 36.6 / 3600; % in MWh per m3
NGDensity = NGLHV2 / NGLHV1; % ton per m3
NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * CO2Req; % ton NG per ton methanol
NGPriceDAC = 3.5 * 47.1 * CEPCI2019 / CEPCI2018; % refer Keith 2018
NGPriceDAC = [NGPriceDAC NGPriceDAC*a NGPriceDAC*b NGPriceDAC*c];

gMethanolPriceWithoutHElec = zeros(length(naturalGasPrices), length(PPP'));
% green ammonia from grid electricity
for i = 1:length(elecPrices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    elseif i > 24 && i <= 36
        j = 3;
    else
        j = 4;
    end
    gMethanolPriceWithoutHElec(i, :) = gMethanolPartial(j, :) + CO2Req*CO2DAC(j) + NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
end


gMethanolPriceWithoutH = gMethanolPriceWithoutHElec + (elecPrices .* elecReq);

gMethanolPriceWithoutHWind = gMethanolPriceWithoutH(:, [1 2 3 4 5 6 7 9]);
gMethanolPriceWithoutHSolar = gMethanolPriceWithoutH(:, [2 3 5 6 7 8 9]);
gWindMethanolPrices = gMethanolPriceWithoutHWind + windLCOH .* H2Req;
gSolarMehtanolPrices = gMethanolPriceWithoutHSolar + solarLCOH .* H2Req;

writematrix(gWindMethanolPrices, 'Prices regionalization.xlsx', 'Sheet', 'Wind methanol', 'Range', 'C2')
writematrix(gSolarMehtanolPrices, 'Prices regionalization.xlsx', 'Sheet', 'Solar methanol', 'Range', 'C2')