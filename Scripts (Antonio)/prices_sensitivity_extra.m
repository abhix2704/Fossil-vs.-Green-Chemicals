clear 
close all
clc

%% CEPCI indexes
CEPCI_2008 = 575.4;
CEPCI_2009 = 521.9;
CEPCI_2012 = 584.6;
CEPCI_2015 = 556.8;
CEPCI_2017 = 567.5;
CEPCI_2018 = 603.1;
CEPCI_2019 = 607.5;
CEPCI_2020 = 596.2;
CEPCI_2021 = 708.0;
CEPCI_2022 = 816.0;
CEPCI_2023 = 798.1;

natural_gas_prices = readmatrix('prices_sensitivity_extra.xlsx', 'Sheet', 'Ammonia', 'Range', 'C2:C25');
elec_prices = readmatrix('prices_sensitivity_extra.xlsx', 'Sheet', 'Ammonia', 'Range', 'G2:G25')/1000;

ng_lhv_1 = 13.1; % in MWh per ton
ng_lhv_2 = 36.6 / 3600; % in MWh per m3
ng_density = ng_lhv_2 / ng_lhv_1; % ton per m3
a = CEPCI_2022/CEPCI_2019;
b = CEPCI_2023/CEPCI_2019;

%% Ammonia sensitivity
% BAU process
file_name = 'Ammonia/BAU - 2019.xlsx';
ammonia_price = readmatrix(file_name, 'Sheet', 'Summary', 'Range', 'C24:C24') * 1000; % USD2019 per ton
natural_gas_req = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'D5:D5'); % in ton/hr
natural_gas_req = natural_gas_req + readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'D15:D15'); % in ton/hr
natural_gas_price = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'E5:E5') * CEPCI_2019 / CEPCI_2018; % in USD2019 per ton
elec_req = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'D9:D9'); % in kWh/hr
elec_price = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'E9:E9') * CEPCI_2019 / CEPCI_2018; % in USD2019 per kWh
ammonia_produced = readmatrix(file_name, 'Sheet', 'Summary', 'Range', 'C23:C23') / 1000; % amount of ammonia produced in ton/hr

ammonia_price_without_NG = ammonia_price - (natural_gas_req * natural_gas_price + elec_req * elec_price) / ammonia_produced; % USD2019 per ton
ammonia_price_without_NG = [ammonia_price_without_NG*a ammonia_price_without_NG*b]; 

j = 1;
for i = 1:length(natural_gas_prices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    end
    ammonia_prices(i) = (ammonia_price_without_NG(j) + (natural_gas_prices(i) * natural_gas_req +...
        elec_prices(i) * elec_req) ./ ammonia_produced);
end
prices = ammonia_prices;
writematrix(prices', 'prices_sensitivity_extra.xlsx', 'Sheet', 'Ammonia', 'Range', 'D2')

% Green process
file_name = 'Ammonia/Green ammonia - 2019.xlsx';

gammonia_price = readmatrix(file_name, 'Sheet', 'Summary', 'Range', 'C26:C26') * 1000; % USD2019 per ton
gammonia_produced = readmatrix(file_name, 'Sheet', 'Summary', 'Range', 'C25:C25') / 1000; % amount of ammonia produced in ton/hr
hydrogen_price = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'E6:E6'); % in ton/hr
hydrogen_req = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'D6:D6'); % in ton/hr
elec_req = readmatrix(file_name, 'Sheet', 'OPEX', 'Range', 'D12:D12'); % in kWh/hr

gammonia_price_without_H = gammonia_price - (hydrogen_req * hydrogen_price + elec_req * elec_price) / gammonia_produced; % USD2019 per ton
gammonia_price_without_H = [gammonia_price_without_H*a gammonia_price_without_H*b];

