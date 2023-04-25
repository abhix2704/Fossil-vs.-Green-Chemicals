clear 
close all
clc

%% CEPCI indexes
CEPCI2008 = 575.4;
CEPCI2012 = 584.6;
CEPCI2015 = 556.8;
CEPCI2018 = 603.1;
CEPCI2019 = 607.5;
CEPCI2021 = 776.3;
CEPCI2022 = 803.6;


naturalGasPrices = 0:50:5000;
coalPrices = 0:50:5000;

NGLHV1 = 13.1; % in MWh per ton
NGLHV2 = 36.6 / 3600; % in MWh per m3
NGDensity = NGLHV2 / NGLHV1; % ton per m3

%% Ammonia sensitivity

% BAU process
fileName = 'Ammonia/BAU - 2019.xlsx';

ammoniaPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C24:C24') * 1000; % USD2019 per ton
naturalGasReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D5:D5'); % in ton/hr
naturalGasReq = naturalGasReq + readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D15:D15'); % in ton/hr
naturalGasPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E5:E5') * CEPCI2019 / CEPCI2018; % in USD2019 per ton
ammoniaProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C23:C23') / 1000; % amount of ammonia produced in ton/hr
hydrogenProduced = 12.34; % ton per hour
hydrogenPrice = 1370; % USD2019 per ton

hydrogenWithoutNG = hydrogenPrice - (naturalGasReq * naturalGasPrice) / hydrogenProduced;
hydrogenWithoutNG = hydrogenWithoutNG * CEPCI2022 / CEPCI2019; % USD2022 per ton

ammoniaPriceWithoutNG = ammoniaPrice - (naturalGasReq * naturalGasPrice) / ammoniaProduced; % USD2019 per ton
ammoniaPriceWithoutNG = ammoniaPriceWithoutNG * CEPCI2022 / CEPCI2019; % USD2022 per ton

