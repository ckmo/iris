# (C) British Crown Copyright 2010 - 2012, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.

# DO NOT EDIT: AUTO-GENERATED RULES

import collections


CFname = collections.namedtuple('CFname', ['cfname', 'unit'])


STASH_TO_CF = {
    "m01s00i004" : CFname(cfname="air_potential_temperature", unit="K"),
    "m01s00i009" : CFname(cfname="moisture_content_of_soil_layer", unit="kg m-2"),
    "m01s00i010" : CFname(cfname="specific_humidity", unit="1"),
    "m01s00i012" : CFname(cfname="mass_fraction_of_cloud_ice_in_air", unit="1"),
    "m01s00i013" : CFname(cfname="convective_cloud_area_fraction", unit="1"),
    "m01s00i020" : CFname(cfname="soil_temperature", unit="K"),
    "m01s00i023" : CFname(cfname="snowfall_amount", unit="kg m-2"),
    "m01s00i024" : CFname(cfname="surface_temperature", unit="K"),
    "m01s00i025" : CFname(cfname="atmosphere_boundary_layer_thickness", unit="m"),
    "m01s00i026" : CFname(cfname="surface_roughness_length", unit="m"),
    "m01s00i028" : CFname(cfname="surface_eastward_sea_water_velocity", unit="m s-1"),
    "m01s00i029" : CFname(cfname="surface_northward_sea_water_velocity", unit="m s-1"),
    "m01s00i030" : CFname(cfname="land_binary_mask", unit="1"),
    "m01s00i031" : CFname(cfname="sea_ice_area_fraction", unit="1"),
    "m01s00i032" : CFname(cfname="sea_ice_thickness", unit="m"),
    "m01s00i033" : CFname(cfname="surface_altitude", unit="m"),
    "m01s00i040" : CFname(cfname="volume_fraction_of_condensed_water_in_soil_at_wilting_point", unit="1"),
    "m01s00i041" : CFname(cfname="volume_fraction_of_condensed_water_in_soil_at_critical_point", unit="1"),
    "m01s00i043" : CFname(cfname="soil_porosity", unit="1"),
    "m01s00i044" : CFname(cfname="soil_hydraulic_conductivity_at_saturation", unit="m s-1"),
    "m01s00i046" : CFname(cfname="soil_thermal_capacity", unit="J kg-1 K-1"),
    "m01s00i047" : CFname(cfname="soil_thermal_conductivity", unit="W m-1 K-1"),
    "m01s00i048" : CFname(cfname="soil_suction_at_saturation", unit="Pa"),
    "m01s00i049" : CFname(cfname="sea_ice_temperature", unit="K"),
    "m01s00i050" : CFname(cfname="vegetation_area_fraction", unit="1"),
    "m01s00i051" : CFname(cfname="root_depth", unit="m"),
    "m01s00i052" : CFname(cfname="surface_albedo_assuming_no_snow", unit="1"),
    "m01s00i053" : CFname(cfname="surface_albedo_assuming_deep_snow", unit="1"),
    "m01s00i060" : CFname(cfname="mass_fraction_of_ozone_in_air", unit="1"),
    "m01s00i101" : CFname(cfname="mass_fraction_of_sulfur_dioxide_in_air", unit="1"),
    "m01s00i102" : CFname(cfname="mass_fraction_of_dimethyl_sulfide_in_air", unit="1"),
    "m01s00i150" : CFname(cfname="upward_air_velocity", unit="m s-1"),
    "m01s00i205" : CFname(cfname="land_area_fraction", unit="1"),
    "m01s00i208" : CFname(cfname="leaf_area_index", unit="1"),
    "m01s00i209" : CFname(cfname="canopy_height", unit="m"),
    "m01s00i214" : CFname(cfname="mass_fraction_of_unfrozen_water_in_soil_moisture", unit="1"),
    "m01s00i215" : CFname(cfname="mass_fraction_of_frozen_water_in_soil_moisture", unit="1"),
    "m01s00i217" : CFname(cfname="leaf_area_index", unit="1"),
    "m01s00i218" : CFname(cfname="canopy_height", unit="m"),
    "m01s00i220" : CFname(cfname="soil_albedo", unit="1"),
    "m01s00i223" : CFname(cfname="soil_carbon_content", unit="kg m-2"),
    "m01s00i231" : CFname(cfname="snow_grain_size", unit="1e-6 m"),
    "m01s00i252" : CFname(cfname="mass_fraction_of_carbon_dioxide_in_air", unit="1"),
    "m01s00i254" : CFname(cfname="mass_fraction_of_cloud_liquid_water_in_air", unit="1"),
    "m01s00i255" : CFname(cfname="dimensionless_exner_function", unit="1"),
    "m01s00i269" : CFname(cfname="surface_eastward_sea_water_velocity", unit="m s-1"),
    "m01s00i270" : CFname(cfname="surface_northward_sea_water_velocity", unit="m s-1"),
    "m01s00i406" : CFname(cfname="dimensionless_exner_function", unit="1"),
    "m01s00i407" : CFname(cfname="air_pressure", unit="Pa"),
    "m01s00i408" : CFname(cfname="air_pressure", unit="Pa"),
    "m01s00i409" : CFname(cfname="surface_air_pressure", unit="Pa"),
    "m01s00i505" : CFname(cfname="land_area_fraction", unit="1"),
    "m01s00i506" : CFname(cfname="surface_temperature", unit="K"),
    "m01s00i507" : CFname(cfname="surface_temperature", unit="K"),
    "m01s00i508" : CFname(cfname="surface_temperature", unit="K"),
    "m01s00i509" : CFname(cfname="sea_ice_albedo", unit="1"),
    "m01s01i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s01i201" : CFname(cfname="surface_net_downward_shortwave_flux", unit="W m-2"),
    "m01s01i203" : CFname(cfname="surface_net_downward_shortwave_flux", unit="W m-2"),
    "m01s01i205" : CFname(cfname="toa_outgoing_shortwave_flux", unit="W m-2"),
    "m01s01i207" : CFname(cfname="toa_incoming_shortwave_flux", unit="W m-2"),
    "m01s01i209" : CFname(cfname="toa_outgoing_shortwave_flux_assuming_clear_sky", unit="W m-2"),
    "m01s01i210" : CFname(cfname="surface_downwelling_shortwave_flux_in_air_assuming_clear_sky", unit="W m-2"),
    "m01s01i211" : CFname(cfname="surface_upwelling_shortwave_flux_in_air_assuming_clear_sky", unit="W m-2"),
    "m01s01i235" : CFname(cfname="surface_downwelling_shortwave_flux_in_air", unit="W m-2"),
    "m01s01i410" : CFname(cfname="surface_downwelling_shortwave_flux_in_air_assuming_clear_sky", unit="W m-2"),
    "m01s01i435" : CFname(cfname="surface_downwelling_shortwave_flux_in_air", unit="W m-2"),
    "m01s02i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s02i201" : CFname(cfname="surface_net_downward_longwave_flux", unit="W m-2"),
    "m01s02i203" : CFname(cfname="surface_net_downward_longwave_flux", unit="W m-2"),
    "m01s02i204" : CFname(cfname="cloud_area_fraction", unit="1"),
    "m01s02i205" : CFname(cfname="toa_outgoing_longwave_flux", unit="W m-2"),
    "m01s02i206" : CFname(cfname="toa_outgoing_longwave_flux_assuming_clear_sky", unit="W m-2"),
    "m01s02i232" : CFname(cfname="tendency_of_air_temperature_due_to_longwave_heating", unit="K s-1"),
    "m01s02i260" : CFname(cfname="mass_fraction_of_ozone_in_air", unit="1"),
    "m01s02i261" : CFname(cfname="cloud_area_fraction_in_atmosphere_layer", unit="1"),
    "m01s03i004" : CFname(cfname="air_temperature", unit="m s-1"),
    "m01s03i010" : CFname(cfname="specific_humidity", unit="1"),
    "m01s03i025" : CFname(cfname="atmosphere_boundary_layer_thickness", unit="m"),
    "m01s03i201" : CFname(cfname="downward_heat_flux_in_sea_ice", unit="W m-2"),
    "m01s03i217" : CFname(cfname="surface_upward_sensible_heat_flux", unit="W m-2"),
    "m01s03i223" : CFname(cfname="surface_upward_water_flux", unit="kg m-2 s-1"),
    "m01s03i224" : CFname(cfname="wind_mixing_energy_flux_into_sea_water", unit="W m-2"),
    "m01s03i227" : CFname(cfname="wind_speed", unit="m s-1"),
    "m01s03i228" : CFname(cfname="surface_upward_sensible_heat_flux", unit="W m-2"),
    "m01s03i230" : CFname(cfname="wind_speed", unit="m s-1"),
    "m01s03i236" : CFname(cfname="air_temperature", unit="K"),
    "m01s03i238" : CFname(cfname="soil_temperature", unit="K"),
    "m01s03i245" : CFname(cfname="relative_humidity", unit="%"),
    "m01s03i313" : CFname(cfname="soil_moisture_content_at_field_capacity", unit="kg m-2"),
    "m01s03i332" : CFname(cfname="toa_outgoing_longwave_flux", unit="W m-2"),
    "m01s03i334" : CFname(cfname="water_potential_evaporation_flux", unit="kg m-2 s-1"),
    "m01s03i337" : CFname(cfname="downward_heat_flux_in_soil", unit="W m-2"),
    "m01s03i391" : CFname(cfname="surface_downward_eastward_stress", unit="Pa"),
    "m01s03i392" : CFname(cfname="surface_downward_eastward_stress", unit="Pa"),
    "m01s03i393" : CFname(cfname="surface_downward_northward_stress", unit="Pa"),
    "m01s03i394" : CFname(cfname="surface_downward_northward_stress", unit="Pa"),
    "m01s03i460" : CFname(cfname="surface_downward_eastward_stress", unit="Pa"),
    "m01s03i461" : CFname(cfname="surface_downward_northward_stress", unit="Pa"),
    "m01s04i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s04i010" : CFname(cfname="specific_humidity", unit="1"),
    "m01s04i201" : CFname(cfname="stratiform_rainfall_amount", unit="kg m-2"),
    "m01s04i202" : CFname(cfname="stratiform_snowfall_amount", unit="kg m-2"),
    "m01s04i203" : CFname(cfname="stratiform_rainfall_rate", unit="kg m-2 s-1"),
    "m01s04i204" : CFname(cfname="stratiform_snowfall_rate", unit="kg m-2 s-1"),
    "m01s05i010" : CFname(cfname="specific_humidity", unit="1"),
    "m01s05i181" : CFname(cfname="tendency_of_air_temperature_due_to_convection", unit="K s-1"),
    "m01s05i182" : CFname(cfname="tendency_of_specific_humidity_due_to_convection", unit="s-1"),
    "m01s05i185" : CFname(cfname="tendency_of_eastward_wind_due_to_convection", unit="m s-2"),
    "m01s05i186" : CFname(cfname="tendency_of_northward_wind_due_to_convection", unit="m s-2"),
    "m01s05i201" : CFname(cfname="convective_rainfall_amount", unit="kg m-2"),
    "m01s05i202" : CFname(cfname="convective_snowfall_amount", unit="kg m-2"),
    "m01s05i209" : CFname(cfname="air_temperature", unit="K"),
    "m01s05i214" : CFname(cfname="rainfall_flux", unit="kg m-2 s-1"),
    "m01s05i215" : CFname(cfname="snowfall_flux", unit="kg m-2 s-1"),
    "m01s06i185" : CFname(cfname="tendency_of_eastward_wind_due_to_gravity_wave_drag", unit="m s-2"),
    "m01s06i186" : CFname(cfname="tendency_of_northward_wind_due_to_gravity_wave_drag", unit="m s-2"),
    "m01s06i201" : CFname(cfname="atmosphere_eastward_stress_due_to_gravity_wave_drag", unit="Pa"),
    "m01s06i202" : CFname(cfname="atmosphere_northward_stress_due_to_gravity_wave_drag", unit="Pa"),
    "m01s08i023" : CFname(cfname="surface_snow_amount", unit="kg m-2"),
    "m01s08i204" : CFname(cfname="surface_runoff_amount", unit="kg m-2"),
    "m01s08i205" : CFname(cfname="subsurface_runoff_amount", unit="kg m-2"),
    "m01s08i223" : CFname(cfname="moisture_content_of_soil_layer", unit="kg m-2"),
    "m01s08i225" : CFname(cfname="soil_temperature", unit="K"),
    "m01s08i234" : CFname(cfname="surface_runoff_flux", unit="kg m-2 s-1"),
    "m01s08i235" : CFname(cfname="subsurface_runoff_flux", unit="kg m-2 s-1"),
    "m01s09i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s09i010" : CFname(cfname="specific_humidity", unit="1"),
    "m01s09i201" : CFname(cfname="stratiform_cloud_area_fraction_in_atmosphere_layer", unit="1"),
    "m01s12i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s12i010" : CFname(cfname="specific_humidity", unit="1"),
    "m01s12i012" : CFname(cfname="mass_fraction_of_cloud_ice_in_air", unit="1"),
    "m01s12i181" : CFname(cfname="tendency_of_air_temperature_due_to_advection", unit="K s-1"),
    "m01s12i182" : CFname(cfname="tendency_of_specific_humidity_due_to_advection", unit="s-1"),
    "m01s12i183" : CFname(cfname="tendency_of_mass_fraction_of_cloud_liquid_water_in_air_due_to_advection", unit="s-1"),
    "m01s12i184" : CFname(cfname="tendency_of_mass_fraction_of_cloud_ice_in_air_due_to_advection", unit="s-1"),
    "m01s12i185" : CFname(cfname="tendency_of_eastward_wind_due_to_advection", unit="m s-1"),
    "m01s12i186" : CFname(cfname="tendency_of_northward_wind_due_to_advection", unit="m s-1"),
    "m01s12i187" : CFname(cfname="tendency_of_upward_air_velocity_due_to_advection", unit="m s-1"),
    "m01s13i181" : CFname(cfname="tendency_of_air_temperature_due_to_diffusion", unit="K s-1"),
    "m01s13i182" : CFname(cfname="tendency_of_specific_humidity_due_to_diffusion", unit="s-1"),
    "m01s13i185" : CFname(cfname="tendency_of_eastward_wind_due_to_diffusion", unit="m s-1"),
    "m01s13i186" : CFname(cfname="tendency_of_northward_wind_due_to_diffusion", unit="m s-1"),
    "m01s15i108" : CFname(cfname="air_pressure", unit="Pa"),
    "m01s15i119" : CFname(cfname="air_potential_temperature", unit="K"),
    "m01s15i127" : CFname(cfname="air_density", unit="kg m-3"),
    "m01s15i142" : CFname(cfname="upward_air_velocity", unit="m s-1"),
    "m01s15i143" : CFname(cfname="eastward_wind", unit="m s-1"),
    "m01s15i144" : CFname(cfname="northward_wind", unit="m s-1"),
    "m01s15i201" : CFname(cfname="eastward_wind", unit="m s-1"),
    "m01s15i202" : CFname(cfname="northward_wind", unit="m s-1"),
    "m01s15i214" : CFname(cfname="ertel_potential_vorticity", unit="K m2 kg-1 s-1"),
    "m01s15i215" : CFname(cfname="air_potential_temperature", unit="K"),
    "m01s15i216" : CFname(cfname="air_potential_temperature", unit="K"),
    "m01s15i217" : CFname(cfname="potential_vorticity_of_atmosphere_layer", unit="Pa-1 s-1"),
    "m01s15i218" : CFname(cfname="potential_vorticity_of_atmosphere_layer", unit="Pa-1 s-1"),
    "m01s15i242" : CFname(cfname="upward_air_velocity", unit="m s-1"),
    "m01s15i243" : CFname(cfname="eastward_wind", unit="m s-1"),
    "m01s15i244" : CFname(cfname="northward_wind", unit="m s-1"),
    "m01s16i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s16i201" : CFname(cfname="geopotential_height", unit="m"),
    "m01s16i202" : CFname(cfname="geopotential_height", unit="m"),
    "m01s16i203" : CFname(cfname="air_temperature", unit="K"),
    "m01s16i222" : CFname(cfname="air_pressure_at_sea_level", unit="Pa"),
    "m01s16i255" : CFname(cfname="geopotential_height", unit="m"),
    "m01s20i003" : CFname(cfname="wind_speed", unit="m s-1"),
    "m01s20i004" : CFname(cfname="wind_speed", unit="m s-1"),
    "m01s20i005" : CFname(cfname="divergence_of_wind", unit="s-1"),
    "m01s20i006" : CFname(cfname="atmosphere_relative_vorticity", unit="s-1"),
    "m01s20i024" : CFname(cfname="tropopause_air_pressure", unit="Pa"),
    "m01s20i025" : CFname(cfname="tropopause_air_temperature", unit="K"),
    "m01s20i026" : CFname(cfname="tropopause_altitude", unit="m"),
    "m01s20i034" : CFname(cfname="air_pressure_at_freezing_level", unit="Pa"),
    "m01s20i064" : CFname(cfname="tropopause_air_pressure", unit="Pa"),
    "m01s20i065" : CFname(cfname="tropopause_air_temperature", unit="K"),
    "m01s20i066" : CFname(cfname="tropopause_altitude", unit="m"),
    "m01s30i003" : CFname(cfname="upward_air_velocity", unit="m s-1"),
    "m01s30i004" : CFname(cfname="air_temperature", unit="K"),
    "m01s30i005" : CFname(cfname="specific_humidity", unit="1"),
    "m01s30i007" : CFname(cfname="specific_kinetic_energy_of_air", unit="m2 s-2"),
    "m01s30i111" : CFname(cfname="air_temperature", unit="K"),
    "m01s30i113" : CFname(cfname="relative_humidity", unit="%"),
    "m01s30i181" : CFname(cfname="tendency_of_air_temperature", unit="K s-1"),
    "m01s30i182" : CFname(cfname="tendency_of_specific_humidity", unit="s-1"),
    "m01s30i183" : CFname(cfname="tendency_of_mass_fraction_of_cloud_liquid_water_in_air", unit="s-1"),
    "m01s30i184" : CFname(cfname="tendency_of_mass_fraction_of_cloud_ice_in_air", unit="s-1"),
    "m01s30i185" : CFname(cfname="tendency_of_eastward_wind", unit="m s-1"),
    "m01s30i186" : CFname(cfname="tendency_of_northward_wind", unit="m s-1"),
    "m01s30i187" : CFname(cfname="tendency_of_upward_air_velocity", unit="m s-1"),
    "m01s30i188" : CFname(cfname="tendency_of_air_density", unit="kg m-3 s-1"),
    "m01s30i201" : CFname(cfname="eastward_wind", unit="m s-1"),
    "m01s30i202" : CFname(cfname="northward_wind", unit="m s-1"),
    "m01s30i203" : CFname(cfname="upward_air_velocity", unit="m s-1"),
    "m01s30i204" : CFname(cfname="air_temperature", unit="K"),
    "m01s30i205" : CFname(cfname="specific_humidity", unit="1"),
    "m01s30i207" : CFname(cfname="geopotential_height", unit="m"),
    "m01s30i208" : CFname(cfname="lagrangian_tendency_of_air_pressure", unit="Pa s-1"),
    "m01s30i211" : CFname(cfname="square_of_eastward_wind", unit="m2 s-2"),
    "m01s30i212" : CFname(cfname="product_of_eastward_wind_and_northward_wind", unit="m2 s-2"),
    "m01s30i213" : CFname(cfname="product_of_eastward_wind_and_upward_air_velocity", unit="m2 s-2"),
    "m01s30i214" : CFname(cfname="product_of_eastward_wind_and_air_temperature", unit="K m s-1"),
    "m01s30i215" : CFname(cfname="product_of_eastward_wind_and_specific_humidity", unit="m s-1"),
    "m01s30i217" : CFname(cfname="product_of_eastward_wind_and_geopotential_height", unit="m2 s-1"),
    "m01s30i218" : CFname(cfname="product_of_eastward_wind_and_omega", unit="Pa m s-1"),
    "m01s30i222" : CFname(cfname="square_of_northward_wind", unit="m2 s-2"),
    "m01s30i223" : CFname(cfname="product_of_northward_wind_and_upward_air_velocity", unit="m2 s-2"),
    "m01s30i224" : CFname(cfname="product_of_northward_wind_and_air_temperature", unit="K m s-1"),
    "m01s30i225" : CFname(cfname="product_of_northward_wind_and_specific_humidity", unit="m s-1"),
    "m01s30i227" : CFname(cfname="product_of_northward_wind_and_geopotential_height", unit="m2 s-1"),
    "m01s30i228" : CFname(cfname="product_of_northward_wind_and_omega", unit="Pa m s-1"),
    "m01s30i233" : CFname(cfname="square_of_upward_air_velocity", unit="m2 s-2"),
    "m01s30i234" : CFname(cfname="product_of_upward_air_velocity_and_air_temperature", unit="K m s-1"),
    "m01s30i235" : CFname(cfname="product_of_upward_air_velocity_and_specific_humidity", unit="m s-1"),
    "m01s30i244" : CFname(cfname="square_of_air_temperature", unit="K2"),
    "m01s30i245" : CFname(cfname="product_of_air_temperature_and_specific_humidity", unit="K"),
    "m01s30i248" : CFname(cfname="product_of_air_temperature_and_omega", unit="K Pa s-1"),
    "m01s30i258" : CFname(cfname="product_of_specific_humidity_and_omega", unit="Pa s-1"),
    "m01s30i277" : CFname(cfname="square_of_geopotential_height", unit="m2"),
    "m01s30i278" : CFname(cfname="product_of_geopotential_height_and_omega", unit="Pa m s-1"),
    "m01s30i288" : CFname(cfname="square_of_lagrangian_tendency_of_air_pressure", unit="Pa2 s-2"),
    "m01s30i302" : CFname(cfname="virtual_temperature", unit="K"),
    "m01s30i401" : CFname(cfname="atmosphere_kinetic_energy_content", unit="J m-2"),
    "m01s30i405" : CFname(cfname="atmosphere_cloud_liquid_water_content", unit="kg m-2"),
    "m01s30i406" : CFname(cfname="atmosphere_cloud_ice_content", unit="kg m-2"),
    "m01s30i417" : CFname(cfname="surface_air_pressure", unit="Pa"),
    "m01s30i418" : CFname(cfname="surface_air_pressure", unit="Pa"),
    "m01s30i451" : CFname(cfname="tropopause_air_pressure", unit="Pa"),
    "m01s30i452" : CFname(cfname="tropopause_air_temperature", unit="K"),
    "m01s30i453" : CFname(cfname="tropopause_altitude", unit="m"),
    "m01s33i041" : CFname(cfname="mole_fraction_of_atomic_chlorine_in_air", unit="1"),
    "m01s33i042" : CFname(cfname="mole_fraction_of_chlorine_monoxide_in_air", unit="1"),
    "m01s33i043" : CFname(cfname="mole_fraction_of_dichlorine_peroxide_in_air", unit="1"),
    "m01s33i044" : CFname(cfname="mole_fraction_of_chlorine_dioxide_in_air", unit="1"),
    "m01s33i047" : CFname(cfname="mole_fraction_of_bromine_chloride_in_air", unit="1"),
    "m01s33i048" : CFname(cfname="mole_fraction_of_bromine_nitrate_in_air", unit="1"),
    "m01s33i049" : CFname(cfname="mole_fraction_of_nitrous_oxide_in_air", unit="1"),
    "m01s33i051" : CFname(cfname="mole_fraction_of_hypochlorous_acid_in_air", unit="1"),
    "m01s33i054" : CFname(cfname="mole_fraction_of_chlorine_nitrate_in_air", unit="1"),
    "m01s33i055" : CFname(cfname="mole_fraction_of_cfc11_in_air", unit="1"),
    "m01s33i056" : CFname(cfname="mole_fraction_of_cfc12_in_air", unit="1"),
    "m01s33i058" : CFname(cfname="mole_fraction_of_atomic_nitrogen_in_air", unit="1"),
    "m01s33i150" : CFname(cfname="age_of_stratospheric_air", unit="1"),
    "m02s00i101" : CFname(cfname="sea_water_potential_temperature", unit="degC"),
    "m02s00i102" : CFname(cfname="sea_water_salinity", unit="1e3 psu @0.035"),
    "m02s00i121" : CFname(cfname="baroclinic_eastward_sea_water_velocity", unit="cm s-1"),
    "m02s00i122" : CFname(cfname="baroclinic_northward_sea_water_velocity", unit="cm s-1"),
    "m02s00i130" : CFname(cfname="ocean_barotropic_streamfunction", unit="cm3 s-1"),
    "m02s00i131" : CFname(cfname="ocean_barotropic_streamfunction", unit="cm3 s-1"),
    "m02s00i132" : CFname(cfname="tendency_of_ocean_barotropic_streamfunction", unit="cm3 s-2"),
    "m02s00i133" : CFname(cfname="tendency_of_ocean_barotropic_streamfunction", unit="cm3 s-2"),
    "m02s00i134" : CFname(cfname="surface_air_pressure", unit="g cm-1 s-2"),
    "m02s00i135" : CFname(cfname="barotropic_eastward_sea_water_velocity", unit="cm s-1"),
    "m02s00i136" : CFname(cfname="barotropic_northward_sea_water_velocity", unit="cm s-1"),
    "m02s00i137" : CFname(cfname="ocean_mixed_layer_thickness", unit="m"),
    "m02s00i139" : CFname(cfname="downward_eastward_stress_at_sea_ice_base", unit="Pa"),
    "m02s00i140" : CFname(cfname="downward_northward_stress_at_sea_ice_base", unit="Pa"),
    "m02s00i141" : CFname(cfname="surface_snow_thickness", unit="m"),
    "m02s00i143" : CFname(cfname="upward_sea_ice_basal_heat_flux", unit="W m-2"),
    "m02s00i146" : CFname(cfname="sea_ice_area_fraction", unit="1"),
    "m02s00i147" : CFname(cfname="sea_ice_thickness", unit="m"),
    "m02s00i148" : CFname(cfname="eastward_sea_ice_velocity", unit="m s-1"),
    "m02s00i149" : CFname(cfname="northward_sea_ice_velocity", unit="m s-1"),
    "m02s00i150" : CFname(cfname="surface_downward_eastward_stress", unit="Pa"),
    "m02s00i151" : CFname(cfname="surface_downward_northward_stress", unit="Pa"),
    "m02s00i152" : CFname(cfname="wind_mixing_energy_flux_into_sea_water", unit="W m-2"),
    "m02s00i166" : CFname(cfname="water_flux_into_sea_water_from_rivers", unit="kg m-2 s-1"),
    "m02s00i171" : CFname(cfname="snowfall_flux", unit="kg m-2 s-1"),
    "m02s00i180" : CFname(cfname="sea_surface_temperature", unit="K"),
    "m02s00i181" : CFname(cfname="sea_surface_salinity", unit="1e3 psu @0.035"),
    "m02s00i182" : CFname(cfname="air_temperature", unit="K"),
    "m02s00i183" : CFname(cfname="sea_ice_thickness", unit="m"),
    "m02s00i185" : CFname(cfname="heat_flux_correction", unit="W m-2"),
    "m02s00i186" : CFname(cfname="water_flux_correction", unit="Kg m-2 s-1"),
    "m02s00i190" : CFname(cfname="surface_snow_and_ice_melt_heat_flux", unit="W m-2"),
    "m02s00i191" : CFname(cfname="downward_heat_flux_in_sea_ice", unit="W m-2"),
    "m02s30i201" : CFname(cfname="upward_sea_water_velocity", unit="cm s-1"),
    "m02s30i202" : CFname(cfname="ocean_mixed_layer_thickness", unit="m"),
    "m02s30i211" : CFname(cfname="northward_ocean_heat_transport", unit="PW"),
    "m02s30i212" : CFname(cfname="northward_ocean_salt_transport", unit="1e7kg s-1"),
    "m02s30i320" : CFname(cfname="eastward_sea_water_velocity", unit="cm s-1"),
    "m02s30i321" : CFname(cfname="northward_sea_water_velocity", unit="cm s-1"),
    "m02s30i324" : CFname(cfname="ocean_mixed_layer_thickness", unit="m"),
    "m02s32i201" : CFname(cfname="tendency_of_sea_ice_area_fraction_due_to_dynamics", unit="s-1"),
    "m02s32i202" : CFname(cfname="tendency_of_sea_ice_thickness_due_to_dynamics", unit="m s-1"),
    "m02s32i209" : CFname(cfname="eastward_sea_ice_velocity", unit="m s-1"),
    "m02s32i210" : CFname(cfname="northward_sea_ice_velocity", unit="m s-1"),
    "m02s32i211" : CFname(cfname="tendency_of_sea_ice_area_fraction_due_to_thermodynamics", unit="s-1"),
    "m02s32i212" : CFname(cfname="tendency_of_sea_ice_thickness_due_to_thermodynamics", unit="m s-1"),
    "m02s32i219" : CFname(cfname="downward_eastward_stress_at_sea_ice_base", unit="Pa"),
    "m02s32i220" : CFname(cfname="downward_northward_stress_at_sea_ice_base", unit="Pa"),
}

