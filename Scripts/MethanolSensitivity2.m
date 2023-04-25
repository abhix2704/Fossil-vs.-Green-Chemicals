clear 
close all
clc

%% CEPCI indexes
CEPCI2008 = 575.4;
CEPCI2009 = 521.9;
CEPCI2012 = 584.6;
CEPCI2015 = 556.8;
CEPCI2016 = 541.7;
CEPCI2017 = 567.5;
CEPCI2018 = 603.1;
CEPCI2019 = 607.5;
CEPCI2020 = 596.2;
CEPCI2021 = 708.0;
CEPCI2022 = 817.5;

naturalGasPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Methanol MP', 'Range', 'F2:F96');
elecPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Methanol MP', 'Range', 'G2:G96')/1000;

% coalPrices = 0:50:5000;
NGLHV1 = 13.1; % in MWh per ton
NGLHV2 = 36.6 / 3600; % in MWh per m3
NGDensity = NGLHV2 / NGLHV1; % ton per m3
a = CEPCI2015/CEPCI2019;
b = CEPCI2016/CEPCI2019;
c = CEPCI2017/CEPCI2019;
d = CEPCI2018/CEPCI2019;
e = CEPCI2019/CEPCI2019;
f = CEPCI2020/CEPCI2019;
g = CEPCI2021/CEPCI2019;
h = CEPCI2022/CEPCI2019;

%% Methanol sensitivity

% BAU process (data from Iasonas et al. 2019 and SimaPro inventory)
naturalGasReq = (0.6518*36.6 + 6.93)/47.1; % ton NG per ton methanol
elecReq = 0.074*1000; % kWh per ton methanol
methanolPriceWithoutNG = 84.8*CEPCI2019/CEPCI2015; % in USD2019 per ton methanol
methanolPriceWithoutNG = [methanolPriceWithoutNG*a methanolPriceWithoutNG*b...
    methanolPriceWithoutNG*c methanolPriceWithoutNG*d methanolPriceWithoutNG*e...
    methanolPriceWithoutNG*f methanolPriceWithoutNG*g methanolPriceWithoutNG*h]; % in USD2022 per ton
