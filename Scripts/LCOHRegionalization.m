%LCOH calculations 
clear;

%% CEPCI indexes
CEPCI2021 = 708.0;
CEPCI2022 = 817.5;

%% Constants
filename = 'Prices regionalization.xlsx';
mat = readmatrix(filename, 'Sheet', 'Wind LCOH countries', 'Range', 'B3:J10');
mat2 = readmatrix(filename, 'Sheet', 'Solar LCOH countries', 'Range', 'B3:J9');
WACC = 0.064;
interest_rate = 0.064;
salvage_fac = 0;
decomissioning_fac = 0.1;
equipment_replacement_fac = 0.15;
other_opex_fac = 0.04;
density_STP_H2 = 0.08988; % in kg/m^3
spec_en_cons = 5; % in kWh/Nm^3
spec_en_cons = spec_en_cons/density_STP_H2; % convert to kWh/kg H2
nominal_H2_per_stack = 1000; % in Nm^3/h
stack_lifetime = 60000; % in hours
capital_cost = 1000/0.8928; % in $/kW
power_demand_per_kg = 55; % in kWh/kg H2

nominal_H2_per_stack_mass  = nominal_H2_per_stack*density_STP_H2; % in kg H2/h
nominal_input_power = spec_en_cons*nominal_H2_per_stack_mass; %in kW

windLCOE = [mat(:,1); mat(:,4); mat(:,7)]; % in $/kW
windCapacity_factor = [mat(:,2); mat(:,5); mat(:,8)];

solarLCOE = [mat2(:,1); mat2(:,4); mat2(:,7)];
solarCapacity_factor = [mat2(:,2); mat2(:,5); mat2(:,8)];


LCOE = [windLCOE; solarLCOE];
capacity_factor = [windCapacity_factor; solarCapacity_factor];

% LCOE = [0.0510 0.0370 0.0310 0.0680 0.0570 0.0550]; % in $/kW
% capacity_factor = [44 43 45 18 16 17];

life_span = stack_lifetime./(8760.*capacity_factor./100);
annual_H2_prod = nominal_H2_per_stack_mass.*stack_lifetime./life_span;
capital_recovery_fac = (WACC*(1+WACC).^life_span)./((1+WACC).^life_span-1);
CAPEX = 0;
for i=-1:1:0
   annualization = (1+interest_rate)^i;
   CAPEX = CAPEX + (nominal_input_power*capital_cost*0.5/annualization); 
end
OPEX = zeros(length(LCOE),1);
LCOH_spec = zeros(length(LCOE),1);
LCOH = zeros(length(LCOE),1);
OPEX_elec = zeros(length(LCOE),1);
OPEX_fixed = zeros(length(LCOE),1);
total_H2_produced = zeros(length(LCOE),1);
equip_replacement = zeros(length(LCOE),1);
plant_decomissioning = zeros(length(LCOE),1);

for j = 1:length(LCOE)
    i = 1;
    while i < life_span(j)
        if i==1
            H2_production_capacity = 0.5;
        else
            H2_production_capacity = 1;
        end
        annualization = (1+interest_rate)^i;
        hydrogen_produced = annual_H2_prod(j)*H2_production_capacity/annualization;
        OPEX_elec(j) = OPEX_elec(j) + power_demand_per_kg*LCOE(j)*hydrogen_produced; 
        OPEX_fixed(j) = OPEX_fixed(j) + other_opex_fac*nominal_input_power*capital_cost/annualization;
        total_H2_produced(j) = total_H2_produced(j) + hydrogen_produced; 
        plant_decomissioning(j) = decomissioning_fac*nominal_input_power*capital_cost/annualization;
        if rem(i,7)==0
            equip_replacement(j) = equip_replacement(j) + equipment_replacement_fac...
                                *nominal_input_power*capital_cost/annualization;
        end
        i = i + 1;
    end
    OPEX(j) = OPEX_elec(j) + OPEX_fixed(j) + plant_decomissioning(j) + equip_replacement(j);
    LCOH_spec(j) = (CAPEX+OPEX(j))/total_H2_produced(j);
    
    LCOH(j) = LCOH_spec(j);
end
a = CEPCI2022/CEPCI2021;
writematrix(LCOH(1:8), filename, 'Sheet', 'Wind LCOH countries', 'Range', 'D3');
writematrix(LCOH(9:16), filename, 'Sheet', 'Wind LCOH countries', 'Range', 'G3');
writematrix(LCOH(17:24), filename, 'Sheet', 'Wind LCOH countries', 'Range', 'J3');
writematrix(LCOH(17:24)*a, filename, 'Sheet', 'Wind LCOH countries', 'Range', 'K3');