LBFC_TO_CF = {
    5 : CFname(cfname="atmosphere_boundary_layer_thickness", unit="m"),
    23 : CFname(cfname="soil_temperature", unit="K"),
    27 : CFname(cfname="air_density", unit="kg m-3"),
    36 : CFname(cfname="land_area_fraction", unit="1"),
    37 : CFname(cfname="sea_ice_area_fraction", unit="1"),
    50 : CFname(cfname="wind_speed", unit="m s-1"),
    73 : CFname(cfname="atmosphere_relative_vorticity", unit="s-1"),
    74 : CFname(cfname="divergence_of_wind", unit="s-1"),
    83 : CFname(cfname="potential_vorticity_of_atmosphere_layer", unit="Pa-1 s-1"),
    94 : CFname(cfname="convective_rainfall_amount", unit="kg m-2"),
    97 : CFname(cfname="rainfall_flux", unit="kg m-2 s-1"),
    102 : CFname(cfname="stratiform_rainfall_amount", unit="kg m-2"),
    108 : CFname(cfname="snowfall_flux", unit="kg m-2 s-1"),
    111 : CFname(cfname="surface_runoff_amount", unit="kg m-2"),
    116 : CFname(cfname="stratiform_snowfall_amount", unit="kg m-2"),
    117 : CFname(cfname="convective_snowfall_amount", unit="kg m-2"),
    122 : CFname(cfname="moisture_content_of_soil_layer", unit="kg m-2"),
    183 : CFname(cfname="wind_speed", unit="m s-1"),
    200 : CFname(cfname="toa_incoming_shortwave_flux", unit="W m-2"),
    203 : CFname(cfname="surface_downwelling_shortwave_flux_in_air", unit="W m-2"),
    206 : CFname(cfname="toa_outgoing_longwave_flux", unit="W m-2"),
    208 : CFname(cfname="surface_downwelling_shortwave_flux_in_air_assuming_clear_sky", unit="W m-2"),
    209 : CFname(cfname="sea_ice_temperature", unit="K"),
    253 : CFname(cfname="tendency_of_air_temperature_due_to_longwave_heating", unit="K s-1"),
    261 : CFname(cfname="downward_heat_flux_in_sea_ice", unit="W m-2"),
    321 : CFname(cfname="root_depth", unit="m"),
    326 : CFname(cfname="vegetation_area_fraction", unit="1"),
    328 : CFname(cfname="surface_albedo_assuming_deep_snow", unit="1"),
    329 : CFname(cfname="volume_fraction_of_condensed_water_in_soil_at_wilting_point", unit="1"),
    330 : CFname(cfname="volume_fraction_of_condensed_water_in_soil_at_critical_point", unit="1"),
    332 : CFname(cfname="soil_porosity", unit="1"),
    333 : CFname(cfname="soil_hydraulic_conductivity_at_saturation", unit="m s-1"),
    335 : CFname(cfname="soil_thermal_capacity", unit="J kg-1 K-1"),
    336 : CFname(cfname="soil_thermal_conductivity", unit="W m-1 K-1"),
    342 : CFname(cfname="soil_suction_at_saturation", unit="Pa"),
    687 : CFname(cfname="sea_ice_thickness", unit="m"),
    701 : CFname(cfname="surface_eastward_sea_water_velocity", unit="m s-1"),
    702 : CFname(cfname="surface_northward_sea_water_velocity", unit="m s-1"),
    981 : CFname(cfname="air_temperature", unit="K"),
    982 : CFname(cfname="specific_humidity", unit="1"),
    984 : CFname(cfname="mass_fraction_of_cloud_ice_in_air", unit="1"),
    1025 : CFname(cfname="surface_downward_eastward_stress", unit="Pa"),
    1026 : CFname(cfname="surface_downward_northward_stress", unit="Pa"),
    1373 : CFname(cfname="mass_fraction_of_dimethyl_sulfide_in_air", unit="1"),
    1374 : CFname(cfname="mass_fraction_of_sulfur_dioxide_in_air", unit="1"),
    1382 : CFname(cfname="leaf_area_index", unit="1"),
    1383 : CFname(cfname="canopy_height", unit="m"),
    1385 : CFname(cfname="mass_fraction_of_unfrozen_water_in_soil_moisture", unit="1"),
    1386 : CFname(cfname="mass_fraction_of_frozen_water_in_soil_moisture", unit="1"),
    1392 : CFname(cfname="leaf_area_index", unit="1"),
    1393 : CFname(cfname="canopy_height", unit="m"),
    1395 : CFname(cfname="soil_albedo", unit="1"),
    1507 : CFname(cfname="snow_grain_size", unit="1e-6 m"),
    1559 : CFname(cfname="soil_moisture_content_at_field_capacity", unit="kg m-2"),
    1720 : CFname(cfname="cloud_area_fraction_in_atmosphere_layer", unit="1"),
}

