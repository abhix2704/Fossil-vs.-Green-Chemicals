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


prices = ammoniaPrices;
writematrix(prices', 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'E2')

% Green process
fileName = 'Ammonia/Green ammonia - 2019.xlsx';

gAmmoniaPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C26:C26') * 1000; % USD2019 per ton
gAmmoniaProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C25:C25') / 1000; % amount of ammonia produced in ton/hr
hydrogenPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E6:E6'); % in ton/hr
hydrogenReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D6:D6'); % in ton/hr
elecReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D12:D12'); % in kWh/hr

gAmmoniaPriceWithoutH = gAmmoniaPrice - (hydrogenReq * hydrogenPrice + elecReq * elecPrice) / gAmmoniaProduced; % USD2019 per ton
gAmmoniaPriceWithoutH = [gAmmoniaPriceWithoutH gAmmoniaPriceWithoutH*a...
    gAmmoniaPriceWithoutH*b gAmmoniaPriceWithoutH*c];

% Green hydrogen prices from Parkinson 2019
HBiomassCCS =  readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'LCOH', 'Range', 'B20:Q20');
HWind = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'LCOH', 'Range', 'B17:Q17');
HSolar = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'LCOH', 'Range', 'B18:Q18');  
HNuclear = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'LCOH', 'Range', 'B19:Q19');

j = 1;
for i = 2:length(HBiomassCCS)
    if mod(i,2) == 0 && mod(i,4) ~= 0
        HBiomassCCSAvg(j) = HBiomassCCS(i-1)*1000;
        HBiomassCCSLow(j) = HBiomassCCS(i)*1000;
        HBiomassCCSHigh(j) = HBiomassCCS(i+1)*1000;
        HWindAvg(j) = HWind(i-1)*1000;
        HWindLow(j) = HWind(i)*1000;
        HWindHigh(j) = HWind(i+1)*1000;
        HSolarAvg(j) = HSolar(i-1)*1000;
        HSolarLow(j) = HSolar(i)*1000;
        HSolarHigh(j) = HSolar(i+1)*1000;
        HNuclearAvg(j) = HNuclear(i-1)*1000;
        HNuclearLow(j) = HNuclear(i)*1000;
        HNuclearHigh(j) = HNuclear(i+1)*1000;
        j = j + 1;
    end