writematrix(LCOH(25:31), filename, 'Sheet', 'Solar LCOH countries', 'Range', 'D3');
writematrix(LCOH(32:38), filename, 'Sheet', 'Solar LCOH countries', 'Range', 'G3');
writematrix(LCOH(39:45), filename, 'Sheet', 'Solar LCOH countries', 'Range', 'J3');
writematrix(LCOH(39:45)*a, filename, 'Sheet', 'Solar LCOH countries', 'Range', 'K3');


%% LCOH 2022 including nothing (same as 2021)
LCOHWind2022IN = LCOH(17:24);
LCOHSolar2022IN = LCOH(39:45);

%% LCOH 2022 including only inflation
CEPCI2022Monthly = [797.6 801.3 803.6 816.3 831.1 832.6 829.8 824.5 821.3 816.2 814.6];
CEPCI2022MonthlyAvg = zeros(length(CEPCI2022Monthly),1);
for i = 1:length(CEPCI2022Monthly)
    CEPCI2022MonthlyAvg(i) = mean(CEPCI2022Monthly(1:i));
end
a = CEPCI2022MonthlyAvg ./ CEPCI2021;
LCOHWind2022II = LCOH(17:24)'.*a;
LCOHSolar2022II = LCOH(39:45)'.*a;
% a = zeros(length(CEPCI2022Monthly), 1);
% a(1) = CEPCI2022Monthly(1) ./ CEPCI2021;
% LCOHWind2022II = zeros(length(CEPCI2022Monthly), length(LCOH(17:24)));
% LCOHSolar2022II = zeros(length(CEPCI2022Monthly), length(LCOH(39:45)));
% LCOHWind2022II(1, :) = LCOH(17:24)' .* a(1);
% LCOHSolar2022II(1, :) = LCOH(39:45)' .* a(1);
% for i = 2:length(a)
%     a(i) = CEPCI2022Monthly(i)/CEPCI2022Monthly(i-1);
%     LCOHWind2022II(i, :) = LCOHWind2022II(i-1, :) .* a(i);
%     LCOHSolar2022II(i, :) = LCOHSolar2022II(i-1, :) .* a(i);
% end
writematrix(LCOHWind2022II, filename, 'Sheet', 'Wind LCOH 2022', 'Range', 'B2');
writematrix(LCOHSolar2022II, filename, 'Sheet', 'Solar LCOH 2022', 'Range', 'B2');

%% LCOH 2022 including only natural gas
NGReqWind = 0.002376642; % m3 per kWh of wind electricity
NGReqSolar = 0.002709867; % m3 per kWh of solar electricity
NGReqWind = NGReqWind * 36.6 / 47.1; % kg per kWh
NGReqSolar = NGReqSolar * 36.6 / 47.1; % kg per kWh
elecReqH2 = 55; % kWh per kg hydrogen
NGReqWindH2 = NGReqWind * elecReqH2; % kg natural gas per kg hydrogen for wind
NGReqSolarH2 = NGReqSolar * elecReqH2; % kg natural gas per kg hydrogen for solar

NGPrices2021 = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'C26:C37')/1000; % in USD per kg
NGPrices2022 = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'C38:C48')/1000; % in USD per kg

LCOHWind2022ING = zeros(length(NGPrices2022), length(LCOHWind2022IN));
LCOHSolar2022ING = zeros(length(NGPrices2022), length(LCOHSolar2022IN));
for i = 1:length(NGPrices2021)-1
    LCOHWind2022ING(i, :) = LCOHWind2022IN' + (NGPrices2022(i) - NGPrices2021(i)) * NGReqWindH2;
    LCOHSolar2022ING(i, :) = LCOHSolar2022IN' + (NGPrices2022(i) - NGPrices2021(i)) * NGReqSolarH2;
end

writematrix(LCOHWind2022ING, filename, 'Sheet', 'Wind LCOH 2022', 'Range', 'B13');
writematrix(LCOHSolar2022ING, filename, 'Sheet', 'Solar LCOH 2022', 'Range', 'B13');

%% LCOH 2022 including both inflation and natural gas
LCOHWind2022IING = zeros(length(NGPrices2022), length(LCOHWind2022IN));
LCOHSolar2022IING = zeros(length(NGPrices2022), length(LCOHSolar2022IN));
for i = 1:length(NGPrices2021)-1
    LCOHWind2022IING(i, :) = (LCOHWind2022IN' - NGPrices2021(i) * NGReqWindH2)*a(i)  + (NGPrices2022(i) * NGReqWindH2);
    LCOHSolar2022IING(i, :) = (LCOHSolar2022IN' - NGPrices2021(i) * NGReqSolarH2)*a(i) + (NGPrices2022(i) * NGReqSolarH2);
end

writematrix(LCOHWind2022IING, filename, 'Sheet', 'Wind LCOH 2022', 'Range', 'B24');
writematrix(LCOHSolar2022IING, filename, 'Sheet', 'Solar LCOH 2022', 'Range', 'B24');