CF_TO_LBFC = {
    CFname(cfname="age_of_stratospheric_air", unit="1") : 501,
    CFname(cfname="air_density", unit="kg m-3") : 27,
    CFname(cfname="air_potential_temperature", unit="K") : 19,
    CFname(cfname="air_pressure", unit="Pa") : 8,
    CFname(cfname="air_pressure_at_freezing_level", unit="Pa") : 8,
    CFname(cfname="air_pressure_at_sea_level", unit="Pa") : 8,
    CFname(cfname="atmosphere_boundary_layer_thickness", unit="m") : 5,
    CFname(cfname="atmosphere_eastward_stress_due_to_gravity_wave_drag", unit="Pa") : 61,
    CFname(cfname="atmosphere_kinetic_energy_content", unit="J m-2") : 63,
    CFname(cfname="atmosphere_northward_stress_due_to_gravity_wave_drag", unit="Pa") : 62,
    CFname(cfname="atmosphere_relative_vorticity", unit="s-1") : 73,
    CFname(cfname="cloud_area_fraction", unit="1") : 30,
    CFname(cfname="cloud_area_fraction_in_atmosphere_layer", unit="1") : 1720,
    CFname(cfname="convective_cloud_area_fraction", unit="1") : 34,
    CFname(cfname="convective_rainfall_amount", unit="kg m-2") : 94,
    CFname(cfname="convective_snowfall_amount", unit="kg m-2") : 117,
    CFname(cfname="dimensionless_exner_function", unit="1") : 7,
    CFname(cfname="divergence_of_wind", unit="s-1") : 74,
    CFname(cfname="downward_heat_flux_in_sea_ice", unit="W m-2") : 261,
    CFname(cfname="downward_heat_flux_in_soil", unit="W m-2") : 1564,
    CFname(cfname="ertel_potential_vorticity", unit="K m2 kg-1 s-1") : 82,
    CFname(cfname="geopotential_height", unit="m") : 1,
    CFname(cfname="lagrangian_tendency_of_air_pressure", unit="Pa s-1") : 40,
    CFname(cfname="land_binary_mask", unit="1") : 395,
    CFname(cfname="mass_fraction_of_carbon_dioxide_in_air", unit="1") : 1564,
    CFname(cfname="mass_fraction_of_cloud_liquid_water_in_air", unit="1") : 79,
    CFname(cfname="mass_fraction_of_dimethyl_sulfide_in_air", unit="1") : 1373,
    CFname(cfname="mass_fraction_of_frozen_water_in_soil_moisture", unit="1") : 1386,
    CFname(cfname="mass_fraction_of_ozone_in_air", unit="1") : 453,
    CFname(cfname="mass_fraction_of_sulfur_dioxide_in_air", unit="1") : 1374,
    CFname(cfname="mass_fraction_of_unfrozen_water_in_soil_moisture", unit="1") : 1385,
    CFname(cfname="moisture_content_of_soil_layer", unit="kg m-2") : 122,
    CFname(cfname="mole_fraction_of_atomic_chlorine_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_atomic_nitrogen_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_bromine_chloride_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_bromine_nitrate_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_cfc11_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_cfc12_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_chlorine_dioxide_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_chlorine_monoxide_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_chlorine_nitrate_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_dichlorine_peroxide_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_hypochlorous_acid_in_air", unit="1") : 501,
    CFname(cfname="mole_fraction_of_nitrous_oxide_in_air", unit="1") : 501,
    CFname(cfname="rainfall_flux", unit="kg m-2 s-1") : 97,
    CFname(cfname="relative_humidity", unit="%") : 88,
    CFname(cfname="root_depth", unit="m") : 321,
    CFname(cfname="sea_ice_albedo", unit="1") : 322,
    CFname(cfname="sea_ice_area_fraction", unit="1") : 37,
    CFname(cfname="sea_ice_temperature", unit="K") : 209,
    CFname(cfname="sea_ice_thickness", unit="m") : 687,
    CFname(cfname="snow_grain_size", unit="1e-6 m") : 1507,
    CFname(cfname="snowfall_amount", unit="kg m-2") : 93,
    CFname(cfname="snowfall_flux", unit="kg m-2 s-1") : 108,
    CFname(cfname="soil_albedo", unit="1") : 1395,
    CFname(cfname="soil_carbon_content", unit="kg m-2") : 1397,
    CFname(cfname="soil_hydraulic_conductivity_at_saturation", unit="m s-1") : 333,
    CFname(cfname="soil_moisture_content_at_field_capacity", unit="kg m-2") : 1559,
    CFname(cfname="soil_porosity", unit="1") : 332,
    CFname(cfname="soil_suction_at_saturation", unit="Pa") : 342,
    CFname(cfname="soil_temperature", unit="K") : 23,
    CFname(cfname="soil_thermal_capacity", unit="J kg-1 K-1") : 335,
    CFname(cfname="soil_thermal_conductivity", unit="W m-1 K-1") : 336,
    CFname(cfname="specific_kinetic_energy_of_air", unit="m2 s-2") : 60,
    CFname(cfname="stratiform_cloud_area_fraction_in_atmosphere_layer", unit="1") : 220,
    CFname(cfname="stratiform_rainfall_amount", unit="kg m-2") : 102,
    CFname(cfname="stratiform_rainfall_rate", unit="kg m-2 s-1") : 99,
    CFname(cfname="stratiform_snowfall_amount", unit="kg m-2") : 116,
    CFname(cfname="stratiform_snowfall_rate", unit="kg m-2 s-1") : 118,
    CFname(cfname="subsurface_runoff_amount", unit="kg m-2") : 112,
    CFname(cfname="subsurface_runoff_flux", unit="kg m-2 s-1") : 1533,
    CFname(cfname="surface_albedo_assuming_deep_snow", unit="1") : 328,
    CFname(cfname="surface_albedo_assuming_no_snow", unit="1") : 322,
    CFname(cfname="surface_altitude", unit="m") : 1,
    CFname(cfname="surface_downwelling_shortwave_flux_in_air", unit="W m-2") : 203,
    CFname(cfname="surface_downwelling_shortwave_flux_in_air_assuming_clear_sky", unit="W m-2") : 208,
    CFname(cfname="surface_eastward_sea_water_velocity", unit="m s-1") : 701,
    CFname(cfname="surface_net_downward_longwave_flux", unit="W m-2") : 187,
    CFname(cfname="surface_net_downward_shortwave_flux", unit="W m-2") : 186,
    CFname(cfname="surface_northward_sea_water_velocity", unit="m s-1") : 702,
    CFname(cfname="surface_roughness_length", unit="m") : 324,
    CFname(cfname="surface_runoff_amount", unit="kg m-2") : 111,
    CFname(cfname="surface_runoff_flux", unit="kg m-2 s-1") : 1532,
    CFname(cfname="surface_snow_amount", unit="kg m-2") : 93,
    CFname(cfname="surface_temperature", unit="K") : 16,
    CFname(cfname="surface_upward_sensible_heat_flux", unit="W m-2") : 178,
    CFname(cfname="surface_upward_water_flux", unit="kg m-2 s-1") : 184,
    CFname(cfname="surface_upwelling_shortwave_flux_in_air_assuming_clear_sky", unit="W m-2") : 207,
    CFname(cfname="tendency_of_air_density", unit="kg m-3 s-1") : 7,
    CFname(cfname="tendency_of_air_temperature", unit="K s-1") : 16,
    CFname(cfname="tendency_of_air_temperature_due_to_diffusion", unit="K s-1") : 16,
    CFname(cfname="tendency_of_air_temperature_due_to_longwave_heating", unit="K s-1") : 253,
    CFname(cfname="tendency_of_eastward_wind", unit="m s-1") : 56,
    CFname(cfname="tendency_of_eastward_wind_due_to_diffusion", unit="m s-1") : 56,
    CFname(cfname="tendency_of_mass_fraction_of_cloud_ice_in_air", unit="s-1") : 78,
    CFname(cfname="tendency_of_mass_fraction_of_cloud_liquid_water_in_air", unit="s-1") : 79,
    CFname(cfname="tendency_of_northward_wind", unit="m s-1") : 57,
    CFname(cfname="tendency_of_northward_wind_due_to_diffusion", unit="m s-1") : 57,
    CFname(cfname="tendency_of_specific_humidity", unit="s-1") : 95,
    CFname(cfname="tendency_of_specific_humidity_due_to_diffusion", unit="s-1") : 95,
    CFname(cfname="tendency_of_upward_air_velocity", unit="m s-1") : 42,
    CFname(cfname="toa_incoming_shortwave_flux", unit="W m-2") : 200,
    CFname(cfname="toa_outgoing_longwave_flux", unit="W m-2") : 206,
    CFname(cfname="toa_outgoing_longwave_flux_assuming_clear_sky", unit="W m-2") : 210,
    CFname(cfname="toa_outgoing_shortwave_flux", unit="W m-2") : 201,
    CFname(cfname="toa_outgoing_shortwave_flux_assuming_clear_sky", unit="W m-2") : 207,
    CFname(cfname="tropopause_air_pressure", unit="Pa") : 8,
    CFname(cfname="tropopause_air_temperature", unit="K") : 16,
    CFname(cfname="tropopause_altitude", unit="m") : 1,
    CFname(cfname="upward_air_velocity", unit="m s-1") : 42,
    CFname(cfname="vegetation_area_fraction", unit="1") : 326,
    CFname(cfname="virtual_temperature", unit="K") : 16,
    CFname(cfname="volume_fraction_of_condensed_water_in_soil_at_critical_point", unit="1") : 330,
    CFname(cfname="volume_fraction_of_condensed_water_in_soil_at_wilting_point", unit="1") : 329,
    CFname(cfname="water_potential_evaporation_flux", unit="kg m-2 s-1") : 115,
    CFname(cfname="wind_mixing_energy_flux_into_sea_water", unit="W m-2") : 182,
}
