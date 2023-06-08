%LCOH calculations 
clear;

LCOEWind2021 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Wind LCOH Countries', 'Range', 'H10:H10'); % in USD per kWh
LCOESolar2021 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Solar LCOH Countries', 'Range', 'H9:H9'); % in USD per kWh

NGPrices2021 = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'C26:C37')/1000; % in USD per kg
NGPrices = NGPrices2021;

NGReqWind = 0.002376642; % m3 per kWh of wind electricity
NGReqSolar = 0.002709867; % m3 per kWh of solar electricity
NGReqWind = NGReqWind * 36.6 / 47.1; % kg natural gas per kWh
NGReqSolar = NGReqSolar * 36.6 / 47.1; % kg natural gas per kWh

percentNGWindElec = NGReqWind .* NGPrices ./ LCOEWind2021 .* 100; % percentage natural gas in 1 kWh of wind electricity
percentNGSolarElec = NGReqSolar .* NGPrices ./ LCOESolar2021 .* 100; % percentage natural gas in 1 kWh of solar electricity
percentNGWindElecAvg = mean(percentNGWindElec); % 2021 average for 1 kWh
percentNGSolarElecAvg = mean(percentNGSolarElec); % 2021 average for 1 kWh

elecReqH2 = 55; % kWh per kg hydrogen
LCOHWind2021 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Wind LCOH Countries', 'Range', 'J10:J10'); % in USD per kg hydrogen
LCOHSolar2021 = readmatrix('Prices regionalization.xlsx', 'Sheet', 'Solar LCOH Countries', 'Range', 'J9:J9'); % in USD per kg hydrogen

NGReqWindH2 = NGReqWind * elecReqH2; % kg natural gas per kg hydrogen for wind
NGReqSolarH2 = NGReqSolar * elecReqH2; % kg natural gas per kg hydrogen for solar

percentNGWindElecH2 = NGReqWindH2 .* NGPrices ./ LCOHWind2021 .* 100;
percentNGSolarElecH2 = NGReqSolarH2 .* NGPrices ./ LCOHSolar2021 .* 100;
percentNGWindElecH2Avg = mean(percentNGWindElecH2); % 2021 average for 1 kg hydrogen
percentNGSolarElecH2Avg = mean(percentNGSolarElecH2); % 2021 average for 1 kg hydrogen