end

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
    gAmmoniaBiomassCCS(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HBiomassCCSAvg(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;

    gAmmoniaWind(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HWindAvg(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    gAmmoniaWindLow(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HWindLow(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    gAmmoniaWindHigh(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HWindHigh(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    
    gAmmoniaSolar(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HSolarAvg(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    gAmmoniaSolarLow(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HSolarLow(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    gAmmoniaSolarHigh(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HSolarHigh(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    
    gAmmoniaNuclear(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HNuclearAvg(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    gAmmoniaNuclearLow(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HNuclearLow(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
    gAmmoniaNuclearHigh(i) = gAmmoniaPriceWithoutH(j)+(hydrogenReq*HNuclearHigh(j)+...
        elecReq*elecPrices(i))/gAmmoniaProduced;
end
prices = [gAmmoniaBiomassCCS' gAmmoniaWind' gAmmoniaSolar' gAmmoniaNuclear'];
pricesSe = [gAmmoniaWindLow'...
    gAmmoniaWindHigh' gAmmoniaSolarLow' gAmmoniaSolarHigh' gAmmoniaNuclearLow' gAmmoniaNuclearHigh'];
writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'F2')
writematrix(pricesSe, 'Prices Sensitivity 2.xlsx', 'Sheet', 'Ammonia high low', 'Range', 'E2')

% hydrogen from SMR-CCS (from G. Collodi et al. 2017)
specificH2 = 11.94; % Nm3/kg of hydrogen
LCOH = 16.5 * specificH2 / 100 * 1.1304; % in USD2017 per kg
NGReq = 15.614 * 11.94; % MJ/kg of hydrogen
NGReqKg = NGReq/47.1; % kg NG/kg of hydrogen
LCOHWithoutNG = LCOH - NGReq/1000*6*1.1304; % in USD2017 per kg
LCOHWithoutNG = LCOHWithoutNG * CEPCI2019 / CEPCI2017;
LCOHWithoutNG = [LCOHWithoutNG LCOHWithoutNG*a LCOHWithoutNG*b LCOHWithoutNG*c];
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
    H2SMRCCS(i) = LCOHWithoutNG(j)*1000 + NGReqKg*naturalGasPrices(i);
    gSMRCCS(i) = gAmmoniaPriceWithoutH(j) + (hydrogenReq*H2SMRCCS(i) +...
        elecReq*elecPrices(i))/gAmmoniaProduced;
end
writematrix(H2SMRCCS', 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'T2')
writematrix(gSMRCCS', 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'U2')

%% Methanol sensitivity

% BAU process (data from Plant to Planet Methanol)
naturalGasReq = (0.6518*36.6 + 6.93)/47.1; % ton NG per ton methanol
elecReq = 0.074*1000; % kWh per ton methanol
methanolPriceWithoutNG = 84.8*CEPCI2019/CEPCI2015; % in USD2019 per ton methanol
methanolPriceWithoutNG = [methanolPriceWithoutNG methanolPriceWithoutNG*a...
    methanolPriceWithoutNG*b methanolPriceWithoutNG*c]; % in USD2022 per ton
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
    methanolPrices(i) = (methanolPriceWithoutNG(j) + naturalGasPrices(i) * naturalGasReq + elecPrices(i) * elecReq)'; 
end

prices = methanolPrices';
writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol', 'Range', 'E2')


% DAC process (data from Daniel et al. 2021)
gMethanolPrice = 1380; % USD2015 per ton
CO2Req = 1.45; % ton carbon dioxide per ton methanol
H2Req = 0.19; % ton hydrogen per ton methanol
CO2Price = 160; % USD2015 per ton
H2Price = 5240; % USD2015 per ton
elecReq = 0.3*1000; % kWh per ton methanol
elecPrice = 104.61/1000; % USD2015 per kWh
gMethanolWithoutHydrogenAndCO2 = gMethanolPrice - CO2Req * CO2Price - H2Price * H2Req - elecReq * elecPrice;
gMethanolWithoutHydrogenAndCO2 = gMethanolWithoutHydrogenAndCO2 * CEPCI2019 / CEPCI2015;
gMethanolWithoutHydrogenAndCO2 = [gMethanolWithoutHydrogenAndCO2 gMethanolWithoutHydrogenAndCO2*a...
    gMethanolWithoutHydrogenAndCO2*b gMethanolWithoutHydrogenAndCO2*c];
CO2DACt = 164.2;
CO2DAC = [CO2DACt CO2DACt*a CO2DACt*b CO2DACt*c];
CO2DACLowt = 94.7;
CO2DACLow = [CO2DACLowt CO2DACLowt*a CO2DACLowt*b CO2DACLowt*c];
CO2DACHight = 233.7;
CO2DACHigh = [CO2DACHight CO2DACHight*a CO2DACHight*b CO2DACHight*c];

NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * CO2Req; % ton NG per ton methanol
NGPriceDAC = 3.5 * 47.1 * CEPCI2019 / CEPCI2018; % refer Keith 2018
NGPriceDAC = [NGPriceDAC NGPriceDAC*a NGPriceDAC*b NGPriceDAC*c];

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
    CPrices(i) = CO2Req*CO2DAC(j) + NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    CPricesLow(i) = CO2Req*CO2DACLow(j) + NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    CPricesHigh(i) = CO2Req*CO2DACHigh(j) + NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));

    gMethanolWind(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HWindAvg(j) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    gMethanolWindLow(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HWindLow(j) + CO2Req*CO2DACLow(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    gMethanolWindHigh(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HWindHigh(j) + CO2Req*CO2DACHigh(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
   
    gMethanolSolar(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HSolarAvg(j) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    gMethanolSolarLow(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HSolarLow(j) + CO2Req*CO2DACLow(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    gMethanolSolarHigh(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HSolarHigh(j) + CO2Req*CO2DACHigh(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    
    gMethanolNuclear(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HNuclearAvg(j) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    gMethanolNuclearLow(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HNuclearLow(j) + CO2Req*CO2DACLow(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
    gMethanolNuclearHigh(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*HNuclearHigh(j) + CO2Req*CO2DACHigh(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));

    gMethanolSMRCCS(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
        (H2Req*H2SMRCCS(i) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
        NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
end

biomassReq = 1.74; % ton straw per ton methanol
elecReq = (0.0857 + 0.00489 + 0.0099) * 1000; % kWh per ton methanol
biomassPrice = 336 - elecReq * 0.75/6.8;
gMethanolBiomassCCS(1:12) = biomassPrice * CEPCI2019/CEPCI2018;
gMethanolBiomassCCS(13:24) = biomassPrice * CEPCI2020/CEPCI2018;
gMethanolBiomassCCS(25:36) = biomassPrice * CEPCI2021/CEPCI2018;
gMethanolBiomassCCS(37:length(gMethanolNuclear)) = biomassPrice * CEPCI2022/CEPCI2018;
gMethanolBiomassCCS = gMethanolBiomassCCS' + elecPrices .* elecReq;

gMethanolPrice = [gMethanolBiomassCCS gMethanolWind'...
    gMethanolSolar' gMethanolNuclear'];
gMethanolPricesSe = [gMethanolWindLow' gMethanolWindHigh' gMethanolSolarLow' gMethanolSolarHigh'...
    gMethanolNuclearLow' gMethanolNuclearHigh'];

writematrix(gMethanolPrice, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol', 'Range', 'F2')
writematrix(gMethanolPricesSe, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol high low', 'Range', 'E2')
writematrix(gMethanolSMRCCS', 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol', 'Range', 'S2')
writematrix(CPrices', 'Prices sensitivity 2.xlsx', 'Sheet', 'DAC', 'Range', 'B2')
writematrix(CPricesLow', 'Prices sensitivity 2.xlsx', 'Sheet', 'DAC', 'Range', 'C2')
writematrix(CPricesHigh', 'Prices sensitivity 2.xlsx', 'Sheet', 'DAC', 'Range', 'D2')

% %% Hydrogen calculations
% 
% writematrix(H2SMRCCS', 'Prices sensitivity 2.xlsx', 'Sheet', 'Hydrogen', 'Range', 'D2')
% j = 1;
% for i = 1:length(naturalGasPrices)
%     if i > 0 && i <= 12
%         j = 1;
%     elseif i > 12 && i <= 24
%         j = 2;
%     elseif i > 24 && i <= 36
%         j = 3;
%     else
%         j = 4;
%     end
%     H2WindPrices(i) = HWindAvg(j);
%     H2WindPricesLow(i) = HWindLow(j);
%     H2WindPricesHigh(i) = HWindHigh(j);
% 
%     H2SolarPrices(i) = HSolarAvg(j);
%     H2SolarPricesLow(i) = HSolarLow(j);
%     H2SolarPricesHigh(i) = HSolarHigh(j);
% 
%     H2NuclearPrices(i) = HNuclearAvg(j);
%     H2NuclearPricesLow(i) = HNuclearLow(j);
%     H2NuclearPricesHigh(i) = HNuclearHigh(j);
% 
%     H2BiomassPrices(i) = HBiomassCCSAvg(j);
% end
% prices = [H2WindPrices' H2SolarPrices' H2NuclearPrices' H2BiomassPrices'];
% pricesSe = [H2WindPricesLow' H2WindPricesHigh' H2SolarPricesLow' H2SolarPricesHigh'...
%     H2NuclearPricesLow' H2NuclearPricesHigh'];
% 
% writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Hydrogen', 'Range', 'E2')
% writematrix(pricesSe, 'Prices sensitivity 2.xlsx', 'Sheet', 'Hydrogen high low', 'Range', 'E2')


