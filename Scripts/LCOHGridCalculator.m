%LCOH calculations 
clear;

%% Constants
mat = readmatrix('Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'S2:S48');
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

LCOE = mat./1000; % in $/kW
capacity_factor = 100;

life_span = stack_lifetime./(8760.*capacity_factor./100);
annual_H2_prod = nominal_H2_per_stack_mass.*stack_lifetime./life_span;
capital_recovery_fac = (WACC*(1+WACC).^life_span)./((1+WACC).^life_span-1);
CAPEX = 0;
for i=-1:1:0
   annualization = (1+interest_rate)^i;
   CAPEX = CAPEX + (nominal_input_power*capital_cost*0.5/annualization); 
end
OPEX = zeros(1,length(LCOE));
LCOH_spec = zeros(1,length(LCOE));
OPEX_elec = zeros(1,length(LCOE));
OPEX_fixed = zeros(1,length(LCOE));
total_H2_produced = zeros(1,length(LCOE));
equip_replacement = zeros(1,length(LCOE));
plant_decomissioning = zeros(1,length(LCOE));

i = 1;
while i < life_span
    if i==1
        H2_production_capacity = 0.5;
    else
        H2_production_capacity = 1;
    end
    annualization = (1+interest_rate)^i;
    hydrogen_produced = annual_H2_prod*H2_production_capacity/annualization;
    OPEX_elec = OPEX_elec + power_demand_per_kg*LCOE*hydrogen_produced; 
    OPEX_fixed = OPEX_fixed + other_opex_fac*nominal_input_power*capital_cost/annualization;
    total_H2_produced = total_H2_produced + hydrogen_produced; 
    plant_decomissioning = decomissioning_fac*nominal_input_power*capital_cost/annualization;
    if rem(i,7)==0
        equip_replacement = equip_replacement + equipment_replacement_fac...
                            *nominal_input_power*capital_cost/annualization;
    end
    i = i + 1;
end
OPEX = OPEX_elec + OPEX_fixed + plant_decomissioning + equip_replacement;
LCOH_spec = (CAPEX+OPEX)/total_H2_produced;

LCOH = LCOH_spec;
writematrix(LCOH*1000, 'Prices sensitivity 2.xlsx', 'Sheet', 'Ammonia', 'Range', 'W2')