hydrogenPrices = (hydrogenWithoutNG + naturalGasPrices .* naturalGasReq ./ hydrogenProduced)';
ammoniaPrices = (ammoniaPriceWithoutNG + naturalGasPrices .* naturalGasReq ./ ammoniaProduced)';
prices = [naturalGasPrices' ammoniaPrices];

writematrix(prices, 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia', 'Range', 'A2')
writematrix(hydrogenPrices, 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia', 'Range', 'P2')

% Green process
fileName = 'Ammonia/Green ammonia - 2019.xlsx';

gAmmoniaPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C26:C26') * 1000; % USD2019 per ton
gAmmoniaProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C25:C25') / 1000; % amount of ammonia produced in ton/hr
hydrogenPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E6:E6'); % in ton/hr
hydrogenReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D6:D6'); % in ton/hr

gAmmoniaPriceWithoutH = gAmmoniaPrice - (hydrogenReq * hydrogenPrice) / gAmmoniaProduced; % USD2019 per ton
gAmmoniaPriceWithoutH = gAmmoniaPriceWithoutH * CEPCI2022 / CEPCI2019;

% Green hydrogen prices from Parkinson 2019
HBiomassCCS = 2270 * CEPCI2022 / CEPCI2019;
HWind = 5240 * CEPCI2022 / CEPCI2019;
HWindSe = [3560 10820] * CEPCI2022 / CEPCI2019;
HSolar = 8870 * CEPCI2022 / CEPCI2019;  
HSolarSe = [3340 17300] * CEPCI2022 / CEPCI2019;
HNuclear = 4630 * CEPCI2022 / CEPCI2019;
HNuclearSe = [3290 6010] * CEPCI2022 / CEPCI2019;

gAmmoniaBiomass = gAmmoniaPriceWithoutH + hydrogenReq * HBiomassCCS / gAmmoniaProduced;
gAmmoniaWind = gAmmoniaPriceWithoutH + hydrogenReq * HWind / gAmmoniaProduced;
gAmmoniaSolar = gAmmoniaPriceWithoutH + hydrogenReq * HSolar / gAmmoniaProduced;
gAmmoniaNuclear = gAmmoniaPriceWithoutH + hydrogenReq * HNuclear / gAmmoniaProduced;
prices = [gAmmoniaBiomass gAmmoniaWind gAmmoniaSolar gAmmoniaNuclear];
H2Prices = [HBiomassCCS HWind HSolar HNuclear];
% prices = gAmmoniaWind;

writematrix(prices, 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia', 'Range', 'C2')
writematrix(H2Prices, 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia', 'Range', 'Q2')

% Green hydrogen high low values

gAmmoniaWindSe = gAmmoniaPriceWithoutH + hydrogenReq .* HWindSe ./ gAmmoniaProduced;
gAmmoniaSolarSe = gAmmoniaPriceWithoutH + hydrogenReq .* HSolarSe ./ gAmmoniaProduced;
gAmmoniaNuclearSe = gAmmoniaPriceWithoutH + hydrogenReq .* HNuclearSe ./ gAmmoniaProduced;
pricesSe = [gAmmoniaWindSe gAmmoniaSolarSe gAmmoniaNuclearSe];
H2PricesSe = [HWindSe HSolarSe HNuclearSe];

writematrix(pricesSe, 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia high low', 'Range', 'C2')
writematrix(H2PricesSe, 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia high low', 'Range', 'S2')

% Coal process (refer Y. Wang et al. 2019)
H2StdVolume = 11.126; % Nm3 per kg
CNY2USD = 0.14; % conversion of CNY to USD
cH2Price = 0.75 * H2StdVolume * CNY2USD * 1000; % USD2019 per ton
cH2Price = cH2Price * CEPCI2022 / CEPCI2019; % USD2022 per ton
coalPrice = 700 * CNY2USD; % USD2019 per ton
coalPrice = coalPrice * CEPCI2022 / CEPCI2019; % USD2022 per ton
coalReq = 6.43; % ton coal per ton hydrogen
cH2PriceWithoutCoal = cH2Price - coalPrice * coalReq; % USD2022 per ton

cH2Prices = cH2PriceWithoutCoal + coalPrices .* coalReq; % USD2022 per ton
cAmmoniaPrices = gAmmoniaPriceWithoutH + hydrogenReq .* cH2Prices ./ gAmmoniaProduced;

writematrix(cAmmoniaPrices', 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia', 'Range', 'K2')
writematrix(cH2Prices', 'Prices sensitivity.xlsx', 'Sheet', 'Ammonia', 'Range', 'U2')

%% Methanol sensitivity

% BAU process (data from Iasonas et al. 2019 and SimaPro inventory)
naturalGasReq = 33 / 47.1; % ton NG per ton methanol
naturalGasPrice = 3.9 * 47.1; % in USD2019 per ton NG
methanolPrice = 328.8; % in USD2019 per ton methanol
methanolPriceWithoutNG = methanolPrice - (naturalGasPrice * naturalGasReq); % in USD2019 per ton
methnaolPriceWithoutNG = methanolPriceWithoutNG * CEPCI2022 / CEPCI2019; % in USD2022 per ton

methanolPrices = (methanolPriceWithoutNG + naturalGasPrices .* naturalGasReq)'; 
prices = [naturalGasPrices' methanolPrices];
writematrix(prices, 'Prices sensitivity.xlsx', 'Sheet', 'Methanol', 'Range', 'A2')

% DAC process (data from Daniel et al. 2021)
gMethanolPrice = 1390; % USD2018 per ton
CO2Req = 1.5; % ton carbon dioxide per ton methanol
H2Req = 0.192; % ton hydrogen per ton methanol
CO2Price = 95.5; % USD2018 per ton
H2Price = 5240 * 1.1597 * CEPCI2018 / CEPCI2015; % USD2018 per ton
gMethanolWithoutHydrogenAndCO2 = gMethanolPrice - CO2Req * CO2Price - H2Price * H2Req;
gMethanolWithoutHydrogenAndCO2 = gMethanolWithoutHydrogenAndCO2 * CEPCI2022 / CEPCI2018;
CO2DAC = 164.2 * CEPCI2022 / CEPCI2019;
CO2DACSe = [94.7 233.7] * CEPCI2022 / CEPCI2019;
gMethanolWindPrice = gMethanolWithoutHydrogenAndCO2 + (CO2Req * CO2DAC + H2Req * HWind);
gMethanolSolarPrice = gMethanolWithoutHydrogenAndCO2 + (CO2Req * CO2DAC + H2Req * HSolar);
gMethanolNuclearPrice = gMethanolWithoutHydrogenAndCO2 + (CO2Req * CO2DAC + H2Req * HNuclear);

NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * CO2Req; % ton NG per ton methanol
NGPriceDAC = 3.5 * 47.1 * CEPCI2022 / CEPCI2018; % refer Keith 2018

gMethanolPrice = [gMethanolWindPrice gMethanolSolarPrice gMethanolNuclearPrice];
gMethanolPriceWithoutNG = gMethanolPrice - (NGReqCarbonDioxide * NGPriceDAC); % USD2022 per ton
gMethanolPrices = (gMethanolPriceWithoutNG' + NGReqCarbonDioxide .* naturalGasPrices)'; % with NG required for carbon dioxide
writematrix(gMethanolPrices, 'Prices sensitivity.xlsx', 'Sheet', 'Methanol', 'Range', 'C2')

% Green methanol low high prices
gMethanolWindSe = gMethanolWithoutHydrogenAndCO2 + (CO2Req * CO2DACSe + H2Req * HWindSe);
gMethanolSolarSe = gMethanolWithoutHydrogenAndCO2 + (CO2Req * CO2DACSe + H2Req * HSolarSe);
gMethanolNuclearSe = gMethanolWithoutHydrogenAndCO2 + (CO2Req * CO2DACSe + H2Req * HNuclearSe);
gMethanolPrices = [gMethanolWindSe gMethanolSolarSe gMethanolNuclearSe];
gMethanolPricesWithoutNG = gMethanolPrices - (NGReqCarbonDioxide * NGPriceDAC); % USD2022 per ton
gMethanolPrices = (gMethanolPricesWithoutNG' + NGReqCarbonDioxide .* naturalGasPrices)'; % with NG required for carbon dioxide
writematrix(gMethanolPrices, 'Prices sensitivity.xlsx', 'Sheet', 'Methanol high low', 'Range', 'C2')

% Coal process (refer D. Zhang et al. 2020)
coalReq = 215/112.71; % ton coal per ton methanol
coalPrice = 88.6; % USD2012 per ton
cMethanolPrice = 272.6; % USD2012 per ton
cMethanolPriceWithoutCoal = cMethanolPrice - coalPrice * coalReq;
cMethanolPriceWithoutCoal = cMethanolPriceWithoutCoal * CEPCI2022 / CEPCI2012;

cMethanolPrices = cMethanolPriceWithoutCoal + coalPrices .* coalReq;
writematrix(cMethanolPrices', 'Prices sensitivity.xlsx', 'Sheet', 'Methanol', 'Range', 'I2')


%% Propanol sensitivity

writematrix(naturalGasPrices', 'Prices sensitivity.xlsx', 'Sheet', 'Propanol', 'Range', 'A2')

% BAU process
fileName = 'Propanol/BAU - 2022.xlsx';

propanolPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C24:C24') * 1000; % USD2022 per ton
naturalGasReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D5:D5'); % in ton/hr
naturalGasPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E5:E5') * CEPCI2022 / CEPCI2021; % in USD2022 per ton
propanolProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C23:C23') / 1000; % amount of propanol produced in ton/hr

propanolPriceWithoutNG = propanolPrice - (naturalGasReq * naturalGasPrice) / propanolProduced; % USD2022 per ton
propanolPrices = (propanolPriceWithoutNG + naturalGasPrices .* naturalGasReq ./ propanolProduced)';

writematrix(propanolPrices, 'Prices sensitivity.xlsx', 'Sheet', 'Propanol', 'Range', 'B2')


% Green process
% Common variables
fileName = 'Propanol/NG + wind + BAU ethylene - 2022.xlsx';

naturalGasReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D12:D12'); % in ton/hr
naturalGasPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E12:E12') * CEPCI2022 / CEPCI2021; % in USD2022 per ton
carbonDioxideReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D5:D5'); % in ton/hr
hydrogenReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D6:D6'); % in ton/hr)
hydrogenPrice = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'E6:E6'); % in ton/hr)
hydrogenPrice = hydrogenPrice * CEPCI2022 / CEPCI2019;
ethyleneReq = readmatrix(fileName, 'Sheet', 'OPEX', 'Range', 'D7:D7'); % in ton/hr
gPropanolProduced = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C23:C23') / 1000; % amount of propanol produced in ton/hr

% DAC, wind, BAU ethylene
fileName = 'Propanol/DAC + wind + BAU ethylene - 2022.xlsx';

gPropanolPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C24:C24') * 1000; % USD2022 per ton

NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * carbonDioxideReq; % ton NG per hr
NGPriceDAC = 3.5 * 47.1 * CEPCI2022 / CEPCI2018; % refer Keith 2018

gPropanolPriceWithoutNGAndH = gPropanolPrice - (naturalGasReq * naturalGasPrice + ...
    NGReqCarbonDioxide * NGPriceDAC + hydrogenReq * hydrogenPrice) / gPropanolProduced; % USD2022 per ton
gPropanolWindPrices = (gPropanolPriceWithoutNGAndH + ((naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices + hydrogenReq * HWind) ./ gPropanolProduced)'; % with NG required for cabron dioxide
gPropanolSolarPrices = (gPropanolPriceWithoutNGAndH + ((naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices + hydrogenReq * HSolar) ./ gPropanolProduced)'; % with NG required for cabron dioxide
gPropanolNuclearPrices = (gPropanolPriceWithoutNGAndH + ((naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices + hydrogenReq * HNuclear) ./ gPropanolProduced)'; % with NG required for cabron dioxide
gPropanolPrices = [gPropanolWindPrices gPropanolSolarPrices gPropanolNuclearPrices];
writematrix(gPropanolPrices, 'Prices sensitivity.xlsx', 'Sheet', 'Propanol', 'Range', 'C2')

gPropanolWindPricesSe = (gPropanolPriceWithoutNGAndH' + (naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices ./ gPropanolProduced)' + hydrogenReq * HWindSe / gPropanolProduced; % with NG required for cabron dioxide
gPropanolSolarPricesSe = (gPropanolPriceWithoutNGAndH' + (naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices ./ gPropanolProduced)' + hydrogenReq * HSolarSe / gPropanolProduced; % with NG required for cabron dioxide
gPropanolNuclearPricesSe = (gPropanolPriceWithoutNGAndH' + (naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices ./ gPropanolProduced)' + hydrogenReq * HNuclearSe / gPropanolProduced; % with NG required for cabron dioxide
gPropanolPricesSe = [gPropanolWindPricesSe gPropanolSolarPricesSe gPropanolNuclearPricesSe];
writematrix(gPropanolPricesSe, 'Prices sensitivity.xlsx', 'Sheet', 'Propanol high low', 'Range', 'C2')

% DAC, wind, green ethylene
fileName = 'Propanol/DAC + wind + gEthylene - 2022.xlsx';

gPropanolPrice = readmatrix(fileName, 'Sheet', 'Summary', 'Range', 'C24:C24') * 1000; % USD2022 per ton

carbonDioxideReqEthylene = 3.62; % ton carbon dioxide per ton of ethylene
carbonDioxideReqEthylene = carbonDioxideReqEthylene * ethyleneReq; % ton carbon dioxide per hr for total ethylene required in the process
totalCarbonDioxideReq = carbonDioxideReq + carbonDioxideReqEthylene;
NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
NGReqCarbonDioxide = NGReqCarbonDioxide * totalCarbonDioxideReq; % ton NG per hr
NGPriceDAC = 3.5 * 47.1 * CEPCI2022 / CEPCI2018; % refer Keith 2018

H2ReqEthylene = 0.47; %ton per ton ethylene
H2ReqEthylene = H2ReqEthylene * ethyleneReq; % ton hydrogen per hr for total ethylene required in the process
totalH2Req = H2Req + H2ReqEthylene;

gPropanolPriceWithoutNGAndH = gPropanolPrice - (naturalGasReq * naturalGasPrice + ...
    NGReqCarbonDioxide * NGPriceDAC + totalH2Req * hydrogenPrice) / gPropanolProduced; % USD2022 per ton
gPropanolWindPrices = (gPropanolPriceWithoutNGAndH + ((naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices + totalH2Req * HWind) ./ gPropanolProduced)'; % with NG required for cabron dioxide
gPropanolSolarPrices = (gPropanolPriceWithoutNGAndH + ((naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices + totalH2Req * HSolar) ./ gPropanolProduced)'; % with NG required for cabron dioxide
gPropanolNuclearPrices = (gPropanolPriceWithoutNGAndH + ((naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices + totalH2Req * HNuclear) ./ gPropanolProduced)'; % with NG required for cabron dioxide
gPropanolPrices = [gPropanolWindPrices gPropanolSolarPrices gPropanolNuclearPrices];
writematrix(gPropanolPrices, 'Prices sensitivity.xlsx', 'Sheet', 'Propanol', 'Range', 'F2')

gPropanolWindPricesSe = (gPropanolPriceWithoutNGAndH' + (naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices ./ gPropanolProduced)' + totalH2Req * HWindSe / gPropanolProduced; % with NG required for cabron dioxide
gPropanolSolarPricesSe = (gPropanolPriceWithoutNGAndH' + (naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices ./ gPropanolProduced)' + totalH2Req * HSolarSe / gPropanolProduced; % with NG required for cabron dioxide
gPropanolNuclearPricesSe = (gPropanolPriceWithoutNGAndH' + (naturalGasReq + NGReqCarbonDioxide) ...
    .* naturalGasPrices ./ gPropanolProduced)' + totalH2Req * HNuclearSe / gPropanolProduced; % with NG required for cabron dioxide
gPropanolPricesSe = [gPropanolWindPricesSe gPropanolSolarPricesSe gPropanolNuclearPricesSe];
writematrix(gPropanolPricesSe, 'Prices sensitivity.xlsx', 'Sheet', 'Propanol high low', 'Range', 'I2')