j = 1;
for i = 1:length(naturalGasPrices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    elseif i > 24 && i <= 36
        j = 3;
    elseif i > 36 && i <= 48
        j = 4;
    elseif i > 48 && i <= 60
        j = 5;
    elseif i > 60 && i <= 72
        j = 6;
    elseif i > 72 && i <= 84
        j = 7;
    else
        j = 8;
    end
    methanolPrices(i) = (methanolPriceWithoutNG(j) + naturalGasPrices(i) * naturalGasReq + elecPrices(i) * elecReq)'; 
end
prices = methanolPrices';

writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol MP', 'Range', 'E2')

% naturalGasPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Methanol MP', 'Range', 'F2:F46');
% elecPrices = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Methanol MP', 'Range', 'G2:G46')/1000;
% 
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
%     methanolPrices(i) = (methanolPriceWithoutNG(j) + naturalGasPrices(i) * naturalGasReq + elecPrices(i) * elecReq)'; 
% end
% prices = methanolPrices';
% 
% writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol MP', 'Range', 'H2')

% % DAC process (data from Daniel et al. 2021)
% gMethanolPrice = 1390; % USD2018 per ton
% CO2Req = 1.5; % ton carbon dioxide per ton methanol
% H2Req = 0.192; % ton hydrogen per ton methanol
% CO2Price = 95.5; % USD2018 per ton
% H2Price = 5240 * 1.1597 * CEPCI2018 / CEPCI2015; % USD2018 per ton
% elecReq = 169; % kWh per ton methanol
% elecPrice = 94.5/1000; % USD2018 per kWh
% gMethanolWithoutHydrogenAndCO2 = gMethanolPrice - CO2Req * CO2Price - H2Price * H2Req - elecReq * elecPrice;
% gMethanolWithoutHydrogenAndCO2 = gMethanolWithoutHydrogenAndCO2 * CEPCI2019 / CEPCI2018;
% gMethanolWithoutHydrogenAndCO2 = [gMethanolWithoutHydrogenAndCO2 gMethanolWithoutHydrogenAndCO2*a...
%     gMethanolWithoutHydrogenAndCO2*b gMethanolWithoutHydrogenAndCO2*c];
% CO2DACt = 164.2;
% CO2DAC = [CO2DACt CO2DACt*a CO2DACt*b CO2DACt*c];
% CO2DACLowt = 94.7;
% CO2DACLow = [CO2DACLowt CO2DACLowt*a CO2DACLowt*b CO2DACLowt*c];
% CO2DACHight = 233.7;
% CO2DACHigh = [CO2DACHight CO2DACHight*a CO2DACHight*b CO2DACHight*c];
% 
% NGReqCarbonDioxide = 138.89; % m3 per ton of carbon dioxide
% NGReqCarbonDioxide = NGReqCarbonDioxide * NGDensity; % ton of NG per ton of carbon dioxide
% NGReqCarbonDioxide = NGReqCarbonDioxide * CO2Req; % ton NG per ton methanol
% NGPriceDAC = 3.5 * 47.1 * CEPCI2019 / CEPCI2018; % refer Keith 2018
% NGPriceDAC = [NGPriceDAC NGPriceDAC*a NGPriceDAC*b NGPriceDAC*c];
% 
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
% 
%     gMethanolWind(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HWindAvg(j) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     gMethanolWindLow(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HWindLow(j) + CO2Req*CO2DACLow(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     gMethanolWindHigh(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HWindHigh(j) + CO2Req*CO2DACHigh(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%    
%     gMethanolSolar(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HSolarAvg(j) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     gMethanolSolarLow(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HSolarLow(j) + CO2Req*CO2DACLow(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     gMethanolSolarHigh(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HSolarHigh(j) + CO2Req*CO2DACHigh(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     
%     gMethanolNuclear(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HNuclearAvg(j) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     gMethanolNuclearLow(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HNuclearLow(j) + CO2Req*CO2DACLow(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
%     gMethanolNuclearHigh(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*HNuclearHigh(j) + CO2Req*CO2DACHigh(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
% 
%     gMethanolSMRCCS(i) = gMethanolWithoutHydrogenAndCO2(j) + ...
%         (H2Req*H2SMRCCS(i) + CO2Req*CO2DAC(j) + elecReq*elecPrices(i)) + ...
%         NGReqCarbonDioxide*(naturalGasPrices(i) - NGPriceDAC(j));
% end
% 
% biomassReq = 1.74; % ton straw per ton methanol
% elecReq = (0.0857 + 0.00489 + 0.0099) * 1000; % kWh per ton methanol
% biomassPrice = 336 - elecReq * 0.75/6.8;
% gMethanolBiomassCCS(1:12) = biomassPrice * CEPCI2019/CEPCI2018;
% gMethanolBiomassCCS(13:24) = biomassPrice * CEPCI2020/CEPCI2018;
% gMethanolBiomassCCS(25:36) = biomassPrice * CEPCI2021/CEPCI2018;
% gMethanolBiomassCCS(37:length(gMethanolNuclear)) = biomassPrice * CEPCI2022/CEPCI2018;
% gMethanolBiomassCCS = gMethanolBiomassCCS' + elecPrices .* elecReq;
% 
% gMethanolPrice = [gMethanolBiomassCCS gMethanolWind'...
%     gMethanolSolar' gMethanolNuclear'];
% gMethanolPricesSe = [gMethanolWindLow' gMethanolWindHigh' gMethanolSolarLow' gMethanolSolarHigh'...
%     gMethanolNuclearLow' gMethanolNuclearHigh'];
% 
% writematrix(gMethanolPrice, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol', 'Range', 'F2')
% writematrix(gMethanolPricesSe, 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol high low', 'Range', 'E2')
% writematrix(gMethanolSMRCCS', 'Prices sensitivity 2.xlsx', 'Sheet', 'Methanol', 'Range', 'S2')
% 
% 
% % %% Hydrogen calculations
% % 
% % writematrix(H2SMRCCS', 'Prices sensitivity 2.xlsx', 'Sheet', 'Hydrogen', 'Range', 'D2')
% % j = 1;
% % for i = 1:length(naturalGasPrices)
% %     if i > 0 && i <= 12
% %         j = 1;
% %     elseif i > 12 && i <= 24
% %         j = 2;
% %     elseif i > 24 && i <= 36
% %         j = 3;
% %     else
% %         j = 4;
% %     end
% %     H2WindPrices(i) = HWindAvg(j);
% %     H2WindPricesLow(i) = HWindLow(j);
% %     H2WindPricesHigh(i) = HWindHigh(j);
% % 
% %     H2SolarPrices(i) = HSolarAvg(j);
% %     H2SolarPricesLow(i) = HSolarLow(j);
% %     H2SolarPricesHigh(i) = HSolarHigh(j);
% % 
% %     H2NuclearPrices(i) = HNuclearAvg(j);
% %     H2NuclearPricesLow(i) = HNuclearLow(j);
% %     H2NuclearPricesHigh(i) = HNuclearHigh(j);
% % 
% %     H2BiomassPrices(i) = HBiomassCCSAvg(j);
% % end
% % prices = [H2WindPrices' H2SolarPrices' H2NuclearPrices' H2BiomassPrices'];
% % pricesSe = [H2WindPricesLow' H2WindPricesHigh' H2SolarPricesLow' H2SolarPricesHigh'...
% %     H2NuclearPricesLow' H2NuclearPricesHigh'];
% % 
% % writematrix(prices, 'Prices sensitivity 2.xlsx', 'Sheet', 'Hydrogen', 'Range', 'E2')
% % writematrix(pricesSe, 'Prices sensitivity 2.xlsx', 'Sheet', 'Hydrogen high low', 'Range', 'E2')
% 
% 