% Green hydrogen prices from Parkinson 2019
h_wind = readmatrix('prices_sensitivity_extra.xlsx', 'Sheet', 'LCOH', 'Range', 'B17:I17');
h_solar = readmatrix('prices_sensitivity_extra.xlsx', 'Sheet', 'LCOH', 'Range', 'B18:I18');  

j = 1;
for i = 2:length(h_wind)
    if mod(i,2) == 0 && mod(i,4) ~= 0
        h_wind_avg(j) = h_wind(i-1)*1000;
        h_wind_low(j) = h_wind(i)*1000;
        h_wind_high(j) = h_wind(i+1)*1000;
        h_solar_avg(j) = h_solar(i-1)*1000;
        h_solar_low(j) = h_solar(i)*1000;
        h_solar_high(j) = h_solar(i+1)*1000;
        j = j + 1;
    end
end

j = 1;
for i = 1:length(natural_gas_prices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    end
    gammonia_wind(i) = gammonia_price_without_H(j)+(hydrogen_req*h_wind_avg(j)+...
        elec_req*elec_prices(i))/gammonia_produced;
    gammonia_wind_low(i) = gammonia_price_without_H(j)+(hydrogen_req*h_wind_low(j)+...
        elec_req*elec_prices(i))/gammonia_produced;
    gammonia_wind_high(i) = gammonia_price_without_H(j)+(hydrogen_req*h_wind_high(j)+...
        elec_req*elec_prices(i))/gammonia_produced;
    
    gammonia_solar(i) = gammonia_price_without_H(j)+(hydrogen_req*h_solar_avg(j)+...
        elec_req*elec_prices(i))/gammonia_produced;
    gammonia_solar_low(i) = gammonia_price_without_H(j)+(hydrogen_req*h_solar_low(j)+...
        elec_req*elec_prices(i))/gammonia_produced;
    gammonia_solar_high(i) = gammonia_price_without_H(j)+(hydrogen_req*h_solar_high(j)+...
        elec_req*elec_prices(i))/gammonia_produced;
end
prices = [gammonia_wind' gammonia_solar'];
pricesSe = [gammonia_wind_low' gammonia_wind_high' gammonia_solar_low' gammonia_solar_high'];
writematrix(prices, 'prices_sensitivity_extra.xlsx', 'Sheet', 'Ammonia', 'Range', 'E2')

%% Methanol sensitivity
% BAU process (data from Plant to Planet Methanol)
natural_gas_req = (0.6518*36.6 + 6.93)/47.1; % ton NG per ton methanol
elec_req = 0.074*1000; % kWh per ton methanol
methanol_price_without_NG = 84.8*CEPCI_2019/CEPCI_2015; % in USD2019 per ton methanol
methanol_price_without_NG = [methanol_price_without_NG*a methanol_price_without_NG*b]; % in USD2022 per ton
j = 1;
for i = 1:length(natural_gas_prices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    end
    methanol_prices(i) = (methanol_price_without_NG(j) + natural_gas_prices(i) * natural_gas_req + elec_prices(i) * elec_req)'; 
end

prices = methanol_prices';
writematrix(prices, 'prices_sensitivity_extra.xlsx', 'Sheet', 'Methanol', 'Range', 'D2')


% DAC process (data from Daniel et al. 2021)
gmethanol_price = 1380; % USD2015 per ton
carbon_dioxide_req = 1.45; % ton carbon dioxide per ton methanol
hydrogen_req = 0.19; % ton hydrogen per ton methanol
carbon_dioxide_price = 160; % USD2015 per ton
hydrogen_price = 5240; % USD2015 per ton
elec_req = 0.3*1000; % kWh per ton methanol
elec_price = 104.61/1000; % USD2015 per kWh
gmethanol_without_H_CO2 = gmethanol_price - carbon_dioxide_req * carbon_dioxide_price - hydrogen_price * hydrogen_req...
        - elec_req * elec_price;
gmethanol_without_H_CO2 = gmethanol_without_H_CO2 * CEPCI_2019 / CEPCI_2015;
gmethanol_without_H_CO2 = [gmethanol_without_H_CO2*a gmethanol_without_H_CO2*b];
CO2_DACt = 164.2;
CO2_DAC = [CO2_DACt*a CO2_DACt*b];
CO2_DAC_Lowt = 94.7;
CO2_DAC_Low = [CO2_DAC_Lowt*a CO2_DAC_Lowt*b];
CO2_DAC_Hight = 233.7;
CO2_DAC_High = [CO2_DAC_Hight*a CO2_DAC_Hight*b];

NG_req_carbon_dioxide = 138.89; % m3 per ton of carbon dioxide
NG_req_carbon_dioxide = NG_req_carbon_dioxide * ng_density; % ton of NG per ton of carbon dioxide
NG_req_carbon_dioxide = NG_req_carbon_dioxide * carbon_dioxide_req; % ton NG per ton methanol
NG_price_DAC = 3.5 * 47.1 * CEPCI_2019 / CEPCI_2018; % refer Keith 2018
NG_price_DAC = [NG_price_DAC*a NG_price_DAC*b];

j = 1;
for i = 1:length(natural_gas_prices)
    if i > 0 && i <= 12
        j = 1;
    elseif i > 12 && i <= 24
        j = 2;
    end
    c_prices(i) = carbon_dioxide_req*CO2_DAC(j) + NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
    c_prices_low(i) = carbon_dioxide_req*CO2_DAC_Low(j) + NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
    c_prices_high(i) = carbon_dioxide_req*CO2_DAC_High(j) + NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));

    gmethanol_wind(i) = gmethanol_without_H_CO2(j) + ...
        (hydrogen_req*h_wind_avg(j) + carbon_dioxide_req*CO2_DAC(j) + elec_req*elec_prices(i)) + ...
        NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
    gmethanol_wind_low(i) = gmethanol_without_H_CO2(j) + ...
        (hydrogen_req*h_wind_low(j) + carbon_dioxide_req*CO2_DAC_Low(j) + elec_req*elec_prices(i)) + ...
        NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
    gmethanol_wind_high(i) = gmethanol_without_H_CO2(j) + ...
        (hydrogen_req*h_wind_high(j) + carbon_dioxide_req*CO2_DAC_High(j) + elec_req*elec_prices(i)) + ...
        NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
   
    gmethanol_solar(i) = gmethanol_without_H_CO2(j) + ...
        (hydrogen_req*h_solar_avg(j) + carbon_dioxide_req*CO2_DAC(j) + elec_req*elec_prices(i)) + ...
        NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
    gmethanol_solar_low(i) = gmethanol_without_H_CO2(j) + ...
        (hydrogen_req*h_solar_low(j) + carbon_dioxide_req*CO2_DAC_Low(j) + elec_req*elec_prices(i)) + ...
        NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));
    gmethanol_solar_high(i) = gmethanol_without_H_CO2(j) + ...
        (hydrogen_req*h_solar_high(j) + carbon_dioxide_req*CO2_DAC_High(j) + elec_req*elec_prices(i)) + ...
        NG_req_carbon_dioxide*(natural_gas_prices(i) - NG_price_DAC(j));

end

gmethanol_price = [gmethanol_wind' gmethanol_solar'];
gmethanol_pricesSe = [gmethanol_wind_low' gmethanol_wind_high' gmethanol_solar_low' gmethanol_solar_high'];

writematrix(gmethanol_price, 'prices_sensitivity_extra.xlsx', 'Sheet', 'Methanol', 'Range', 'E2')
writematrix(c_prices', 'prices_sensitivity_extra.xlsx', 'Sheet', 'DAC', 'Range', 'C2')
writematrix(c_prices_low', 'prices_sensitivity_extra.xlsx', 'Sheet', 'DAC', 'Range', 'D2')
writematrix(c_prices_high', 'prices_sensitivity_extra.xlsx', 'Sheet', 'DAC', 'Range', 'E2')